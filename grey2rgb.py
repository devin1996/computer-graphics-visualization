from skimage.color import rgb2gray
from skimage import data, io

image = data.camera()
colorImage = rgb2gray(image)
io.imshow(image)
io.show()
