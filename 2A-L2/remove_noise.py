import cv2
import numpy as np

# Apply a Gaussian filter to remove noise
img = cv2.imread('images/saturn.png', 0)
cv2.imshow('Img', img)

# function to set value between 0 and 255, will lose information here. Same as np.clip
# better use normalization, not np.clip.
def set_image_value(image):
    low_value_id = image < 0
    high_value_id = image > 255
    image[low_value_id] = 0
    image[high_value_id] = 255
    image = image.astype(np.uint8)
    return image

# TODO: Add noise to the image
noise_sigma = 25
img_with_noise = set_image_value(img + np.random.randn(*img.shape) * noise_sigma)
cv2.imshow('Img_noise', img_with_noise)

# TODO: Now apply a Gaussian filter to smooth out the noise
kernel_size = 11
kernel_sigma = 2

Gaussian_filter = cv2.getGaussianKernel(kernel_size, kernel_sigma)

# multiply kernel with its transpose to get the 2D kernel.

Gaussian_filter = Gaussian_filter * Gaussian_filter.T
img_with_noise_filtered = cv2.filter2D(img_with_noise, -1, Gaussian_filter)
cv2.imshow('Img_filtered', img_with_noise_filtered)
cv2.waitKey(0)
