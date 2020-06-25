from skimage import data
from skimage.filters import try_all_threshold
import matplotlib.pyplot as plt

image = data.page()

#obtain optimal threshold value
thresh =127

# Apply threshold to the image
binary = image > thresh
inverted_binary = image <= thresh

plt.imshow(image)
plt.title('Original')
plt.axis('off')
plt.show()

plt.imshow(binary)
plt.title('Thresholded')
plt.axis('off')
plt.show()

plt.imshow(inverted_binary)
plt.title('Invertd Thresholded')
plt.axis('off')
plt.show()

#obtain all the resulting images
fig, ax = try_all_threshold(image, verbose=False)

#showing resulting plots
#show_plot(fig, ax)

#Optial threshhold value

#Global unniform background

#Import the otsu threshold function
from skimage.filters import threshold_otsu

#Obtain the optimal threshold value
thresh = threshold_otsu(image)

#apply thresh holding to the image
binary_global = image > thresh

plt.imshow(binary_global)
plt.title('Global background')
plt.axis('off')
plt.show()

#Local Uneven background

#import the local threshold function
from skimage.filters import threshold_local

# Set the block size to 35
block_size = 35

# Obtain the optimal local thresholding
local_thresh = threshold_local(image, block_size, offset=10)

#Apply local thresholding and obtain the binary image
binary_local = image > local_thresh

plt.imshow(binary_local)
plt.title('Local thresholding')
plt.axis('off')
plt.show()
