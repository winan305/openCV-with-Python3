# p33~35 : 에지 탐지
# 에지탐지는 영상에서 날카로운 에지를 탐색하고 결과로서 이진 영상을 생성한다.
# 에지를 나타내기 위해 검은 바탕에 흰색 라인을 그림.

import cv2

img = cv2.imread('img/input.jpg', cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape

# 수평, 수직 엣지를 위한 Sobel 에지 필터로 이미지 생성
sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=5)

cv2.imshow('Original', img)
cv2.imshow('Sobel horizontal', sobel_horizontal)
cv2.imshow('Sobel vertical', sobel_vertical)

# Sobel 필터는 모든 에지의 결과를 보여주지 않기 때문에 라플라시안 필터 사용.
laplacian = cv2.Laplacian(img, cv2.CV_64F)
cv2.imshow('Laplacian Filter', laplacian)

# 라플라시안 커널은 잡음을 발생시키기 때문에 캐니 에지 탐지가 필요함.
canny = cv2.Canny(img, 50, 240)
cv2.imshow('Canny', canny)

cv2.waitKey()