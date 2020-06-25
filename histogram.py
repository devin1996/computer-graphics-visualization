import matplotlib.pyplot as plt

# Loading the image using Matplotlib
garden_image = plt.imread('garden.jpg')

red = garden_image[:, :, 0]
green = garden_image[:, :, 1]
blue = garden_image[:, :, 2]

plt.hist(red.ravel(), bins=256)
plt.title('Red Histogram')
plt.show()

plt.hist(red.ravel(), bins=256)
plt.title('Green Histogram')
plt.show()

plt.hist(red.ravel(), bins=256)
plt.title('Blue Histogram')
plt.show()


# plt.imshow(red)
# plt.show()