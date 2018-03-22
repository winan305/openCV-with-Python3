# p15~16 : 영상 회전

import cv2

img = cv2.imread('img/input.jpg')
# 이미지의 가로, 세로 저장
num_rows, num_cols = img.shape[:2]

# 변환행렬 생성
rotation_matrix = cv2.getRotationMatrix2D((num_cols/2, num_rows/2), 30, 1)

# 변환 이미지 생성
img_rotation = cv2.warpAffine(img, rotation_matrix, (num_cols, num_rows))

cv2.imshow('Translation', img_rotation)
cv2.waitKey()