# p46~47 : 컬러 영상을 어떻게 다룰 것인가?
# 9 에서 그레이 영상에 히스토그램 균일화를 적용하였음
# 컬러 영상에 어떻게 적용할 것인지에 대한 예제
# RGB 채널을 분리하여 합치는 것은 안됨. 그래서 YUV 컬러공간으로 바꾼 뒤 Y채널을 균일화하고 합침.

import cv2
import numpy as np

img = cv2.imread('img/input.jpg')
img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])

img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

cv2.imshow('Original', img)
cv2.imshow('Histogram equalized', img_output)

cv2.waitKey()