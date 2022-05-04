import cv2
import numpy as np
import random

video = cv2.VideoCapture("../images/IFMA Campus Caxias.mp4")

def salpimenta(image, prob):
    output = image.copy()
    if len(image.shape) == 2:
        preto = 0
        branco = 255            
    else:
        colorido = image.shape[2]
        if colorido == 3:
            preto = np.array([0, 0, 0], np.uint8)
            branco = np.array([255, 255, 255], np.uint8)
        else:  
            preto = np.array([0, 0, 0, 255], np.uint8)
            branco = np.array([255, 255, 255, 255], np.uint8)
            
    probs = np.random.random(output.shape[:2])
    output[probs < (prob / 2)] = preto
    output[probs > 1 - (prob / 2)] = branco
    return output

def aumentar():
    global probabilidade
    probabilidade += 0.01

def diminuir():
    global probabilidade
    probabilidade -= 0.01

probabilidade = 0.005

if not video.isOpened():
    print("Erro ao acessar video")
else:   
    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            cv2.imshow("SP", salpimenta(frame,  probabilidade))

            key = cv2.waitKey(10)
            if key == 27:
                break
            elif key == ord("w"): #W
                aumentar()
            elif key == ord("s"):
                diminuir()
        else: break

video.release()
cv2.destroyAllWindows()