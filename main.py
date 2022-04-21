import numpy as np
import cv2 as cv
import OpenGL.GL as gl
import pypangolin as pn
from multiprocessing import freeze_support

if __name__ == "__main__":
    freeze_support()
    orb = cv.ORB_create(nfeatures=250, scaleFactor=1.2)

    vid = cv.VideoCapture("0.hevc")
    if vid.isOpened() == False:
        print("Error opening")

    while True:
        status, cur_frame = vid.read()
        if status == False:
            break

        grey = cv.cvtColor(cur_frame, cv.COLOR_BGR2GRAY)
        kp_current, des_current = orb.detectAndCompute(grey, None)

        img3 = cv.drawKeypoints(cur_frame, kp_current, None, color=(0, 255, 0))
        cv.imshow('frame', img3)
        
        key = cv.waitKey()

        if key == 113:
            quit()
