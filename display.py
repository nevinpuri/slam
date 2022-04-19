from threading import Thread, Event
import numpy as np
import OpenGL.GL as gl
import pypangolin as pn
import matplotlib.pyplot as plt

class Display(object):
    def __init__(self):
        pn.CreateWindowAndBind('Thread', 640, 480)

        gl.glEnable(gl.GL_DEPTH_TEST)

        self.scam = pn.OpenGlRenderState(
                pn.ProjectionMatrix(640, 480, 420, 420, 320, 240, 0.1, 1000),
                pn.ModelViewLookAt(-0, 0.5, -3, 0, 0, 0, pn.AxisDirection.AxisY))

        self.handler = pn.Handler3D(self.scam)
        self.dcam = (
                pn.CreateDisplay()
                .SetBounds(
                    pn.Attach(0),
                    pn.Attach(1),
                    pn.Attach.Pix(180),
                    pn.Attach(1),
                    -640/480,
                    )
                .SetHandler(self.handler)
                )
        self.stop_event = False

    def run(self):
        print("running")
        while not pn.ShouldQuit():
            print("ok")
            if self.stop_event == True:
                break
            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
            gl.glClearColor(1.0, 1.0, 1.0, 1.0)
            dcam.Activate(scam)

            pn.glDrawColouredCube()

            points = np.random.random((100000, 3)) * 10
            gl.glPointSize(2)
            gl.glColor3f(1.0, 0.0, 0.0)

            pn.FinishFrame()

        print("quit")



    def stop(self):
        self.stop_event = True

    def stopped(self):
        return self.stop_event
