import cv2
import numpy as np

image = cv2.imread('../images/face.jpg')
oculos = cv2.imread('../images/sungalsses.png', cv2.IMREAD_UNCHANGED)
bigode = cv2.imread('../images/moustache.png', cv2.IMREAD_UNCHANGED)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_mcs_mouth.xml')

porcentagem = 50
def resize(image, porcentagem):
    width = int(image.shape[1] * porcentagem / 100)
    height = int(image.shape[0] * porcentagem / 100)
    dimensao = (width, height)
    image = cv2.resize(image, dimensao, interpolation=cv2.INTER_AREA)
    return image

oculos = resize(oculos, porcentagem)
bigode = resize(bigode, porcentagem)

def filtro(image, objeto, x, y, w, h):
    rows, cols = objeto.shape[:2]
    alpha = objeto[:, :, 3] / 255
    overlay = objeto[:, :, :3]
    mask = np.dstack((alpha, alpha, alpha))
    roi = image[(y-h):(y-h) + rows, (x-w):(x-w) + cols]
    output = roi * (1 - mask) + overlay * mask
    image[(y-h):(y-h) + rows, (x-w):(x-w) + cols] = output
    return image

faces = face_cascade.detectMultiScale(gray)
for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1, 10)
    for (ex, ey, ew, eh) in eyes:
        roi_color = filtro(roi_color, oculos, ex, ey, 14, -10)
        break
    mouth = mouth_cascade.detectMultiScale(roi_gray, 2.0, 20)
    for (mx, my, mw, mh) in mouth:
        roi_color = filtro(roi_color, bigode, mx, my, 15, 30)

cv2.imshow('Stories', image)

cv2.waitKey(0)
cv2.destroyAllWindows()