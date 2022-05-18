import cv2
import numpy as np

image = cv2.imread('../images/morphological_car.png')
kernel = np.ones((5,5),np.uint)

image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# output = cv2.morphologyEx(image, cv2.MORPH_TOPHAT, kernel)
output = cv2.morphologyEx(image, cv2.MORPH_BLACKHAT, kernel)

cv2.imshow('Imagem', image)
cv2.imshow('RES', output)

cv2.waitKey(0)
cv2.destroyAllWindows()