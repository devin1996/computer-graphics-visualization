from skimage.feature import corner_harris
import matplotlib.pyplot as plt

#convert image to grayscale
image =  rgb2gray(image)

#Apply the harris corner detector on the image
measure_image = corner_harris(image)

#show the harris response image
show_image(measure_image)

#finds the coordinates of the corners
coords  = corner_peaks(corner_harris(image), min_distance=5)

print("A total of", len(coords), "Corners were detected.")

def show_image_with_detected_corners(image, coords, title="Corners detected"):
    plt.imshow(image, interpolation='nearest', cmap='gray')
    plt.title(title)
    plt.plot(coords[:, 1], coords[:, 0], '+r', markersize=15)
    plt.axis('off')
    plt.show()

show_image_with_detected_corners(image, coords)