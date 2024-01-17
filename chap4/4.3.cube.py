#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from pylab import *
import homography
import camera
import cv2
import numpy as np

def my_calibration(sz):
  row,col = sz
  fx = 2555.0*col/2592
  fy = 2586.0*row/1936
  K = diag([fx,fy,1])
  K[0,2] = 0.5*col
  K[1,2] = 0.5*row
  return K

def process_image(image_name, output_name):
    # 画像を読み込み、グレースケールに変換
    image = cv2.imread(image_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # SIFT機能を初期化
    sift = cv2.SIFT_create()

    # 特徴点と記述子を検出
    keypoints, descriptors = sift.detectAndCompute(gray, None)

    # 特徴点をファイルに保存
    with open(output_name, 'wb') as f:
        np.save(f, descriptors)

    return keypoints, descriptors

def match_twosided(desc1, desc2):
    # BFMatcherを使用して記述子間のマッチングを行う
    bf = cv2.BFMatcher(cv2.NORM_L2)
    matches = bf.knnMatch(desc1, desc2, k=2)

    # Lowe's ratio testを適用して良いマッチングを選択
    good_matches = []
    for m, n in matches:
        if m.distance < 0.75 * n.distance:
            good_matches.append(m)

    return good_matches

# 特徴量を計算する
l0, d0 = process_image('../data/book_frontal.JPG','im0.sift')
l0 = np.array([l.pt for l in l0])

l1, d1 = process_image('../data/book_perspective.JPG','im1.sift')
l1 = np.array([l.pt for l in l1])

# 特徴量を対応づけホモグラフィーを推定する
matches = match_twosided(d0,d1)
ndx = [m.queryIdx for m in matches]
fp = homography.make_homog(l0[ndx,:2].T)
ndx2 = [m.trainIdx for m in matches]
tp = homography.make_homog(l1[ndx2,:2].T)

model = homography.RansacModel()
H = homography.H_from_ransac(fp,tp,model)[0]

def cube_points(c,wid):
  """plotで立方体を描画するための頂点のリストを生成する。
     最初の5点は底面の正方形であり、辺が繰り返されます """
  p = []
  # 底面
  p.append([c[0]-wid,c[1]-wid,c[2]-wid])
  p.append([c[0]-wid,c[1]+wid,c[2]-wid])
  p.append([c[0]+wid,c[1]+wid,c[2]-wid])
  p.append([c[0]+wid,c[1]-wid,c[2]-wid])
  p.append([c[0]-wid,c[1]-wid,c[2]-wid]) # 描画を閉じるため第一点と同じ

  # 上面
  p.append([c[0]-wid,c[1]-wid,c[2]+wid]) 
  p.append([c[0]-wid,c[1]+wid,c[2]+wid]) 
  p.append([c[0]+wid,c[1]+wid,c[2]+wid]) 
  p.append([c[0]+wid,c[1]-wid,c[2]+wid]) 
  p.append([c[0]-wid,c[1]-wid,c[2]+wid]) # 描画を閉じるため第一点と同じ

  # 垂直の辺
  p.append([c[0]-wid,c[1]-wid,c[2]+wid]) 
  p.append([c[0]-wid,c[1]+wid,c[2]+wid]) 
  p.append([c[0]-wid,c[1]+wid,c[2]-wid]) 
  p.append([c[0]+wid,c[1]+wid,c[2]-wid]) 
  p.append([c[0]+wid,c[1]+wid,c[2]+wid]) 
  p.append([c[0]+wid,c[1]-wid,c[2]+wid]) 
  p.append([c[0]+wid,c[1]-wid,c[2]-wid]) 
  return array(p).T

# カメラのキャリブレーション
K = my_calibration((747,1000)) 

# z=0の平面上の辺の長さ0.2の立方体の3Dの点
box = cube_points([0,0,0.1],0.1) 
# 第1の画像の底面の正方形を射影する
cam1 = camera.Camera( hstack((K,dot(K,array([[0],[0],[-1]])) )) ) 

# 最初の点群は、底面の正方形
box_cam1 = cam1.project(homography.make_homog(box[:,:5])) 

# Hを使って第2の画像に点を変換する
box_trans = homography.normalize(dot(H,box_cam1)) 

# cam1とHから第2のカメラ行列を計算する
cam2 = camera.Camera(dot(H,cam1.P)) 
A = dot(linalg.inv(K),cam2.P[:,:3]) 
A = array([A[:,0],A[:,1],cross(A[:,0],A[:,1])]).T 
cam2.P[:,:3] = dot(K,A) 

# 第2のカメラ行列を使って射影する
box_cam2 = cam2.project(homography.make_homog(box))

# テスト：z=0上の点を射影を変換すると同じになるはず
point = array([1,1,0,1]).T 
print(homography.normalize(dot(dot(H,cam1.P),point))) 
print(cam2.project(point))

im0 = array(Image.open('../data/book_frontal.JPG'))
im1 = array(Image.open('../data/book_perspective.JPG'))

# 底面の正方形を2Dに射影
figure() 
imshow(im0) 
plot(box_cam1[0,:],box_cam1[1,:],linewidth=3)

# Hで変換されたものを2Dに射影
figure()
imshow(im1)
plot(box_trans[0,:],box_trans[1,:],linewidth=3)

# 3Dの立方体
figure()
imshow(im1)
plot(box_cam2[0,:],box_cam2[1,:],linewidth=3)

show()

import pickle
print(K)
print(f)

with open('ar_camera.pkl','wb') as f:
  pickle.dump(K,f)
  pickle.dump(dot(linalg.inv(K),cam2.P),f)
