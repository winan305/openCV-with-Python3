# p36 : 모션블러

import cv2
import numpy as np

img = cv2.imread('img/input.jpg')
cv2.imshow('Original', img)

size = 15

# size에 맞는 커널 생성.

# size * size 크기의 numpy 배열을 0으로 채운다.
kernel_motion_blur = np.zeros((size, size))
# 수평 방향 블러링을 위해 가운데 요소들을 1로 채운다.
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
# 요소들을 나눠준다.
kernel_motion_blur = kernel_motion_blur / size
print(kernel_motion_blur)

output = cv2.filter2D(img, -1, kernel_motion_blur)

cv2.imshow('Motion blur', output)

cv2.waitKey()