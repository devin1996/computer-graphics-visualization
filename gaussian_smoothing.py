# import the module and function
from skimage.filters import gaussian

import matplotlib.pyplot as plt

def plot_comparison(original, filtered, title_filtered):
    fig, (ax1, ax2) = plt.subplots(ncols=2, figsize=(8, 6), sharex=True, sharey=True)

    ax1.imshow(original, cmap=plt.cm.gray)
    ax1.set_title('original')
    ax1.axis('off')

    ax2.imshow(filtered, cmap=plt.cm.gray)
    ax2.set_title(title_filtered)
    ax2.axis('off')

garden_image = plt.imread('garden.jpg')

#Apply edge detection filter
gaussian_image = gaussian(garden_image, multichannel=True)

plot_comparison(garden_image, gaussian_image, "Blurred with Gaussian Filter")

plt.imshow(gaussian_image)
plt.title('Original')
plt.axis('off')
plt.show()