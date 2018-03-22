# p.9~12 : 영상 컬러 공간 사이의 변환, RGB, YUV, HSV

import cv2

img = cv2.imread('./img/input.jpg')
# BGR -> YUV
'''yuv_img = cv2.cvtColor(img, cv2.COLOR_BGR2YUV) # BGR -> YUV 로 변환.
print(img.shape)
# 가로 x 세로 x 채널수
cv2.imshow('Y Channel', yuv_img[:,:,0]) # Y 채널
cv2.imshow('U Channel', yuv_img[:,:,1]) # U 채널
cv2.imshow('V Channel', yuv_img[:,:,2]) # V 채널
cv2.waitKey()'''

# BGR -> HSV
hsv_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) # BGR -> HSV 로 변환.
print(img.shape)
# 가로 x 세로 x 채널수
cv2.imshow('H Channel', hsv_img[:,:,0]) # H 채널
cv2.imshow('S Channel', hsv_img[:,:,1]) # S 채널
cv2.imshow('V Channel', hsv_img[:,:,2]) # V 채널
cv2.waitKey()
