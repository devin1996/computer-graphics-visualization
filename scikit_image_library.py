#get pre stored data from the library which is a rocket
from skimage import data, io

rocket_image = data.rocket()
io.imshow(rocket_image)
io.show()
