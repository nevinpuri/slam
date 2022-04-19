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
    vid = cv.VideoCapture("0.hevc")
    if vid.isOpened() == False:
        print("Error opening 0")

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

