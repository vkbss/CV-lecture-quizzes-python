import cv2
import numpy as np


# Helper function
def imnoise(img_in, method, dens):

    if method == 'salt & pepper':
        img_out = np.copy(img_in)
        r, c = img_in.shape
        x = np.random.rand(r, c)
        ids = x < dens / 2.
        img_out[ids] = 0
        ids = dens / 2. <= x
        ids &= x < dens
        img_out[ids] = 255

        return img_out

    else:
        print "Method {} not yet implemented.".format(method)
        exit()

# Apply a median filter

# Read an image
img = cv2.imread('images/moon.png', 0)
cv2.imshow('Image', img)

# TODO: Add salt & pepper noise
noisy_img = imnoise(img, 'salt & pepper', 0.02)
cv2.imshow('noisy image', noisy_img)

# TODO: Apply a median filter. Use cv2.medianBlur
median_filtered = cv2.medianBlur(noisy_img, 3)
cv2.imshow('filtered image', median_filtered)
