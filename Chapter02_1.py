# p31~32 : 블러링

import cv2
import numpy as np

img = cv2.imread('img/input.jpg')
rows, cols = img.shape[:2]

# 커널 = 영상필터. 커널을 영상에 적용하는 것을 영상 필터링 이라고 함.
kernel_identity = np.array([[0,0,0],[0,1,0],[0,0,0]])
kernel_3x3 = np.ones((3,3), np.float32)/9.0
kernel_5x5 = np.ones((5,5), np.float32)/25.0

cv2.imshow('Original', img)

# 커널을 영상에 적용시킴.
output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow('Identity filter', output)

output = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow('3x3 filter', output)

output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow('5x5 filter', output)

# 커널을 생성하지 않고 openCV에서 제공하는 함수 사용
output = cv2.blur(img, (10,10))
cv2.imshow('Using cv2.blur', output)

cv2.waitKey()