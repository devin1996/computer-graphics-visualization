from skimage.restoration import inpaint

# Obtain the mask
mask = get_mask(defect_image)

#Apply inpainting to the damaged image using the mask
restored_image = inpaint.inpaint_biharmonic(defect_image, mask, multichannel=True)

#show the resulting image
show_image(defect_image, 'Image Defected')
show_image(restored_image, 'Image restored')