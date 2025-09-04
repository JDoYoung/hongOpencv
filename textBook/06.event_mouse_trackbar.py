import numpy as np
import cv2

def onChange(value):

    global image, title

    add_value = value - int(image[0][0])
    print("추가 화소값:", add_value)
    image[:] = image + add_value
    cv2.imshow(title, image)

def onMouse(event, x, y, flags, param):
    global image, bar_name

    if event == cv2.EVENT_RBUTTONDOWN:
        if (image[0][0] < 235): image[:] = image + 20
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

    elif event == cv2.EVENT_LBUTTONDOWN:
        if (image[0][0] >= 20):
            image[:] = image - 20
        cv2.setTrackbarPos(bar_name, title, image[0][0])
        cv2.imshow(title, image)

image = np.zeros((300,500), np.uint8)
title = "Trackbar & Mouse Event"
bar_name = 'Brightness'
cv2.imshow(title, image)

cv2.createTrackbar(bar_name, title, image[0][0], 255, onChange)
cv2.setMouseCallback(title, onMouse)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 235를 한 이유 - 0~255까지인데 지금 클릭당 20씩 증감하니 오버플로우 방지용
# image[0][0]은 그 좌표의 밝기값을 알아내는것인데
# 어차피 imgae[:]로 전체 값을 바꾸니 특정 위치 값의 밝기를 알아도 무관