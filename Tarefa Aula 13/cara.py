import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_frontalface_default.xml')
mouth_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_mcs_mouth.xml')
eye_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_eye.xml')

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
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1,10)
            for (ex,ey,ew,eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            mouth = mouth_cascade.detectMultiScale(roi_gray, 2.0, 20)
            for (mx,my,mw,mh) in mouth:
                cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)
                ret, frame = video.read()

        cv2.imshow('img',img)

        if ret is True:

            key = cv2.waitKey(1)
            if(key == 27):
                break

        else: break

video.release()
cv2.destroyAllWindows()