from skimage import morphology
from skimage import data
import matplotlib.pyplot as plt

image_horse = data.horse()
#set structuring  element to the rectangular-shaped
selem = morphology.rectangle(12, 6)

#obtain the erosed
erosed_image = morphology.binary_erosion(image_horse, selem=selem)

def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

show_image(erosed_image, 'Erosion')