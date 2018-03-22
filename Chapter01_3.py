# p13~14 : 영상 이동

import cv2
import numpy as np

img = cv2.imread('img/input.jpg')
# 이미지의 가로, 세로 저장
num_rows, num_cols = img.shape[:2]

# 변환행렬 생성
translation_matrix = np.float32([[1,0,70], [0,1,110]])

# 변환 이미지 생성
img_translation = cv2.warpAffine(img, translation_matrix, (num_cols, num_rows))

cv2.imshow('Translation', img_translation)
cv2.waitKey()