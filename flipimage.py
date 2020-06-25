import matplotlib.pyplot as plt
import numpy as np

# Loading the image using Matplotlib
garden_image = plt.imread('garden.jpg')

vertically_flipped = np.flipud(garden_image)

#show_image(vertically_flipped, 'Vertically flipped image')
plt.imshow(vertically_flipped)
plt.title('Vertically flipped image')
plt.axis('off')
plt.show()

horizontly_flipped = np.fliplr(garden_image)
plt.imshow(horizontly_flipped)
plt.title('Horizontally flipped image')
plt.axis('off')
plt.show()