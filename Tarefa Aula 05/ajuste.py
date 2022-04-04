import cv2
import numpy as np
from matplotlib import pyplot as plt

imagem = cv2.imread('../images/logo-if.jpg')

def ajuste_brilho(img, br):
    brilho = [br, br, br]
    res = np.zeros(img.shape, np.uint8)
    for y in range(0, img.shape[0]):
        for x in range(0, img.shape[1]):
            res[y, x] = np.minimum(brilho + img[y, x], [255, 255, 255])
    return res

def ajuste_contraste(img, cont):
    contraste = [cont, cont, cont]
    res = np.zeros(img.shape, np.uint8)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
                res[i,j] = np.minimum(contraste * img[i,j], [255, 255, 255])
    return res

def ajuste_negativo(img, negative):
    negativo = [negative, negative, negative]
    res = np.zeros(img.shape, np.uint8)
    for i in range(0, img.shape[0]):
        for j in range(0, img.shape[1]):
                res[i,j] = np.minimum(negativo - img[i,j], [255, 255, 255])
    return res
    
cv2.namedWindow('MOD')
brilho = 0
contraste = 1
negativo = 255
result = imagem

while(True):
    cv2.imshow('MOD', result)
    key = cv2.waitKey(20)
    if key == 27:
        break
    elif key == ord('a'):
        brilho = min(brilho + 50, 255)
        result = ajuste_brilho(imagem, brilho)
    elif key == ord('z'):
        brilho = max(brilho - 50, 0)
        result = ajuste_brilho(imagem, brilho)
    elif key == ord('s'):
        contraste = min(contraste + 0.20, 255)
        if(contraste > 1):
            result = ajuste_contraste(imagem, contraste)
    elif key == ord('x'):
        contraste = max(contraste - 0.20, 0)
        if(contraste > 0 and contraste < 1):
            result = ajuste_contraste(imagem, contraste)
    elif key == ord('n'):
        negativo = max(negativo, 0)
        result = ajuste_negativo(imagem, negativo)

cv2.destroyAllWindows()