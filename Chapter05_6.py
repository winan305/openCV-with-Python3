# p101~102 : BRIEF
# FAST를 사용해도 SIFT, SURF 를 사용함.
# BRIEF는 간결하고 빠르다.
# cv2.DescriptorExtractor_create("BRIEF") -> cv2.xfeatures2d.BriefDescriptorExtractor_create()
import cv2
import numpy as np

gray = cv2.imread("./img/city.jpg", cv2.COLOR_BGR2GRAY)

fast = cv2.FastFeatureDetector_create()
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

kp = fast.detect(gray, None)

kps = brief.compute(gray, kp)

gray_keypoints = cv2.drawKeypoints(gray, kp, None, color=(0,255,0))

cv2.imshow("BRIEF", gray_keypoints)
cv2.waitKey()