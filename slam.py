import cv2 as cv
import numpy as np


if __name__ == "__main__":
    cap = cv.VideoCapture("0.hevc")
    orb = cv.ORB_create()

    FLANN_INDEX_LSH = 6
    index_params = dict(algorithm = FLANN_INDEX_LSH,
            table_number = 6,
            key_size = 12,
            multi_probe_level = 1)

    search_params = dict(checks=50)

    flann = cv.FlannBasedMatcher(index_params, search_params)


    prev_frame = None
    while True:
        ret, frame = cap.read()

        if ret != True:
            break

        if prev_frame is None:
            prev_frame = frame
            continue

        wp = int(frame.shape[1] // 2)
        hp = int(frame.shape[0] // 2)

        i_params = [
            [910, 0, wp],
            [0, 910, hp],
            [0, 0, 1]
        ]

        print(frame.shape)

        kp1, des1 = orb.detectAndCompute(prev_frame, None)
        kp2, des2 = orb.detectAndCompute(frame, None)

        matches = flann.knnMatch(des1, des2, k=2)

        # print(matches)

        matchesMask = [[0,0] for i in range(len(matches))]

        for i, k in enumerate(matches):
            if len(k) < 2:
                continue

            if k[0].distance < 0.7 * k[1].distance:
                matchesMask[i] = [1,0]


        draw_params = dict(matchColor = (0, 255, 0),
                singlePointColor = (255, 0, 0),
                matchesMask = matchesMask,
                flags = cv.DrawMatchesFlags_DEFAULT)

        # frame = cv.drawKeypoints(frame, kp2, None, color=(0, 255, 0), flags=0)
        matches_frame = cv.drawMatchesKnn(prev_frame, kp1, frame, kp2, matches, None, **draw_params)

        cv.imshow("frame", matches_frame)
        prev_frame = frame

        key = cv.waitKey()

        if key == 113:
            break

cap.release()
cv.destroyAllWindows()
