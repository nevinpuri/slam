import numpy as np
import cv2 as cv
import OpenGL.GL as gl
import pypangolin as pn
from display import Display

vid = cv.VideoCapture("0.hevc")
if vid.isOpened() == False:
    print("Error opening 0")

display = Display()
display.start()
orb = cv.ORB_create(nfeatures=250, scaleFactor=1.2)
while True:
    status, frame = vid.read()
    if status == False:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    kp = orb.detect(gray, None)
    kp, description = orb.compute(gray, kp)
    print(description[0])

    img2 = cv.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv.imshow("frame", img2)
    key = cv.waitKey()

    if key == 113:
        display.stop()
        quit()


