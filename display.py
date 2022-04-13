from threading import Thread, Event
import numpy as np
import OpenGL.GL as gl
import pypangolin as pn

class Display(Thread):
    def __init__(self):
        Thread.__init__(self)
        self._stop = Event

    def run(self):
        # most definitely needs to go in init function and be class var
        pn.CreateWindowAndBind('Main', 640, 480)
        gl.glEnable(gl.GL_DEPTH_TEST)

        scam = pn.OpenGlRenderState(
                pn.ProjectionMatrix(640, 480, 420, 420, 320, 240, 0.1, 1000),
                pn.ModelViewLookAt(-0, 0.5, -3, 0, 0, 0, pn.AxisDirection.AxisY))

        handler = pn.Handler3D(scam)
        dcam = (
                pn.CreateDisplay()
                .SetBounds(
                    pn.Attach(0),
                    pn.Attach(1),
                    pn.Attach.Pix(180),
                    pn.Attach(1),
                    -640/480,
                    )
                .SetHandler(handler)
                )


        while not pn.ShouldQuit():
            gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
            gl.glClearColor(1.0, 1.0, 1.0, 1.0)
            dcam.Activate(scam)

            pn.glDrawColouredCube()

            points = np.random.random((100000, 3)) * 10
            gl.glPointSize(2)
            gl.glColor3f(1.0, 0.0, 0.0)

            pn.FinishFrame()


    def stop(self):
        self._stop.set()

    def stopped(self):
        return self._stop.isSet()
