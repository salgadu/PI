import cv2
import numpy as np

video = cv2.VideoCapture("../images/IFMA Campus Caxias(logo).mp4")
# image = cv2.imread('../images/logo-if-vertical.png')

# porcentagem = 20 
# width = int(image.shape[1] * porcentagem / 100)
# height = int(image.shape[0] * porcentagem / 100)
# dim = (width, height)
# image = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

# print('Resized Dimensions : ', image.shape)

# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# ret, mask_inv = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
# mask = cv2.bitwise_not(mask_inv)

top, right, bottom, left = 0, 960, 720, 0 

def logo (image):
    res = np.zeros(image.shape, np.uint8)
    interesse = image [25:165, 1130:1225]
    gray = cv2.cvtColor(interesse, cv2.COLOR_BGR2GRAY)
    _, mask_inv = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
    background = cv2.bitwise_and(interesse, interesse, mask = mask_inv)
    res [25:165, 1130:1225] = background
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    repo = cv2.inpaint(image, gray, 3, cv2.INPAINT_NS)
    cv2.imshow("Logo", repo)

def aspect(image):
    resize = cv2.resize(image, (960, 720), interpolation = cv2.INTER_LINEAR)    
    cv2.imshow("aspect", resize)

def crop(image):
    crop = image[top:bottom, left:right, :]
    cv2.imshow("crop", crop)

if not video.isOpened():
    print("Erro ao acessar video")
else:   
    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            cv2.imshow("Original", frame)
            logo(frame)
            key = cv2.waitKey(10)
            if key == 27:
                break
            elif key == ord("a"):
                # cv2.imshow("aspect", aspect(frame))
                aspect(frame)
            elif key == ord("c"):
                # cv2.imshow("crop", crop(frame))
                crop(frame)
            
        else: break

video.release()
cv2.destroyAllWindows()