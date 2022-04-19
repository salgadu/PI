# import cv2
# import numpy as np

# rodando = 0
# pontoA, pontoB = 0, 0

# img = cv2.imread('../images/logo-if.jpg')

# rows, cols = img.shape[:2]

# def ponto(event, x, y, flags, param):
#     global pontoA, pontoB
#     if event == cv2.EVENT_LBUTTONDOWN:
#         pontoA, pontoB = x, y
        
# def rotacao():
#     global rodando
#     rodando = rodando + 1

# cv2.namedWindow('res')
# cv2.setMouseCallback('res', ponto)

# while(True):
#     res = cv2.getRotationMatrix2D((pontoA, pontoB), rodando, 1)
#     resultado = cv2.warpAffine(img, res, (cols, rows))

#     cv2.imshow('res', resultado)

#     key = cv2.waitKey(20)
#     if key == 27:
#         break
#     elif key == ord('r'):
#        rotacao()

# cv2.waitKey(0)
# cv2.destroyAllWindows()