import numpy as np
import cv2 as cv

class Img(object):
    def __init__(self):
        self.orb = cv.ORB_create(nfeatures=250, scaleFactor=1.2)
        q = mp.Queue()
        p = mp.Process(target=self.step, args=())
        p.start()

    def open(self, vid):
        self.vid = cv.VideoCapture(vid)
        return vid.isOpened()
    
    def step(self):
        status, frame = vid.read()
        if status == False:
            print("end")
            return

        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        kp = self.orb.detect(gray, None)
        kp, description = self.orb.compute(gray, kp)

        img2 = cv.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

        cv.imshow("frame", img2)
        key = cv.waitKey()

        if key == 113:
            quit()
