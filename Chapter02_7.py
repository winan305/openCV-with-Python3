# p42~43 : 비네트 필터의 생성
# 비네트 필터는 기본적으로 영상의 특정 부분에는 밝게, 다른 부분에는 어둡게 하는 것에 초점을 둠.

import cv2
import numpy as np

img = cv2.imread('img/input.jpg')
rows, cols = img.shape[:2]

# 두번째 인자는 가우시안의 표준편차
# 밝은 중앙 영역의 반지름을 조저암.
kernel_x = cv2.getGaussianKernel(cols, 200)
kernel_y = cv2.getGaussianKernel(rows, 200)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

for i in range(3) :
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow('Original', img)
cv2.imshow('Vignette', output)

cv2.waitKey()