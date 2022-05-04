from random import randint
import cv2

BLUE = (255, 0, 0)
GREEN = (0, 255, 0)
RED = (0, 0, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)

COLORS=[BLUE,GREEN,RED,BLACK,GRAY]

drawing = False
circles = []
c = 0

def line_drawing(event,x,y,flags,param):
    global drawing

    if event==cv2.EVENT_LBUTTONDOWN:
        drawing=True
        circles.append((x, y))

    elif event==cv2.EVENT_MOUSEMOVE:
        if drawing==True:
            circles.append((x, y))

    elif event==cv2.EVENT_LBUTTONUP:
        drawing=False
        circles.append((x, y))

video = cv2.VideoCapture("../images/IFMA Campus Caxias.mp4")

frame_width = video.get(cv2.CAP_PROP_FRAME_WIDTH)
frame_height = video.get(cv2.CAP_PROP_FRAME_HEIGHT)
fps = video.get(cv2.CAP_PROP_FPS)

cv2.namedWindow("Frame")
cv2.setMouseCallback("Frame", line_drawing)

if not video.isOpened():
    print("Erro ao acessar video")
else:   
    fourcc = cv2.VideoWriter_fourcc('X', 'V', 'I', 'D')
    output = cv2.VideoWriter("video_desenhado.avi", fourcc, int(fps), (int(frame_width), int(frame_height)))

    while video.isOpened():
        ret, frame = video.read()
        if ret is True:
            for center_position in circles:
                cv2.line(frame, center_position, center_position,COLORS[c],5)

            output.write(frame)

            cv2.imshow("Frame", frame)

            key = cv2.waitKey(25)
            if key == 27:
                break
            elif key == ord(" "):
                circles = []
            elif key == ord("c"):
                c = randint(0, len(COLORS)-1)
        else: break

video.release()
output.release()
cv2.destroyAllWindows()