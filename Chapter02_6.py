# p41~42 : 침식과 팽창
# 침식은 구조의 가장 외부 화소 부분을 벗겨냄
# 팽창은 구조의 화소 외부 층을 더하는 것

import cv2
import numpy as np

img = cv2.imread('img/input.jpg', 0)
kernel = np.ones((5,5), np.uint8)

# iterations 는 얼마나 많이 침식/팽창 할 것인가를 결정
# 결과 영상에 연속적으로 적용됨.
img_erosing = cv2.erode(img, kernel, iterations=1)
img_dilation = cv2.dilate(img, kernel, iterations=1)

cv2.imshow('Input', img)
cv2.imshow('Erosing', img_erosing)
cv2.imshow('Dilation', img_dilation)

cv2.waitKey()