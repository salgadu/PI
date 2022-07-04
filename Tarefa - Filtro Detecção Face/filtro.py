import cv2
import numpy as np

oculos = cv2.imread('../images/sungalsses.png', cv2.IMREAD_UNCHANGED)
bigode = cv2.imread('../images/moustache.png', cv2.IMREAD_UNCHANGED)

face_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_mcs_mouth.xml')

porcentagem = 50
def resize(image, width, height):
    width = int(width * porcentagem / 100)
    height = int(height * porcentagem / 100)
    dimensao = (width, height)
    image = cv2.resize(image, dimensao, interpolation=cv2.INTER_AREA)
    return image

# oculos = resize(oculos, porcentagem)
# bigode = resize(bigode, porcentagem)

def filtro(image, objeto, x, y, w, h):
    rows, cols = objeto.shape[:2]
    alpha = objeto[:, :, 3] / 255
    overlay = objeto[:, :, :3]
    mask = np.dstack((alpha, alpha, alpha))
    roi = image[(y-h):(y-h) + rows, (x-w):(x-w) + cols]
    output = roi * (1 - mask) + overlay * mask
    image[(y-h):(y-h) + rows, (x-w):(x-w) + cols] = output
    return image

face_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_profileface.xml')

video = cv2.VideoCapture("../images/IFMA Campus Caxias.mp4")

if not video.isOpened():
    print("Erro ao acessar video")
else:   
    while video.isOpened():
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 15)
            for (ex, ey, ew, eh) in eyes:
                cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
                roi_color = filtro(roi_color, resize(oculos, ew, eh), ex, ey, 14, -10)
                break
            mouth = mouth_cascade.detectMultiScale(roi_gray, 2.0, 20)
            for (mx, my, mw, mh) in mouth:
                cv2.rectangle(roi_color,(mx,my),(mx+mw,my+mh),(0,0,255),2)
                roi_color = filtro(roi_color, resize(bigode, mw, mh), mx, my, 15, 30)

        cv2.imshow('img',frame)
    
        if ret is True:

            key = cv2.waitKey(1)
            if(key == 27):
                break

        else: break

video.release()
cv2.destroyAllWindows()