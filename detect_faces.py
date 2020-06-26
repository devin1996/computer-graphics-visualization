#import tha classifier class
from skimage.feature import Cascade
import matplotlib.pyplot as plt

#load the trained file from the module root.
trained_file = data.lpp_frontal_face_cascade_filename()

#initilize the detector cascade
detector = Cascade(trained_file)

#apply detector on the image
detected = detector.detect_multi_scale(img=image,
                                       scale_factor=1.2,
                                       step_ratio=1,
                                       min_size=(10,10),
                                       max_size=(200,200))
print(detected)

def show_detected_face(result, detected, title="Face image"):
    plt.imshow(result)
    img_desc = plt.gca()
    plt.set_camp('gray')
    plt.title(title)
    plt.axis('off')

    for patch in detected:
        img_desc.add_patch(
            patches.Rectangle(
                (patch['c'], patch['r']),
                patch['width'],
                patch['height'],
                fill=False,color='r',linewidth=2)
        )

    plt.show()
show_deteccted_face(image, detected)