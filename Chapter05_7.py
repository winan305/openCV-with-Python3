# p103~104 : ORB
# 빠르고 강하고 오픈소스임.
# SIFT, SURF 는 특허 등록이 되어 있어 상업적 사용이 불가능하다.
# cv2.ORB() -> cv2.ORB_create()

import cv2

img = cv2.imread("./img/city.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()

kp = orb.detect(gray, None)
kp, des = orb.compute(gray, kp)
final_kp = cv2.drawKeypoints(img, kp, None, (0,255,0), 0)

cv2.imshow("ORB", final_kp)
cv2.waitKey()