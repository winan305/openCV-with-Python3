# p.5~9 : 영상 읽기, 디스플레이, 저장하기

import cv2

# img = cv2.imread('./img/input.jpg')
img = cv2.imread('./img/input.jpg', cv2.IMREAD_GRAYSCALE) # 그레이 스케일 영상
# img 의 타입은 numpy.ndarray

cv2.imshow('openCV Chapter01_1', img) # img를 화면에 띄움
cv2.imwrite('img/gray_img.jpg', img) # img를 img 폴더에 gray_img.jpg로 저장
cv2.waitKey()
# waitKey는 키보드 바인딩을 위해 사용됨
# 인수로 숫자를 취함, 수는 ms 단위. 키보드 이벤트 만나기 전 까지 기다리도록 한다.
# 0이나 아무것도 전달되지 않으면 키보드 이벤트를 무한정 기다림.
