import cv2
import numpy as np

image = cv2.imread("../images/cars.png")
borrado = cv2.GaussianBlur(image, (31, 31), 0)

mask = np.zeros(image.shape, np.uint8)
mask = cv2.circle(mask, (910, 250), 250, (255, 255,255), -1)

output = np.where(mask == np.array([255, 255, 255]), image, borrado)

cv2.imshow('Imagem Noise', image)
cv2.imshow('Imagem Boa M', output)

cv2.waitKey(0)
cv2.destroyAllWindows()