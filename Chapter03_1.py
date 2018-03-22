# p.50 : 웹캠 접근

import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened() :
    raise IOError("Can't open webcam")

while True :
    # ret은 bool형 변수. true가 되어야함.
    ret, frame = cap.read()

    # 책에는 없는 코드.
    if ret == True :
        frame = cv2.resize(frame, None, fx=0.5, fy = 0.5, interpolation=cv2.INTER_AREA)
        cv2.imshow('Web Cam', frame)
        c = cv2.waitKey(30)&0xFF
        if c == 27 :
            break

cap.release()
cv2.destroyAllWindows()
