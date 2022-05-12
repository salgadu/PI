import cv2

back = cv2.imread('../images/ifma-caxias.jpg')
fore = cv2.imread('../images/logo-if.jpg')

fore = cv2.resize(fore, (200,100), interpolation=cv2.INTER_AREA)

rows, cols, channels = fore.shape
interesse = back[0:rows, 0:cols]
fore_gray = cv2.cvtColor(fore, cv2.COLOR_BGR2GRAY)
ret, mask_inv = cv2.threshold(fore_gray, 125, 255, cv2.THRESH_BINARY)
mask = cv2.bitwise_not(mask_inv)
background = cv2.bitwise_and(interesse, interesse, mask = mask_inv)
foreground = cv2.bitwise_and(fore, fore, mask = mask)
output = cv2.add(background, foreground)
back [0:rows, 0:cols ] = output

telea = cv2.inpaint(output, mask, 3, cv2.INPAINT_TELEA)
ns = cv2.inpaint(output, mask, 3, cv2.INPAINT_NS)
back[0:rows, 0:cols ] = telea
cv2.imshow('TELEA', telea)
cv2.imshow('resTELEA', back)
back[0:rows, 0:cols ] = ns
cv2.imshow('NS', ns)
cv2.imshow('resNS', back)

cv2.waitKey(0)
cv2.destroyAllWindows()