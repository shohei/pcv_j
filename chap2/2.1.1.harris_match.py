from PIL import Image
from numpy import *
from pylab import *
import harris

#im1 = array(Image.open('crans_1_small.jpg').convert('L')) 
#im2 = array(Image.open('crans_1_small.jpg').convert('L')) 
im1 = array(Image.open('sf_view1.jpg').convert('L')) 
im2 = array(Image.open('sf_view2.jpg').convert('L')) 

wid = 5

harrisim = harris.compute_harris_response(im1,5)
filtered_coords1 = harris.get_harris_points(harrisim,wid+1)
d1 = harris.get_descriptors(im1,filtered_coords1,wid)

harrisim = harris.compute_harris_response(im2,5)
filtered_coords2 = harris.get_harris_points(harrisim,wid+1)
d2 = harris.get_descriptors(im2,filtered_coords2,wid)

print 'starting matching'
matches = harris.match_twosided(d1,d2)

figure()
gray()
harris.plot_matches(im1,im2,filtered_coords1,filtered_coords2,matches[:100])
show()
