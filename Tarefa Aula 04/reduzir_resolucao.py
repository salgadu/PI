import cv2
import numpy as np

img = cv2.imread('../images/logo-if.jpg')

cv2.imshow('Base', img)

(height, width) = img.shape[0:2]

low_width = int(width / 3)
low_height = int(height / 3)

img_eliminada = np.zeros((low_height, low_width, 3), np.uint8)
img_media = np.zeros(img.shape, np.uint8)

def matriz_eliminada(m):
    return m[1, 1]

def matriz_media(matrix):
    return cv2.mean(matrix)[:3]

# Redução da resolução de uma imagem tomando por base a eliminação dos pixels da vizinhança-8.
for y in range(low_width):
    auxY = y * 3
    for x in range(low_height):
        auxX = x * 3 
        matrix = img[auxX: auxX + 3, auxY: auxY + 3]
        img_eliminada[x, y] = matriz_eliminada(matrix)

# Redução da resolução de uma imagem tomando por base a média dos pixels na vizinhança-8.
for y in range(width):
    for x in range(height):
        matriz = img[x - 1: x + 2, y - 1: y + 2]
        img_media[x, y] = matriz_media(matriz)

cv2.imshow('Eliminada', img_eliminada)
cv2.imshow('Media', img_media)
 
cv2.waitKey(0)
cv2.destroyAllWindows()