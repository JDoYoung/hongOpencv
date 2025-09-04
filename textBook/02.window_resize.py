import numpy as np
import cv2
image = np.zeros((200,300), np.uint8)
image.fill(255)

title1, title2 = 'AUTOSIZE', 'NORMAL'
cv2.namedWindow(title1, cv2.WINDOW_AUTOSIZE) # 화면 확대 축소에 맞춰 image도 크기 변함
cv2.namedWindow(title2, cv2.WINDOW_NORMAL) # 확대 축소해도 image 크기 그대로

cv2.imshow(title1, image)
cv2.imshow(title2, image)
cv2.resizeWindow(title1, 400, 300)
cv2.resizeWindow(title2, 400, 300)
cv2.waitKey(0)
cv2.destroyAllWindows()