#!/usr/bin/python
# -*- coding: utf-8 -*-

from pylab import *
import imtools

# dirs = ('jkfaces2008_small', 'jkfaces2008_small/aligned')
dirs = [('jkfaces2008_small')]
for dir in dirs:
  imlist = imtools.get_imlist(dir)
  avgimg = imtools.compute_average(sorted(imlist)[:150])
  figure()
  imshow(avgimg)
  gray()
  axis('off')
  title(dir)

show()
