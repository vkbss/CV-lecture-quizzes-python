import cv2

# Explore edge options

# Load an image
img = cv2.imread('images/fall-leaves.png')
cv2.imshow('Image', img)

# TODO: Create a Gaussian filter. Use cv2.getGaussianKernel.

filter_size = 21
filter_sigma = 3;
filter = cv2.getGaussianKernel(filter_size, filter_sigma)
filter = filter * filter.T


# TODO: Apply it, specifying an edge parameter (try different parameters). Use cv2.filter2D.

smoothed = cv2.filter2D(img, -1, filter, borderType = cv2.BORDER_WRAP)

cv2.imshow("smoothed image", smoothed)
cv2.waitKey(0)
