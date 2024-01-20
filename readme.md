- Downloaded from here: https://www.oreilly.co.jp/pub/9784873116075/index.html



実践コンピュータビジョン サンプルプログラム
===========================================

はじめに
--------

[「実践コンピュータビジョン」](http://www.oreilly.co.jp/books/9784873116075/)のサンプルプログラムについて、本書に掲載順に説明します。

なお、本アーカイブにはプログラムのみ収められているので、画像ファイルは別途ダウンロードしていただく必要があります。empire.jpg等の原著者の提供している画像は、[原著者のサイト](http://programmingcomputervision.com/)から
[pcv\_data.zip](http://programmingcomputervision.com/downloads/pcv_data.zip)
をダウンロードして展開してください。
これ以外の画像ファイルは、各章で説明します。
画像ファイルの配置方法も、各章ごとに記載します。

プログラムの実行は、次のように、それぞれの\*.pyファイルをpythonの引数にして起動します。

    $ python 1.1.pil.py

必要なパッケージや外部プログラムは、本書の付録にしたがって事前にインストールしておいてください。

1章
---

### 準備

pcv\_data.zipからempire.jpgとhouses.pngを展開してカレントディレクトリに置いて下さい。

pcv\_data.zipに含まれるfontimages.zipを、a\_thumbs/\*.jpg
となるように展開して下さい。

### 1.1.pil.py

PILを使って画像ファイルempire.jpgを読み込み、回転や切り貼りをして表示します。

### 1.2.1.matplot.py

Matplotlibを使って画像を表示し点や線を描画します。

### 1.2.2.contour\_histgram.py

等高線画像とヒストグラムを求めて描画します。

### 1.2.3.ginput.py

ユーザーに座標を入力してもらいます。3箇所クリックしてください。

### 1.3.1.arrayimg.py

画像をNumPyの配列に変換して扱います。

### 1.3.2.graylevel.py

グレーレベルを変換します。

### 1.3.4.histeq.py

グレーレベルをヒストグラム平坦化します。

### 1.3.5.average.py

a\_thumb/\*.jpgのフォント画像を読み込んで、平均画像を表示します。

### 1.3.6.pca\_test.py

a\_thumb/\*.jpgのフォント画像を読み込んで、主成分分析をします。

さらに、pickleを用いて、平均と主成分をfont\_pca\_modes.pklというファイルに保存します。このファイルは、6.1.2で用います。

### 1.4.1.gauss.py

ガウシアンでぼかします。

### 1.4.1.gauss\_color.py

色チャンネル毎にガウシアンでぼかします。

### 1.4.2.sobel.py

Sobelフィルタで画像の微分を計算し、x,y方向の微分係数と、勾配の大きさを画像として表示します。勾配画像をmagnitude.pngとして保存します。

### 1.4.2.gauss\_deriv.py

ガウシアン微分を計算し、x,y方向の微分係数と、勾配の大きさを画像として表示します。

### 1.4.3.label.py

画像ファイルhouses.pngを読み込み、ラベリングしてラベル画像を表示します。

### 1.4.3.morph\_opening.py

Opening処理をして、ラベル画像を表示します。

### 1.4.4.1.mat.py

NumPyの配列をMATLAB形式のファイルtest.matに保存し、もう一度読み込んで表示します。

### 1.4.4.2.save\_lena.py

Lena画像を test.jpg として保存します。

### 1.5.denoise.py

ノイズ画像を生成し、ガウシアンとROFでノイズ除去して表示します。ノイズ画像をsynth\_rof.pdf、ガウシアンでノイズ除去した画像をsynth\_gaussian.pdf、ROFでノイズ除去した画像をsynth\_rof.pdfで、それぞれ保存します。

### 1.5.denoise2.py

画像ファイルempire.jpgについて、ROFでノイズ除去して表示します。

### imtools.py

画像に関するユーティリティー関数を収めたモジュールで、他のプログラムから読み込んで使われます。

### pca.py

主成分分析を行うモジュールです。

### rof.py

ROFによりノイズ除去を行うモジュールです。

2章
---

### 準備

pca\_data.zipから、empire.jpg、sf\_view1.jpg、sf\_view2.jpgを展開してカレントディレクトリに置きます。

外部プログラムとして、VLFeatのsiftを用いるので、実行できるようにsiftにパスを通しておいてください。

### 2.1.harris.py

empire.jpgからHarrisコーナーを計算して表示します。

### 2.1.1.harris\_match.py

sf\_view1.jpgとsf\_view2.jpgの間でHarrisコーナーを対応づけて表示します。計算に時間がかかります。

### 2.2.3.sift.py

empire.jpgからSIFT特徴点を検出して表示します。SIFT特徴量をempire.siftというファイルに保存します。

### 2.2.4.sift\_match.py

sf\_view1.jpgとsf\_view2.jpgの間で、SIFT特徴点を対応づけて表示します。SIFT特徴量をsf\_view1.jpg.siftとsf\_view2.jpg.siftとして保存します。

### 2.3.1.panoramio\_dl.py

Panoramioからホワイトハウス周辺の画像をダウンロードし、panoramio/\*.jpg
として保存されます。Panoramioには常に画像が投稿されているので、ダウンロードされるファイルは変動します。

### 2.3.2.pano\_sift\_match.py

Panoramioの画像panoramio/\*.jpgを読み込み、SIFT特徴量を計算して対応付け、対応づけられた特徴点の数を表示します。総当たりで対応付けを計算するのに多少時間がかかります。SIFT特徴量をpanoramio/\*.jpg.siftに保存し、対応付けデータをpanoramio\_matchscores.pkl
に保存します。

### 2.3.3.pydot.py

Pydotを使い、図2-9のグラフを描画して、graph.png に保存します。

### 2.3.3.pano\_pydot.py

先に計算したPanoramioの画像の対応付けデータ（panoramio\_matchscores.pkl）を読み込み、画像の類似グラフを描画して、whitehouse.pngに保存します。

### harris.py

Harrisコーナーを計算したり対応づけをするモジュールです。

### sift.py

VLFeatのsiftを実行してSIFT特徴量を計算したり対応づけするモジュールです。

### imtools.py

1章と同じです。

3章
---

### 準備

pca\_data.zipから、empire.jpg、Univ1.jpg～Univ5.jpgを展開してカレントディレクトリに置きます。

以下の画像を、それぞれFlickrからダウンロードしてください。

-   [billboard\_for\_rent.jpg](http://flickr.com/photos/striatic/21671910/)
    660x1024
-   [blank\_billboard.jpg](http://flickr.com/photos/ericingrum/4038961240/)
    1024x576
-   [cat.jpg](http://flickr.com/photos/kneva/560380352/) 640x428
-   [turningtorso1.jpg](http://flickr.com/photos/newsoresund/8186379972/)
    2336x3504
-   [sunset\_tree.jpg](http://flickr.com/photos/jpck/3344929385/)
    480x640

turningtorso1.jpg は、次のように一部を切り出しておきます。

    import shutil
    from PIL import Image
    fn = 'turningtorso1.jpg'
    shutil.copyfile(fn, fn + '.org')
    src = Image.open(fn)
    dst = src.crop((900,508,1325,1384))
    dst.save(fn)

pcv\_data.zipに含まれるjkfaces.zipを展開し、JPEGファイルをjkfaces2008\_smallにコピーして下さい。pcv\_data.zipのjkfaces.xmlは、データが間違っているので、訳者が作成したjkfaces2008\_small/jkfaces.xmlを使って下さい。

<http://www.scipy.org/Cookbook/RANSAC> のページの一番下からransac.py
をダウンロードしてください。

### 3.2.warping.py

empire.jpgを読み込み、アフィン変換で変形して表示します。

### 3.2.1.warping.py

cat.jpgを変形して、billboard\_for\_rent.jpg の中に合成します。

### 3.2.1.warping\_tri.py

cat.jpgをblank\_billboard.jpg
の中に合成します。単純にアフィン変換したものと、三角形に分割してそれぞれアフィン変換したものを表示します。Pythonde三角形の透明度マップを計算しているので、時間がかかります。

### 3.2.2.delaunay.py

ランダムな点をドロネー三角形分割して表示します。

### 3.2.2.piecewise.py

分割点をturningtorso1\_points.txt
から読み込み、sunset\_tree.jpgを分割アフィンワーピングして、turningtorso1.jpgに合成して表示します。

### 3.2.3.imreg.py

jkfaces2008\_small/jkfaces.xmlと、jkfaces2008\_small/\*.jpgを読み込んで、画像を位置合わせして、jkfaces2008\_small/aligned/\*.jpgに保存します。

### 3.2.3.average.py

jkfaces2008\_small/\*.jpg
の平均画像と、jkfaces2008\_small/aligned/\*.jpg
の平均画像を求めて表示します。

### 3.2.3.pca.py

顔画像に楕円形のマスクをかけて主成分分析をして表示します。

### 3.3.2.sift.py

Univ1.jpg～Univ5.jpgのSIFT特徴量を計算して対応づけて表示します。SIFT特徴量をUniv1.sift～Univ5.siftにそれぞれ保存します。対応付けに多少時間がかかります。

### 3.3.3.ransac\_pano.py

Univ1.jpg～Univ5.jpgのSIFT特徴量を計算し、RANSACでロバストに対応づけて、パノラマ画像を合成します。対応付けと合成に非常に時間がかかります。

画像を縮小すれば時間を短縮できます。その際、Univ4.jpgとUniv5.jpgの対応点が少なくてエラーになることがあります。その場合は、H\_43の計算とim\_42の合成をコメントアウトし、im\_32を表示するようにして下さい。

### warp.py

画像の変形を行うモジュールです。

### homograpy.py

ホモグラフィー関連のモジュールです。

### imregistration.py

画像の位置合わせをするモジュールです。

### imtools.py, pca.py, sift.py

前述のものと同じです。

4章
---

### 準備

<http://www.robots.ox.ac.uk/~vgg/data/data-mview.html>の「Model
House」から「3D geometry: points, line segments, camera
matrices」をクリックして、3D.tar.gzをダウンロードします。そこから、house.p3dを取り出します。

    $ tar xvzf 3D.tar.gz house.p3d

pca\_data.zipから、book\_frontal.JPG, book\_perspective.JPG,
book\_perspective.bmpを展開してカレントディレクトリに置きます。

<http://www.pygame.org/wiki/OBJFileLoader>から、上の部分をコピーして、objloader.pyとして保存します。

<http://www.oyonale.com/modeles.php?page=56>から、toyplane\_obj.zip
をダウンロードし、toplane.objを展開します。

### 4.1.2.camera.py

house.p3dを読み込んで、射影変換して表示します。また、ランダムな軸に回転して表示します。

### 4.1.3.rq.py

カメラ行列をRQ分解して表示します。

### 4.3.cube.py

book\_frontal.JPGとbook\_perspective.JPGのSIFT特徴点を求め、RANSACでロバストに特徴点を対応づけて、カメラパラメータを求め、book\_perspective.JPGの上に四角形と立方体を描きます。SIFT特徴量を
im0.sift,im1.siftに保存します。推定したカメラパラメータを、ar\_camera.pklに保存します。

### 4.4.4.teapot.py

上で求めたカメラパラメータar\_camera.pklを読み込んで、book\_perspective.bmpの上に、ユタ・ティーポットを描画します。

### 4.4.5.toyplane.py

上で求めたカメラパラメータar\_camera.pklを読み込み、飛行機の3Dモデルtoyplane.objを読み込んで、book\_perspective.bmpの上に、飛行機を描画します。3Dモデルの読み込みに多少の時間がかかります。

### camera.py

カメラパラメータを管理するCameraクラスです。

### toyplane.mtl

飛行機の3Dモデル用のマテリアルファイルです。

### sift.py, homograpy.py, ransac.py

前述のものと同じです。

5章
---

### 準備

<http://www.robots.ox.ac.uk/~vgg/data/data-mview.html>の「Merton College
I」から、以下のファイルをダウンロードして展開してください。

-   「images - 3
    frames」からimages.tar.gzをダウンロードし、サブディレクトリ
    images/に展開してください。
-   「2D geometry: interest points, line segments,
    matches」から2D.tar.gz をダウンロードして、サブディレクトリ
    2D/に展開してください。
-   「3D geometry: camera matrices, points, line segments」から3D.tar.gz
    をダウンロードして、サブディレクトリ 3D/に展開してください。

pca\_data.zipから、alcatraz1.jpg,
alcatraz2.jpgを展開してカレントディレクトリに置きます。

<http://vision.middlebury.edu/stereo/data/scenes2001/>の「Tsukuba」をクリックし、scene1.row3.col3.ppmと、scene1.row3.col4.ppmをダウンロードします。

### 5.1.1.merton2d.py

Merton Collegeのデータを読み込み、画像の上にコーナーを描画します。

### 5.1.2.testplot3d.py

テストデータを3Dプロットします。

### 5.1.2.merton3d.py

Merton
Collegeのデータを読み込み、コーナーを3Dプロットします。マウスの左ボタンのドラッグ操作で回転、右ボタンのドラッグ操作で拡大縮小することができます。

### 5.1.4.sfm.py

エピ極とエピポーラ線を描画します。

### 5.2.1.triangulate.py

三角測量を実行し、復元した3Dの点と正解の点を描画します。

### 5.2.2.compute.py

3D点の対応からカメラ行列を推定して描画します。

### 5.3.2.recon3d.py

alcatraz1.jpgとalcatraz2.jpgのSIFT特徴点を求め、RANSACでロバストに対応づけて、カメラ行列を求め、特徴点の3D座標を推定して描画します。計算に非常に時間がかかります。

### 5.4.1.stereo.py

scene1.row3.col3.ppmとscene1.row3.col4.ppmを読み込んで、視差マップ画像を計算します。一様フィルタの結果を
depth.png、ガウシアンを用いた結果を depthg.pngに保存します。

### load\_vggdata.py

Merton College I の画像、2D、3Dデータを読み込むモジュールです。

### sfm.py

カメラパラメータを推定するモジュールです。

### stereo.py

ステレオ画像の視差マップを計算するモジュールです。

### sift.py, homograpy.py, ransac.py, camera.py

前述のものと同じです。

6章
---

### 準備

pca\_data.zip
に含まれるselectedimages.zipを展開し、画像ファイルをサブディレクトリ
selected\_fontimages/ にコピーします。

pca\_data.zip から empire.jpg を展開します。

pca\_data.zip
に含まれるsunsets.zipを展開し、画像ファイルをサブディレクトリ
flickr-sunsets/ にコピーします。

1章で保存したfont\_pca\_modes.pklをコピーします。

2章でダウンロードしたpanoramio/\*.jpgと、計算して保存した
panoramio\_matchscores.pklをコピーします。

### 6.1.1.kmeans.py

k平均法を用いて、ランダムな2Dの点をクラスタリングして描画します。

### 6.1.2.img\_clustering.py

フォント画像の主成分分析の結果font\_pca\_modes.pklを用いて、selected\_fontimages/\*.jpgの第40主成分までを射影して、k平均法でクラスタリングします。

### 6.1.3.plot\_cluster.py

2つの主成分に射影した結果を2Dプロットします。

### 6.1.4.pixel.py

k平均法を使ってピクセルをクラスタリングして表示します。

### 6.2.hcluster.py

ランダムな2群の数字を階層クラスタリングします。

### 6.2.1.sunset\_hclustering.py

flickr-sunsets/\*.jpg
を階層クラスタリングし、系統図と3要素以上あるクラスタを表示します。系統図は、sunset.pdf
に保存されます。

### 6.2.1.font\_hclustering.py

selected\_fontimages/\*.jpgを階層クラスタリングして、系統図を表示します。系統図は、fonts.jpg
に保存されます。

### 6.3.font\_spectral.py

フォント画像をスペクトラルクラスタリングし、クラスタを表示します。

### 6.3.pano\_spectral.py

Panoramio画像をスペクトラルクラスタリングし、クラスタを表示します。

### hcluster.py

階層クラスタリングをするモジュールです。

### imtools.py

1章と同じです。

7章
---

### 準備

<http://www.vis.uky.edu/~stewe/ukbench/>の「Download」の「Zipped
File」をクリックして、ukbench.zip
をダウンロードしてください。約1.5GBあります。これに含まれるファイルのうち、ukbench00000.jpg～ukbench00999.jpgを、サブディレクトリ
first1000/にコピーします。

### 7.2.1.mk\_imlist.py

first1000/\*.jpg
の一覧から、ukbench\_imlist.pklとwebimlist.txtを保存します。

### 7.2.1.mk\_sift.py

first1000/\*.jpgのSIFT特徴量を計算し、first1000/\*.siftとして保存します。1000枚の画像を処理するのに時間がかかります。

### 7.2.1.mk\_voc.py

first1000/\*.siftを読み込んで、ボキャブラリを学習して、vocabulary.pklを保存します。学習に非常に時間がかかります。また、メモリ不足だとMemoryErrorで異常終了することがあります。その場合には、使用する画像枚数を減らして下さい。

### 7.3.2.mk\_index.py

vocabulary.pklを読み込んで、SQLiteのデータベースファイルtest.dbにインデクスを登録します。

### 7.3.2.query.py

test.dbから、画像数と、最初の画像ファイル名を問い合わせて表示します。

### 7.4.1.imagesearch.py

先頭の画像に類似した画像IDを10件表示します。ビジュアルワードのヒストグラムの一致数だけを用いているので精度が悪いです。

### 7.4.2.query\_by\_image.py

先頭の画像に類似した画像IDを10件表示します。ヒストグラムの距離を用いているので、精度が良くなります。

### 7.4.3.bench.py

ukbenchスコアを計算します。処理に時間がかかります。

### 7.4.3.plot.py

先頭画像に類似した画像の検索結果を描画します。

### 7.5.rerank.py

特徴点の一致度を用いて、リランキングします。

### vocabulary.py

ビジュアルワードのボキャブラリを学習するためのモジュールです。

### imagesearch.py

画像検索のモジュールです。

### searchdemo.py

CherryPiを用いた画像検索Webアプリです。webimlist.txt、vocabulary.pklを読み込みます。設定ファイルservice.confを編集する必要があります。

### loaddata.py

ukbench\_imlist.pklとvocabulary.pklを読み込むモジュールです。

### imtools.py, homograpy.py, sift.py

前述のものと同じです。

8章
---

### 準備

<http://www.idiap.ch/resource/gestures/>の「Sebastien Marcel Static Hand
Posture
Database」から、「test\_set\_16.3Mb」をクリックし、shp\_marcel\_test.tar.gzをダウンロードします。
展開して、{A,B,C,Five,Point,V}のそれぞれのuniform/の中にあるppmファイルを、だいたい半分ずつ、訓練用
train/ と、テスト用
test/にコピーします。たとえば、次のように分配します。

-   train/A-uniform01～29.ppm, test/A-uniform30～59.ppm
-   train/B-uniform01～29.ppm, test/B-uniform30～61.ppm
-   train/C-uniform01～29.ppm, test/C-uniform30～65.ppm
-   train/Five-uniform01～29.ppm, test/Five-uniform30～76.ppm
-   train/Point-uniform01～29.ppm, test/Point-uniform30～65.ppm
-   train/V-uniform01～29.ppm, test/V-uniform30～57.ppm

次のようにshellのワイルドカードを活用してmvすると簡単に分配できます。

    $ mv Marcel-Test/*/uniform/*uniform[0-2]?.ppm train
    $ mv Marcel-Test/*/uniform/*.ppm test

pcv\_data.zipに含まれるsudoku\_images.zipから、sudoku\_images/ocr\_data/{training,testing}/\*.jpg
を展開します。

### 8.1.1.mk\_2dp.py

ランダムな2D座標を生成し
points\_normal.pklとpoints\_ring.pklに保存します。いちど実行して、points\_normal.pkl
を points\_normal\_test.pkl、points\_ring.pkl を points\_ring\_test.pkl
にコピーしてから、もう一度実行して、合計4つのpklファイルを作成してください。

### 8.1.1.knn\_n.py

points\_normal.pklとpoints\_normal\_test.pklを読み込んで、k近傍法で分類して、表示します。時間がかかります。

### 8.1.1.knn\_r.py

points\_ring.pklとpoints\_ring\_test.pklを用います。

### 8.1.2.dsift.py

empire.jpgの密なSIFT特徴量を計算してempire.siftに保存し、特徴点を表示します。

### 8.1.3.mk\_dsift.py

test/\*.jpg と train/\*.jpg
について、密なSIFT特徴量を求めて、test/\*.dsift、train/\*.dsift
を作成します。

### 8.1.3.knn\_g.py

k近傍法分類器を
train/\*.dsiftを用いて訓練し、test/\*.dsiftでテストして結果を表示します。

### 8.2.bayes\_n.py

points\_normal.pklとpoints\_normal\_test.pklを読み込んで、ベイズ分類器で分類して、表示します。多少時間がかかります。

### 8.2.bayes\_r.py

points\_ring.pklとpoints\_ring\_test.pklを用います。

### 8.2.1.bayes\_g.py

ベイズ分類器を
train/\*.dsiftを用いて訓練し、test/\*.dsiftでテストして結果を表示します。

### 8.3.1.svm\_n.py

points\_normal.pklとpoints\_normal\_test.pklを読み込んで、SVMで分類して、表示します。

### 8.3.1.svm\_r.py

points\_ring.pklとpoints\_ring\_test.pklを用います。

### 8.3.2.svm\_g.py

SVMを
train/\*.dsiftを用いて訓練し、test/\*.dsiftでテストして結果を表示します。

### 8.4.3.ocr.py

sudoku\_images/ocr\_data/training/\*.jpg
を用いてSVMを訓練し、sudoku\_images/ocr\_data/testing/\*.jpg
でテストします。 また、sudoku\_images/sudokus/sudoku18.JPG
を読み込み、数字の認識結果を表示します。

### 8.4.5.rectify.py

sudoku\_images/sudokus/sudoku8.JPGを表示するので、枠の4隅を左上から順に時計回りにクリックしてください。しばらくすると、位置合わせをした画像を表示します。

### dsift.py

siftを実行して密なSIFT特徴量を計算し
.siftファイルを保存するモジュールです。

### knn.py

k近傍法分類器のモジュールです。

### bayes.py

ベイズ分類器のモジュールです。

### 

前述のものと同じです。

9章
---

### 準備

pcv\_data.zipからempire.jpg、ceramic-houses\_t0.pngを展開してカレントディレクトリに置いて下さい。

<http://research.microsoft.com/en-us/um/cambridge/projects/visionimagevideoediting/segmentation/grabcut.htm>の「Ground
truth database」の「Labelling -
Rectangle」をクリックし、boundary\_GT\_rect.zipをダウンロードして、376043.bmpをカレントディレクトリに展開します。

<http://www.eecs.berkeley.edu/Research/Projects/CS/vision/grouping/segbench/>の「Downloads　Segmentation
Dataset」の\[images\]をクリックして、BSD300-images.tgz
をダウンロードして展開します。BSD300/images/test/376043.jpg
をカレントディレクトリにコピーします。

8章の準備で説明した「Sebastien Marcel Static Hand Posture
Database」のshp\_marcel\_test.tar.gzから、C/uniform/C-uniform03.ppm
をカレントディレクトリに展開します。

### 9.1.graphcut.py

サンプルのグラフをカットします。

### 9.1.1.graphcut.py

empire.jpgをグラフカットで領域分割して表示します。非常に時間がかかります。

### 9.1.2.grabcut.py

376043.bmpを注釈データとして、376043.jpgをグラフカットで領域分割して、labelplot.pdfに保存します。非常に時間がかかります。

### 9.2.ncut.py

C-uniform03.ppmを正規化カットで領域分割します。時間がかかります。

### 9.3.chanvese.py

Chan-Vese領域分割モデルに基づき、ceramic-houses\_t0.pngを領域分割して表示します。時間がかかります。

### graphcut.py

グラフカットを実行するモジュールです。

### ncut.py

正規化カットを実行するモジュールです。

### bayse.py, rof.py

前述のものと同じです。

10章
----

### 準備

pcv\_data.zipからempire.jpg、fisherman.jpgを展開してカレントディレクトリに置いて下さい。

<http://www.robots.ox.ac.uk/~vgg/data/data-mview.html>のページから、「Dinosaur」の「Images
- 36 frames」をクリックして、images.tar.gzをダウンロードし、viff.\*.ppm
を展開します。

上と同じページから、「Corridor」の「Images - 11
frames」をクリックして、images.tar.gzをダウンロードし、bt.\*.pgm
を展開します。

### 10.2.1.loadsave.py

OpenCVを用いて、empire.jpg
を読み込み、サイズを表示して、PNG形式でresult.pngを保存します。また、グレースケール画像をresultgray.pngに保存します。

### 10.2.3.integral.py

fisherman.jpgを読み込み、積分画像を作成して、result.jpgに保存します。

### 10.2.3.floodfill.py

fisherman.jpgを読み込み、単色で塗りつぶして表示します。何かキーを押すとウィンドウが閉じます。結果をresult.jpgに保存します。

### 10.2.3.surf.py

empire.jpgのSURF特徴量を計算して表示します。

### 10.3.1.video.py

test.aviから動画をキャプチャし、スペースを押すとフレームをvid\_result.jpgに保存します。ESCで終了します。

### 10.3.1.video\_gauss.py

test.aviから動画をキャプチャし、ガウシアンでぼかします。ESCで終了します。

### 10.3.2.video.py

test.aviから動画をキャプチャし、NumPy配列に格納します。ESCで終了します。

### 10.4.1.optflow.py

test.aviから動画をキャプチャし、オプティカルフローを描画します。

### 10.4.2.1.lk.py

Lucas-Kanade法を使って、bt.003.pgm ～ bt.000.pgm
の特徴点を追跡します。何かキーを押すと、次のフレームを表示します。

### 10.4.2.2.lk\_gen.py

Lucas-Kanade法を使って、viff.000.ppm ～ viff.004.ppm
の特徴点を追跡して奇跡を描画します。

### lktrack.py

Lucas-Kanade法を使って特徴点を追跡するモジュールです。

付録B
-----

### 準備

<https://code.google.com/p/flickrpy/>からflickr.pyをダウンロードします。

[FlickrのAPI
Keys](http://www.flickr.com/services/api/keys/)で認証すると、KeyとSecretのキーが発行されるので、flickr.pyを編集してAPI\_KEYとAPI\_SECRETに設定します。

### tagdownload.py

Flickrから指定したタグの付いた画像をダウンロードするプログラムです。
次のように実行します。

    $ python tagdownload.py sunset

カレントディレクトリに画像ファイルとファイルのURLリスト urllist.txt
が保存されます。