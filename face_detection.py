import cv2

face_cascade = cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")
img = cv2.imread("Resources/large-group-of-people-white-background.jpg")
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(img_gray, 1.3, 4)

for (x,y,w,h) in faces:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0, 255, 0), 4)

cv2.imshow("Result", img)
cv2.waitKey(0)