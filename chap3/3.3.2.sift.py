#!/usr/bin/python
# -*- coding: utf-8 -*-

import sift

featname = ['../data/Univ'+str(i+1)+'.sift' for i in range(5)]
imname = ['../data/Univ'+str(i+1)+'.jpg' for i in range(5)]
l = {}
d = {}
for i in range(5):
  l[i], d[i] = sift.process_image(imname[i],featname[i])

matches = {}
for i in range(4):
  matches[i] = sift.match(d[i+1],d[i])

from PIL import Image
from numpy import *
from pylab import *

im = [array(Image.open(imname[i]).convert('L')) for i in range(5)]
for i in range(4):
  figure()
  gray()
  sift.plot_matches(im[i+1],im[i],l[i+1],l[i],matches[i])
show()
