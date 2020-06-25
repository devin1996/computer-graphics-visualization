#Import module and function
from skimage.filters import sobel
from skimage import data,io

image = data.camera()


image = data.coins()

#apply edge detection filter
edge_sobel = sobel(image)

#Show original and resultig image to compare
io.imshow(image)
io.show()

io.imshow(edge_sobel)
io.show()