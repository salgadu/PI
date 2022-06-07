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

btnA = False
btnC = False
kernel = np.ones((3, 3), np.uint)

def logo (image):
    top, right, bottom, left = 35, 1220, 153, 1135 
    
    res = np.zeros(image.shape, np.uint8)
    interesse = image [top:bottom, left:right]
    gray = cv2.cvtColor(interesse, cv2.COLOR_BGR2GRAY)
    _, mask_inv = cv2.threshold(gray, 180, 255, cv2.THRESH_BINARY)
    trans = cv2.morphologyEx(mask_inv, cv2.MORPH_CLOSE, kernel)
    trans = cv2.GaussianBlur(trans, (5, 5), 0)
    background = cv2.bitwise_and(interesse, interesse, mask = trans)
    res [top:bottom, left:right] = background
    gray = cv2.cvtColor(res, cv2.COLOR_BGR2GRAY)
    repo = cv2.inpaint(image, gray, 3, cv2.INPAINT_NS)
    cv2.imshow("Logo", repo)

def aspect(image):
    resize = cv2.resize(image, (960, 720), interpolation = cv2.INTER_LINEAR)  
    return resize  
    
def crop(image):
    top, right, bottom, left = 0, 1120, 720, 160 
    crop = image[top:bottom, left:right]
    return crop

if not video.isOpened():
    print("Erro ao acessar video")
else:   
    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            logo(frame)
            key = cv2.waitKey(10)

            if(key == ord('a')):
                btnA = not btnA
            if(btnA):
                frame = aspect(frame)
            
            if(key == ord('c')):
                btnC = not btnC
            if(btnC):
                frame = crop(frame)

            cv2.imshow("Original", frame)
            
            if(key == 27):
                break

        else: break

video.release()
cv2.destroyAllWindows()