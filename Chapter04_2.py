# p73~73 : 눈 탐지
# 이후의 것들은 xml 파일을 구하지 못함.
# 다른 탐지들도 코드가 대부분 비슷하다.

import cv2

face_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('./haarcascades/haarcascade_eye.xml')

if face_cascade.empty():
    raise IOError("Unable to load the face cascade classifier xml file.")

if eye_cascade.empty():
    raise IOError("Unable to load the eye cascade classifier xml file.")

cap = cv2.VideoCapture(0)
scaling_factor = 0.5

while True :
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    for (x, y, w, h) in faces:
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]
        eyes = eye_cascade.detectMultiScale(roi_gray)
        for (x_eye, y_eye, w_eye, h_eye) in eyes:
            center = (int(x_eye + 0.5*w_eye), int(y_eye + 0.5*h_eye))
            r = int(0.3 * (w_eye + h_eye))
            color = (0, 255, 0)
            thickness = 3
            cv2.circle(roi_color, center, r, color, thickness)
    cv2.imshow("Eye Detector", frame)

    c = cv2.waitKey(1)
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()