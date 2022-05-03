import numpy as np
import cv2 as cv
import OpenGL.GL as gl
import pypangolin as pn
from display import Display
from multiprocessing import freeze_support

f = 910 # pixels

w = 1164
h = 874


# get focal length in mm
fx = f / w
fy = f / h

i_cam = [[fx, 0, 0],
        [0, fy, 0],
        [0, 0, 1]]

if __name__ == "__main__":
    print(i_cam)
    # display = Display()
    freeze_support()
    orb = cv.ORB_create(nfeatures=2000, scaleFactor=1.2)

    index_params = dict(algorithm=1, trees=5)
    search_params = dict(checks=50)
    flann = cv.FlannBasedMatcher(index_params, search_params)


    vid = cv.VideoCapture("2.hevc")
    if vid.isOpened() == False:
        print("Error opening")

    prev_frame = None

    i = 0

    while True:
        status, cur_frame = vid.read()
        if status == False:
            break

        i += 1

        good = []

        gray = cv.cvtColor(cur_frame, cv.COLOR_BGR2GRAY)

        if i <= 1:
            prev_frame = gray
            print("continued")
            continue # because prev frame doesn't exist

        kp_prev, des_prev = orb.detectAndCompute(prev_frame, None)
        kp_current, des_current = orb.detectAndCompute(gray, None)

        # print(kp_current[0].angle)

        if des_prev.size == 0 or des_current.size == 0:
            print("error: empty descriptions. skipping")
            continue

        # use float32 because the matcher expects float32, but matches are uint8
        matches = flann.knnMatch(np.float32(des_prev), np.float32(des_current), k=2)

        for m, n in matches:
            if m.distance < 0.7 * n.distance:
                # good = np.append(good, [m])
                good.append(m)

        old_frame_planar = []
        new_frame_planar = []

        for m in good:
            prev_idx = m.queryIdx
            cur_idx = m.trainIdx
            (x1, y1) = kp_prev[prev_idx].pt
            (x2, y2) = kp_current[cur_idx].pt
            old_frame_planar.append((x1, y1))
            new_frame_planar.append((x2, y2))
            # print(f"{x1} - {y1} = {x2} - {y2}")
        # prev_idx = good[0].queryIdx
        # cur_idx = good[0].trainIdx
        # print(f"{prev_idx} - {cur_idx}")
        # (x1, y1) = kp_prev[prev_idx].pt
        # (x2, y2) = kp_current[cur_idx].pt
        # print(f"{x1} - {y1} = {x2} - {y2}")
        # print(np.array(old_frame_planar))
        old_frame_planar = np.array(old_frame_planar)
        new_frame_planar = np.array(new_frame_planar)

        h = cv.findHomography(old_frame_planar, new_frame_planar, cv.RANSAC)
        # print(h)

        # find intrinsic params as well

        f, mask = cv.findFundamentalMat(old_frame_planar, new_frame_planar, cv.FM_LMEDS)

        h = np.array(h[0])
        f = np.array(f)

        rh = np.sum(h) / (np.sum(h) + np.sum(f))

        chosen = None
        if rh > 0.45:
            chosen = h
        else:
            chosen = f

        print(chosen)

        # img3 = cv.drawKeypoints(cur_frame, kp_current, None, color=(0, 255, 0))
        img3 = cv.drawMatchesKnn(prev_frame, kp_prev, gray, kp_current, matches[:10], None, (0, 255, 0))
        # cv.imshow('frame', img3)

        # prev_frame = gray
        # continue down here

        key = cv.waitKey()

        prev_frame = gray

        if key == 113:
            quit()
