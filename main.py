import numpy as np
import cv2 as cv
import OpenGL.GL as gl
import pypangolin as pn
from multiprocessing import freeze_support

if __name__ == "__main__":
    freeze_support()
    orb = cv.ORB_create(nfeatures=250, scaleFactor=1.2)

    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)


    vid = cv.VideoCapture("0.hevc")
    if vid.isOpened() == False:
        print("Error opening")

    prev_frame = None

    i = 0

    while True:
        status, cur_frame = vid.read()
        if status == False:
            break

        i += 1
        if not i > 1:
            prev_frame = cur_frame
            print("continued")
            continue # because prev frame doesn't exist

        good = np.array([])

        gray = cv.cvtColor(cur_frame, cv.COLOR_BGR2GRAY)

        if not i % 100 == 0:
            continue

        prev_frame = gray

        kp_prev, des_prev = orb.detectAndCompute(prev_frame, None)
        kp_current, des_current = orb.detectAndCompute(gray, None)

        if des_prev.size == 0 or des_current.size == 0:
            print("error: empty descriptions. skipping")
            continue

        # use float32 because the matcher expects float32, but matches are uint8
        matches = flann.knnMatch(np.float32(des_prev), np.float32(des_current), k=2)

        for i, (m, n) in enumerate(matches):
            if m.distance < 0.7 * n.distance:
                good = np.append(good, [m])

        # print(good)

        # img3 = cv.drawKeypoints(cur_frame, kp_current, None, color=(0, 255, 0))
        img3 = cv.drawMatchesKnn(prev_frame, kp_prev, gray, kp_current, matches, None, (0, 255, 0))
        cv.imshow('frame', img3)

        
        key = cv.waitKey()

        if key == 113:
            quit()
