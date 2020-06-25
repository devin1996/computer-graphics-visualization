import matplotlib.pyplot as plt

# Loading the image using Matplotlib
garden_image = plt.imread('garden.jpg')

red = garden_image[:, :, 0]
green = garden_image[:, :, 1]
blue = garden_image[:, :, 2]

plt.imshow(garden_image)
plt.show()

plt.imshow(red)
plt.show()

plt.imshow(green)
plt.show()

plt.imshow(blue)
plt.show()

#grey color map
plt.imshow(red, cmap="gray")
plt.title('Red')
plt.axis('off')
plt.show()

plt.imshow(green, cmap="gray")
plt.title('Green')
plt.axis('off')
plt.show()

plt.imshow(blue, cmap="gray")
plt.title('Blue')
plt.axis('off')
plt.show()