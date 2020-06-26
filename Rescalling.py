from skimage.transform import rescale
import matplotlib.pyplot as plt

# Loading the image using Matplotlib
image = plt.imread('garden.jpg')

#Rescale the image to be 1/4
image_rescaled = rescale(image, 1/4, anti_aliasing=True, multichannel=True)

def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

show_image(image, 'orginal')
show_image(image_rescaled, 'Rescale image')
