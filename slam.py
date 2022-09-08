import cv2 as cv
import numpy as np

if __name__ == "__main__":
    cap = cv.VideoCapture("0.hevc")
    orb = cv.ORB_create()

    prev_frame = None
    while True:
        ret, frame = cap.read()

        if ret != True:
            break

        if prev_frame is None:
            prev_frame = frame
            continue

        kp1, des1 = orb.detectAndCompute(prev_frame, None)
        kp2, des2 = orb.detectAndCompute(frame, None)

        print(kp1)

        frame = cv.drawKeypoints(frame, kp2, None, color=(0, 255, 0), flags=0)

        cv.imshow("frame", frame)
        prev_frame = frame

        key = cv.waitKey()

        if key == 113:
            break

cap.release()
cv.destroyAllWindows()
