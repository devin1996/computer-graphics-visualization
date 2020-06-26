from skimage.transform import rotate
import matplotlib.pyplot as plt

# Loading the image using Matplotlib
image = plt.imread('garden.jpg')
#Rotate the image 90 degrees clockwise
image_rotated = rotate(image, -90)

def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

show_image(image, 'orginal')
show_image(image_rotated, 'Rotated 90 degrees clockwise')

image_rotated_anticlockwise = rotate(image, 90)

show_image(image_rotated_anticlockwise, 'Rotated 90 degrees anticlockwise')

