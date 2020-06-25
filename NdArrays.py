import matplotlib.pyplot as plt

# Loading the image using Matplotlib
garden_image = plt.imread('garden.jpg')
type(garden_image)

print(type(garden_image))

red = garden_image[:, :, 0]
green = garden_image[:, :, 1]
blue = garden_image[:, :, 2]

plt.imshow(green)
plt.show()