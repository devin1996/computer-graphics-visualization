# Import the module and function
from skimage.util import random_noise

# Add noise to the image
noisy_image = random_noise(dog_image)

#show original and resulting image
show_image(dog_image)
show_image(noisy_image, 'Noisy image')