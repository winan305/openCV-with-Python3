# p98~99: SURF 키포인트 추출
# cv2.SURF -> cv2.xfeatures2d.SURF_create() 로 바뀜.

import cv2

img = cv2.imread("./img/city.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

surf = cv2.xfeatures2d.SURF_create()
kp = surf.detect(gray,None)

img = cv2.drawKeypoints(img, kp, None)

cv2.imshow("SURF Features", img)
cv2.waitKey()