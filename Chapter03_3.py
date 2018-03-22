# p53 : 마우스 입력

import cv2
import numpy as np

def detect_quadrant(event, x, y, flags, param) :
    if event == cv2.EVENT_LBUTTONDOWN :
        print(x, y)
        if x > width/2 :
            if y > height/2 :
                point_top_left = (int(width/2), int(height/2))
                point_bottom_right = (width-1, height-1)

            else :
                point_top_left = (int(width/2), 0)
                point_bottom_right = (width-1, int(height/2))
        else :
            if y > height / 2:
                point_top_left = (0, int(height / 2))
                point_bottom_right = (int(width/2), height - 1)

            else:
                point_top_left = (0, 0)
                point_bottom_right = (int(width/2), int(height / 2))

        cv2.rectangle(img, (0,0), (width-1, height-1), (255,255,255), -1)
        cv2.rectangle(img, point_top_left, point_bottom_right, (0,100,0),-1)

if __name__ == '__main__' :
    width, height = 640, 480
    img = 255 * np.ones((122, 121, 3), dtype=np.uint8)
    cv2.namedWindow('Input window')
    cv2.setMouseCallback('Input window', detect_quadrant)

    while True :
        cv2.imshow('Input window', img)
        c = cv2.waitKey(10)
        if c == 27 : break

cv2.destroyAllWindows()

# openCV에서 제공하는 이벤트들을 모두 보기 위함. EVENT 로 시작하는 것들을 리스트에 담고 출력한다.
#print ([x for x in dir(cv2) if x.startswith('EVENT')])