import cv2
import numpy as np


# For Your Eyes Only
frizzy = cv2.imread('images/frizzy.png', 0)
froomer = cv2.imread('images/froomer.png', 0)
cv2.imshow('Frizzy', frizzy)
cv2.imshow('Froomer', froomer)

def detect_edge(img):
    #img = cv2.GaussianBlur(img, (5, 5), 2)
    edges = cv2.Canny(img, 30, 90)
    return edges

# TODO: Find edges in frizzy and froomer images

edge_frizzy = detect_edge(frizzy)
edge_froomer = detect_edge(froomer)

# TODO: Display common edge pixels
# edge images are 0 or 255.
common_edge = edge_frizzy & edge_froomer

cv2.imshow('common edge', common_edge)
cv2.waitKey(0)
