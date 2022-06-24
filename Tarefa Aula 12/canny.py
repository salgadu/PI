import cv2
import numpy as np

video = cv2.VideoCapture("../images/IFMA Campus Caxias(logo).mp4")

if not video.isOpened():
    print("Erro ao acessar video")
else:   
    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            canny = cv2.Canny(frame, 100, 200)
            cv2.imshow("Original", canny)

            key = cv2.waitKey(10)
            if(key == 27):
                break

        else: break

video.release()
cv2.destroyAllWindows()