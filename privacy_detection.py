#Import Cascade of classifier and gaussian filter
from skimage.feature import Cascade
from skimage.filters import gaussian

#detect the faces
detected = detector.detect_multi_scale(img=image,
                                       scale_factor=1.2, step_ratio=1,
                                       min_size=(50, 50), max_size=(100, 100))

def getFace(d):
    '''Extractes the face rectangle from the image using the cordinates of the detected'''
    # X and Y starting points of the rectangle
    x, y = d['r'], d['c']

    #the width an height of the face rectangle
    width, height = d['r'] + d['width'], d['c'] + d['height']

    #Extract the detected face
    face = image[x:width, y:height]
    return face

#For each detected face
for d in detected:
    #Obtain the face cropped from the detected coordinates
    face =getFace(d)

def mergeBlurryFace(original, gaussian_image):
    #X and y starting points of the face rectangle
    x, y = d['r'], d['c']
    #the width and height of the face rectangle
    width, height = d['r'] + d['width'], d['c'] + d['height']

    original[x:width, y=height] =gaussian_image
    return original
