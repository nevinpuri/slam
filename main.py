import numpy as np
import cv2 as cv
import OpenGL.GL as gl
import pypangolin as pn

vid = cv.VideoCapture("0.hevc")
pn.CreateWindowAndBind('Main', 640, 480)
gl.glEnable(gl.GL_DEPTH_TEST)

scam = pn.OpenGlRenderState(
        pn.ProjectionMatrix(640, 480, 420, 420, 320, 240, 0.2, 100),
        pn.ModelViewLookAt(-2, 2, -2, 0, 0, 0, pn.AxisDirection.AxisY))

handler = pn.Handler3D(scam)

dcam = pn.CreateDisplay()
print(dir(dcam))
dcam.SetBounds(0.0, 1.0, 0.0, 1.0, -640.0/480.0)
dcam.SetBounds(handler)

if vid.isOpened() == False:
    print("Error opening 0")

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

    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glClearColor(1.0, 1.0, 1.0, 1.0)
    dcam.Activate(scam)

    pangolin.glDrawColouredCube()

    points = np.random.random((100000, 3)) * 10
    gl.glPointSize(2)
    gl.glColor3f(1.0, 0.0, 0.0)
    pangolin.DrawPoints(points)

    pangolin.FinishFrame()

    cv.imshow("frame", img2)
    key = cv.waitKey()

    if key == 113:
        quit()


