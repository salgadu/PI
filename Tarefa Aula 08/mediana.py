import cv2
import numpy as np

tam = 7
image = cv2.imread('../images/noise.jpg')
mediana = cv2.medianBlur(image, tam)

cv2.imshow('Imagem Noise', image)
cv2.imshow('Imagem Boa M', mediana)

cv2.waitKey(0)
cv2.destroyAllWindows()