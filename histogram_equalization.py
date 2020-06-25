from skimage import exposure
import matplotlib.pyplot as plt

image = plt.imread('car.jpg')

#Obtain the equalised image
image_eq = exposure.equalize_hist(image)

#CLAHE in scikit-image
image_adapteq = exposure.equalize_adapthist(image, clip_limit=0.03)

def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

show_image(image, 'Original')
show_image(image_eq, 'Histogram  equalized')
show_image(image_adapteq, 'Adaptive equalized')