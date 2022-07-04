import cv2

face_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_frontalface_default.xml')
profile_cascade = cv2.CascadeClassifier('../classificadores/haarcascade_profileface.xml')

video = cv2.VideoCapture("../images/IFMA Campus Caxias.mp4")
contfaces = 0

if not video.isOpened():
    print("Erro ao acessar video")
else:   
    while video.isOpened():
        ret, frame = video.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        faces = face_cascade.detectMultiScale(gray)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            
        perfil = profile_cascade.detectMultiScale(gray)
        for (x, y, w, h) in perfil:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]

        if (len(faces) and len(perfil) > 0):
            contfaces += 1

        text = "{} pessoas".format(contfaces)
        cv2.putText(frame, text, (10, 20), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 255), 2)

        cv2.imshow('img',frame)
    
        if ret is True:

            key = cv2.waitKey(1)
            if(key == 27):
                break

        else: break

video.release()
cv2.destroyAllWindows()