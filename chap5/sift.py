#!/usr/bin/python
# -*- coding: utf-8 -*-

from PIL import Image
from numpy import *
from pylab import *
import os
import cv2
import numpy as np

def process_image(image_name, output_name):
    # 画像を読み込み、グレースケールに変換
    image = cv2.imread(image_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # SIFT機能を初期化
    sift = cv2.SIFT_create()

    # 特徴点と記述子を検出
    keypoints, descriptors = sift.detectAndCompute(gray, None)
    keypoints = np.array([l.pt for l in keypoints])

    # 特徴点をファイルに保存
    with open(output_name, 'wb') as f:
        np.save(f, descriptors)

    return keypoints, descriptors

def write_features_to_file(filename,locs,desc):
  """ 特徴点の配置と記述子をファイルに保存する """
  savetxt(filename,hstack((locs,desc)))

def plot_features(im,locs,circle=False):
  """ 画像を特徴量とともに描画する。
     入力：im（配列形式の画像）、locs（各特徴量の座標とスケール、方向）"""

  def draw_circle(c,r):
    t = arange(0,1.01,.01)*2*pi
    x = r*cos(t) + c[0]
    y = r*sin(t) + c[1]
    plot(x,y,'b',linewidth=2)

  imshow(im)
  if circle:
    for p in locs:
      draw_circle(p[:2],p[2])
  else:
    plot(locs[:,0],locs[:,1],'ob')
  axis('off')

def match(desc1,desc2):
  """ 第1の画像の各記述子について、第2の画像の対応点を求める。
     入力：desc1（第1の画像の記述子）、desc2（第2の画像の記述子）"""

  desc1 = array([d/linalg.norm(d) for d in desc1])
  desc2 = array([d/linalg.norm(d) for d in desc2])

  dist_ratio = 0.6
  desc1_size = desc1.shape

  matchscores = zeros(desc1_size[0],'int')
  desc2t = desc2.T # あらかじめ転置行列を計算しておく

  for i in range(desc1_size[0]):
    dotprods = dot(desc1[i,:],desc2t) # 内積ベクトル
    dotprods = 0.9999*dotprods
    # 第2の画像の特徴点の逆余弦を求め、ソートし、番号を返す
    indx = argsort(arccos(dotprods))

    # 最も近い近接点との角度が、2番目に近いもののdist_rasio倍以下か？
    if arccos(dotprods)[indx[0]] < dist_ratio * arccos(dotprods)[indx[1]]:
      matchscores[i] = int(indx[0])

  return matchscores

def match_twosided(desc1,desc2): 
  """ 双方向対称バージョンのmatch() """
  # BFMatcherを使用して記述子間のマッチングを行う
  bf = cv2.BFMatcher(cv2.NORM_L2)
  matches = bf.knnMatch(desc1, desc2, k=2)

  # Lowe's ratio testを適用して良いマッチングを選択
  good_matches = []
  for m, n in matches:
      if m.distance < 0.75 * n.distance:
          good_matches.append(m)

  return good_matches

def appendimages(im1,im2):
  """ 2つの画像を左右に並べた画像を返す """

  # 行の少ない方を選び、空行を0で埋める
  rows1 = im1.shape[0]
  rows2 = im2.shape[0]

  if rows1 < rows2:
    im1 = concatenate((im1,zeros((rows2-rows1,im1.shape[1]))),axis=0)
  elif rows1 > rows2:
    im2 = concatenate((im2,zeros((rows1-rows2,im2.shape[1]))),axis=0)
  # 行が同じなら、0で埋める必要はない

  return concatenate((im1,im2), axis=1)


def plot_matches(im1,im2,locs1,locs2,matchscores,show_below=True):
  """ 対応点を線で結んで画像を表示する
    入力： im1,im2（配列形式の画像）、locs1,locs2（特徴点座標）
       machescores（match()の出力）、
       show_below（対応の下に画像を表示するならTrue）"""

  im3 = appendimages(im1,im2)
  if show_below:
    im3 = vstack((im3,im3))

  imshow(im3)

  cols1 = im1.shape[1]
  for i,m in enumerate(matchscores):
    if m>0: plot([locs1[i][0],locs2[m][0]+cols1],[locs1[i][1],locs2[m][1]],'c')
  axis('off')
