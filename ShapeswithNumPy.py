import matplotlib.pyplot as plt

# Loading the image using Matplotlib
garden_image = plt.imread('garden.jpg')

garden_image.shape
#(height,width,no layers)
print(garden_image.shape)

size = garden_image.size
print(size)


