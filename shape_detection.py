import cv2
import numpy as np
from stack_function import stack_images

def getContours(img):
    contours, hierarchy = cv2.findContours(img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 500:
            cv2.drawContours(img_contour, contour, -1, (0,0,255), 3)
            peri = cv2.arcLength(contour, True)
            approx = cv2.approxPolyDP(contour, 0.02*peri, True)
            print(len(approx))


img = cv2.imread("Resources/shapes.png")
img_contour = img.copy()

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.GaussianBlur(img_gray, (7,7), 1)
img_canny = cv2.Canny(img_blur, 50, 50)
getContours(img_canny)

img_blank = np.zeros_like(img)
img_stacked = stack_images(0.6, ([img, img_gray, img_blur],
                                 [img_canny, img_contour, img_blank]))

cv2.imshow("Stack", img_stacked)

cv2.waitKey(0)