import cv2

img = cv2.imread("profile.jpg")

cv2.namedWindow("redEliminacao")
while True:
    cv2.imshow("redEliminacao", img)

    key = cv2.waitKey(20)
    if key == 27:
        break

cv2.destroyAllWindows
