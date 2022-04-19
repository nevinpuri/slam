import numpy as np
import cv2 as cv

class Img(object):
    def __init__(self):
        self.orb = cv.ORB_create(nfeatures=250, scaleFactor=1.2)

    def run():
        vid = cv.VideoCapture("0.hvec")
        if vid.isOpened() == False:
            print("Error opening 0")

    while True:
        status, frame = vid.read()
        if status == False:
            return

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        kp = self.orb.detect(gray, None)
        kp, description = self.orb.compute(gray, kp)
        # print(description[0])

        img2 = cv.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv.imshow("frame", img2)
        key = cv.waitKey()

        if key == 113:
            display.stop()
            quit()
