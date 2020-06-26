from skimage import measure
from skimage.filters import threshold_otsu

image = color.rgb2gray(image)

#obtain the optimal thresh value of the image
thresh = threshold_otsu(image)

#Apply thresholding and obtain binary image
thresholded_image = image > thresh

#find contours at a constant value of 0.8
contours = measure.find_contours(thresholded_image, 0.8)

#contours:list of (n,2) -ndarrays
for contour in contours
    print(contour.shape)


