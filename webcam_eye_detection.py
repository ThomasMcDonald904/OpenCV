import cv2
import numpy as np
from stack_function import stack_images

frameWidth = 640
frameHeight = 480

face_cascade = cv2.CascadeClassifier("Resources/haarcascade_eye.xml")

video = cv2.VideoCapture(0)

video.set(10,1000)

while True:
    succes, img = video.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img_gray, 1.1, 4)

    for  (x,y,w,h) in faces:
        cv2.circle(img, (x,y), int((h/2)), (0,255,0), cv2.FILLED)
    try:
        cv2.resize(img, (frameWidth, frameHeight))
        cv2.resize(img_gray, (frameWidth, frameHeight))
    except:
        exit()

    stack = stack_images(0.5, ([img, img_gray]))
    cv2.imshow("Face Detection", stack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break