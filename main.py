import numpy as np
import cv2 as cv
import OpenGL.GL as gl
import pypangolin as pn
from display import Display
import matplotlib.pyplot as plt
from matplotlib.widgets import Button

vid = cv.VideoCapture("0.hevc")
if vid.isOpened() == False:
    print("Error opening 0")

"""
display = Display()
display.start()
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

pn.CreatePanel("ui").SetBounds(pn.Attach(0), pn.Attach(1.0), pn.Attach(0), pn.Attach.Pix(180))

while not pn.ShouldQuit():
    gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
    gl.glClearColor(0, 0, 0, 1)
    d_cam.Activate(s_cam)

    pn.glDrawColouredCube()

    pn.FinishFrame()
"""

def next(event, text):
    print(text)
    pass

fig, = plt.figure(figsize=plt.figaspect(2.))

ax = fig.add_subplot(2, 1, 1)
ax.set_ylabel('ok')

ax = fig.add_subplot(2, 1, 2, projection='3d')

plt.show()

# just do a callback before and then wait for key press or something

orb = cv.ORB_create(nfeatures=250, scaleFactor=1.2)
while True:
    status, frame = vid.read()
    if status == False:
        break

    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

    kp = orb.detect(gray, None)
    kp, description = orb.compute(gray, kp)
    # print(description[0])

    img2 = cv.drawKeypoints(frame, kp, None, color=(0, 255, 0), flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    cv.imshow("frame", img2)
    key = cv.waitKey()

    if key == 113:
        display.stop()
        quit()


