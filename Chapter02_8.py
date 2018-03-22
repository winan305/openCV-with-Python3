# p44 : 영상 중앙에 초점을 맞추는 비네트필터

import cv2
import numpy as np

img = cv2.imread('img/input.jpg')
rows, cols = img.shape[:2]

kernel_x = cv2.getGaussianKernel(int(1.5*cols), 200)
kernel_y = cv2.getGaussianKernel(int(1.5*rows), 200)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
mask = mask[int(0.5*rows):, int(0.5*cols):]
output = np.copy(img)

for i in range(3) :
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow('Original', img)
cv2.imshow('Vignette', output)

cv2.waitKey()