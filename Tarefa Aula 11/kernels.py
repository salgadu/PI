import cv2
import numpy as np

image = cv2.imread('../images/atividade_aula11.png')
image = cv2.resize(image, (400, 400), interpolation=cv2.INTER_AREA)

cv2.imshow('Imagem', image)

# Saida 01
kernel = np.ones((40, 40), np.uint)
fino_deslocado = cv2.erode(image, kernel, iterations = 1, anchor = (39, 39))
cv2.imshow('Image01', fino_deslocado)

# Saida 02
kernel = np.ones((120, 60), np.uint)
duas_linhas = cv2.erode(image, kernel, iterations = 1)
kernel = cv2.getStructuringElement(shape = cv2.MORPH_ELLIPSE, ksize = (40, 80))
duas_linhas = cv2.dilate(duas_linhas, kernel, iterations = 1)
cv2.imshow('Image02', duas_linhas)

# Saida 03
kernel = cv2.getStructuringElement(shape = cv2.MORPH_ELLIPSE, ksize = (40, 40))
grande = cv2.dilate(image, kernel, iterations = 2)
grande = cv2.erode(grande, kernel, iterations = 1)
cv2.imshow('Image03', grande)

cv2.waitKey(0)
cv2.destroyAllWindows()