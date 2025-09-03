import cv2
import numpy as np

# winget install --interactive --exact dorssel.usbipd-win << 웹캠 관련 다운로드
# usbipd list << 리스트 보기
# usbipd bind --busid 1-6 --force << 1-n n은 리스트보고 웹에 해당되는 주소 넣으면 됨
# usbipd attach --wsl --busid 1-6 << 리눅스에 웹캠 연결


def put_string(frame, text, pt, value, color=(120, 200, 90)):             # 문자열 출력 함수 - 그림자 효과
    text += str(value)
    shade = (pt[0] + 2, pt[1] + 2)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, text, shade, font, 0.7, (0, 0, 0), 2)  # 그림자 효과
    cv2.putText(frame, text, pt, font, 0.7, (120, 200, 90), 2)  # 글자 적기

def main():
    cap = cv2.VideoCapture("/home/aa/hongOpencv/data/vtest.avi") # 0으로 할시 웹캠 # 주소면 영상

    print(f"너비 {cap.get(cv2.CAP_PROP_FRAME_WIDTH)}")
    print(f"높이 {cap.get(cv2.CAP_PROP_FRAME_HEIGHT)}")
    print(f"FPS {cap.get(cv2.CAP_PROP_FPS)}")
    print(f"포맷 {cap.get(cv2.CAP_PROP_FORMAT)}")
    print(f"노출 {cap.get(cv2.CAP_PROP_EXPOSURE)}")
    print(f"밝기 {cap.get(cv2.CAP_PROP_BRIGHTNESS)}")
    
    if not cap.isOpened():
        print("웹캠을 열 수 없습니다.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("프레임을 읽지 못했습니다.")
            break
        cv2.imshow("Webcam", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()