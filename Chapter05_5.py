# p99~101 : FAST
# SURF, SIFT 는 실시간 시스템에서 사용하기에 느림.
# cv2.FastFeatureDetector() -> cv2.FastFeatureDetector_create()
import cv2
import numpy as np

gray = cv2.imread("./img/city.jpg", cv2.COLOR_BGR2GRAY)
fast = cv2.FastFeatureDetector_create()

kp = fast.detect(gray, None)
print("kp :", len(kp))

img_kp = cv2.drawKeypoints(gray, kp, outImage=None, color=(0,255,0))
cv2.imshow("Fast KP", img_kp)

cv2.waitKey()