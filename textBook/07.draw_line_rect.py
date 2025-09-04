import numpy as np
import cv2

blue, green, red = (255,0,0), (0,255,0), (0,0,255)
image = np.zeros((400,600,3), np.uint8)
image[:] = (255,255,255)

pt1, pt2 = (50,50), (250, 150)
pt3, pt4 = (400,150), (500,50)
roi = (50,200,200,100)

cv2.line(image, pt1, pt2, red)
cv2.line(image, pt3, pt4, green, 3, cv2.LINE_AA)

cv2.rectangle(image, pt1, pt2, blue, 3, cv2.LINE_4)
cv2.rectangle(image, roi, red, 3, cv2.LINE_8)
cv2.rectangle(image, (400,200,100,100), green, cv2.FILLED)

cv2.imshow("Line & Rectangle", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#roi 특정 무언가가 실행되는 공간
#roi = (x좌표, y좌표, 너비, 높이)

#LINE_AA는 안티-에일리어싱
#LINE_4는 4방향(상하좌우)를 고려하여 연결하는 알고리즘
#LINE_8는 8방향(상하좌우, 북동,북서,남동,남서)를 고려하여 연결