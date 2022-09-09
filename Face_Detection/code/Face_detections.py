import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv.VideoCapture(0)
while True:
    ret,img = cap.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray,
        scaleFactor=1.2,
        minNeighbors=5,
        minSize=(20, 20)
)
    for(x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(255,255,0),2)
    cv.imshow('sami',img)
    if cv.waitKey(30) & 0xFF == 27:
        break
cap.release()