import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_frontalface_default.xml')
# mouth_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_mcs_mouth.xml')
# eye_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_eye.xml')

video = cv2.VideoCapture("../images/IFMA Campus Caxias.mp4")

if not video.isOpened():
    print("Erro ao acessar video")
else:   
    while video.isOpened():
        ret, img = video.read()
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        faces = face_cascade.detectMultiScale(gray, 1.1,10)
        for (x,y,w,h) in faces:
            cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = img[y:y+h, x:x+w]

        cv2.imshow('img',img)

        if ret is True:

            key = cv2.waitKey(1)
            if(key == 27):
                break

        else: break

video.release()
cv2.destroyAllWindows()