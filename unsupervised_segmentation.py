#Import the modules
from skimage.segmentation import slic
from skimage.color import lab2rgb

#Obtain the segments
segments = segmentation.slic(image)

#put segments on top of original image to compare
segmented_image = label2rgb(segments, image, kind=avg)

show_image(image)
show_image(segmented_image, "Segmented image")