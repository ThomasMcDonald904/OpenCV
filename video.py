import cv2

frameWidth = 640
frameHeight = 480
video = cv2.VideoCapture("Resources/coffee.mp4")

# video.set(10,1000)

while True:
    success, img = video.read()
    try:
        img = cv2.resize(img, (frameWidth, frameHeight))
    except:
        exit()
    cv2.imshow("Result", img)
    if cv2.waitKey(1) and 0xFF == ord('q'):
        break