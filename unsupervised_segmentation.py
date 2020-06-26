#Import the modules
from skimage.segmentation import slic
from skimage.color import lab2rgb

#Obtain the segments
segments = segmentation.slic(image)

#put segments on top of original image to compare
segmented_image = label2rgb(segments, image, kind=avg)

show_image(image)
show_image(segmented_image, "Segmented image")

#Obtain the segments with 300 regions
segments = segmentation.slic(image, n_segments=300)

#put segements on top of original image to compare
segmented_images = lab2rgb(segements, image, kind='avg')

show_image(segmented_images)
