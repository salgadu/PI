# coding=utf-8
import cv2
import numpy as np

image = cv2.imread('../images/coins.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

blur = cv2.medianBlur(image, 5)
blur = cv2.cvtColor(blur, cv2.COLOR_BGR2GRAY)

circles = cv2.HoughCircles(blur, cv2.HOUGH_GRADIENT, 1, 50, 
    param1 = 200, param2 = 50, minRadius = 0, maxRadius = 0)
circles = np.uint16(np.around(circles))

for circle in circles[0]:
    x, y, radius = circle
    moedas = cv2.circle(image, (int(x), int(y)), int(radius), (255, 0, 0), 4)
    
    xm = x - 60
    ym = y - 20

    if(radius == 85 ): 
        cv2.putText(image, "1 real", (xm, ym), cv2.FONT_HERSHEY_COMPLEX, 0.5, (0, 0, 0), 2)
    if(radius == 73 ): 
        cv2.putText(image, "50 centavos", (xm, ym), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(radius == 74 ):
        cv2.putText(image, "25 centavos", (xm, ym), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(radius == 60): 
        cv2.putText(image, "10 centavos", (xm, ym), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)
    if(radius == 67): 
        cv2.putText(image, "5 centavos", (xm, ym), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 0), 2)

cv2.imshow('Moedas', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
