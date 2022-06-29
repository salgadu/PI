import cv2

image = cv2.imread('../images/face.jpg')
oculos = cv2.imread('../images/sungalsses.png')
bigode = cv2.imread('../images/moustache.png')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

face_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_eye.xml')
mouth_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_mcs_mouth.xml')

porcentagem = 50
def resize(image, porcentagem):
    width = int(image.shape[1] * porcentagem / 100)
    height = int(image.shape[0] * porcentagem / 100)
    dim = (width, height)
    image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)
    return image

def filtro(image, objeto, x, y, w, h):
    rows, cows = objeto.shape[:2]
    roi_img = image[(y-h):(y-h) + rows, (x-w):(x-w) + cows] 
    roi_img [objeto < [150, 150, 150]] = objeto [objeto < [150, 150, 150]]    
    return image

faces = face_cascade.detectMultiScale(gray)
for (x, y, w, h) in faces:
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = image[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray, 1.1,10)
    for (ex, ey, ew, eh) in eyes:
        roi_color = filtro(roi_color, resize(oculos, porcentagem), ex, ey, 14, -10)
        break
    mouth = mouth_cascade.detectMultiScale(roi_gray, 2.0, 20)
    for (mx, my, mw, mh) in mouth:
        roi_color = filtro(roi_color, resize(bigode, porcentagem), mx, my, 15, 15)

cv2.imshow('Stories', image)
  
cv2.waitKey(0)
cv2.destroyAllWindows()