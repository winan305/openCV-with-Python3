# p97 : SIFT 키포인트 추출
# cv2.SIFT() -> cv2.xfeatures2d.SIFT_create() 로 바뀜.

import cv2

img = cv2.imread("./img/city.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sift = cv2.xfeatures2d.SIFT_create()
kp = sift.detect(gray,None)

img = cv2.drawKeypoints(img, kp, img)

cv2.imshow("SIFT Features", img)
cv2.waitKey()