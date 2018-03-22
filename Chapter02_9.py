# p45~46 : 영상의 대비 향상
# 대비를 얻기 위해 히스토그램 균일화로 불리는 처리를 이용함.

import cv2
import numpy as np

img = cv2.imread('img/input.jpg', 0)

histeq = cv2.equalizeHist(img)

cv2.imshow('Original', img)
cv2.imshow('Histogram equalized', histeq)

cv2.waitKey()