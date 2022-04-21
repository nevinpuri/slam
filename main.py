import numpy as np
import cv2 as cv
import OpenGL.GL as gl
import pypangolin as pn
from display import Display
# from img import Img
import matplotlib.pyplot as plt
from multiprocessing import freeze_support
from matplotlib.widgets import Button

if __name__ == '__main__':
    freeze_support()
    orb = cv.ORB_create(nfeatures=250, scaleFactor=1.2)
    # bf = cv.BFMatcher(cv.NORM_HAMMING, crossCheck=True)
    FLANN_INDEX_KDTREE = 1
    index_params = dict(algorithm = FLANN_INDEX_KDTREE, trees = 5)
    search_params = dict(checks = 50)
    # flann = cv.DescriptorMatcher_create(cv.DescriptorMatcher_FLANNBASED)
    flann = cv.FlannBasedMatcher(index_params, search_params)

    vid = cv.VideoCapture("0.hevc")
    if vid.isOpened() == False:
        print("Error opening 0")

    while True:
        status, cur_frame = vid.read()
        if status == False:
            break

        cur_frame_gray = cv.cvtColor(cur_frame, cv.COLOR_BGR2GRAY)
        kp_current, des_current = orb.detectAndCompute(cur_frame_gray, None)
        # des_current = np.float32(des_current)

        status, next_frame = vid.read()
        if status == False:
            break

        next_frame_gray = cv.cvtColor(next_frame, cv.COLOR_BGR2GRAY)
        kp_next, des_next = orb.detectAndCompute(next_frame_gray, None)
        # des_next = np.float32(des_next)

        # print(des_current)
        matches = flann.knnMatch(np.float32(des_current), np.float32(des_next), k=2)
        # print(matches)
        matches_mask = [[0, 0] for i in range(len(matches))]

        good_matches = np.array([])

        for i, (m, n) in enumerate(matches):
            if m.distance < 0.7 * n.distance:
                matches_mask[i] = [1,0]
                good_matches = np.append(good_matches, [m])

                """
                idx1 = item_match.trainIdx
                idx2 = itemMatch.queryIdx
                """

        draw_params = dict(
                matchColor=(0, 255, 0),
                singlePointColor=(255, 0, 0),
                matchesMask=matches_mask,
                flags=cv.DrawMatchesFlags_DEFAULT
                )

        pre_matches = np.float32([kp_current[m.queryIdx].pt for m in good_matches])
        cur_matches = np.float32([kp_next[m.trainIdx].pt for m in good_matches])

        homography = cv.findHomography(pre_matches, cur_matches)
        print(homography)

        img3 = cv.drawMatchesKnn(cur_frame_gray, kp_current, next_frame_gray, kp_next, matches, None, (0, 255, 0), None, None, cv.DrawMatchesFlags_DEFAULT)

        cv.imshow('frame', img3)

        # img3 = cv.drawMatches(cur_frame, kp_current, next_frame, kp_next, matches, None, **draw_params)

        # cv.imshow("frame", img3)

        # img2 = cv.drawKeypoints(frame, kp, None, color=(0, 255, 0))

        # cv.imshow("frame", img2)
        key = cv.waitKey()
        if key == 113:
            quit()
display = Display()
print("ok")

"""
img = Img()
img.run()
"""


"""
pn.CreateWindowAndBind('Main', 640, 480)
gl.glEnable(gl.GL_DEPTH_TEST)
s_cam = pn.OpenGlRenderState(
        pn.ProjectionMatrix(640, 480, 420, 420, 320, 240, 0.1, 1000),
        pn.ModelViewLookAt(-0, 0.5, -3, 0, 0, 0, pn.AxisDirection.AxisY))

handler = pn.Handler3D(s_cam)
d_cam = (
        pn.CreateDisplay()
        .SetBounds(
            pn.Attach(0),
            pn.Attach(1),
            pn.Attach.Pix(180),
            pn.Attach(1),
            -640/480
            )
        .SetHandler(handler)
        )

pn.RegisterKeyPressCallback(-96 + ord('a'), my_callback)
pn.CreatePanel("ui").SetBounds(pn.Attach(0), pn.Attach(1.0), pn.Attach(0), pn.Attach.Pix(180))

while not pn.ShouldQuit():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glClearColor(0, 0, 0, 1)
    d_cam.Activate(s_cam)

    pn.glDrawColouredCube()

    pn.FinishFrame()
"""

# just do a callback before and then wait for key press or something

