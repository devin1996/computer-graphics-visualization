from skimage.transform import resize
import matplotlib.pyplot as plt

# Loading the image using Matplotlib
image = plt.imread('garden.jpg')

height = 400
width = 500

#Resize image
image_resized = resize(image, (height, width), anti_aliasing=True)
def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()

show_image(image, 'orginal')
show_image(image_resized, 'Resized image')
