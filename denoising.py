from skimage.restoration import denoise_tv_chambolle

#Apply total variation filter denoising
denoised_image = denoise_tv_chambolle(noisy_image,weight=0.1, multichannel=True)

#Show denoised_image
show_image(noisy_image, 'Noisy image')
show_image(denoised_image, 'Denoised image')

from skimage.restoration import denoise_bilateral

#Apply total variation filter denoising
denoised_image_bilateral_filter = denoise_bilateral(noisy_image, multichannel=True)

#Show denoised_image
show_image(noisy_image, 'Noisy image')
show_image(denoised_image_bilateral_filter, 'Denoised image')