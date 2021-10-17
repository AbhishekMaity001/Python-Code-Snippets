from threading import Thread
import cv2


class VideoShow:
    """
    Class that continuously shows a frame using a dedicated thread.
    """

    def __init__(self, frame=None):
        self.frame = frame
        self.stopped = False

    def stop(self):
        self.stopped = True

    def show(self):
        while not self.stopped:
            cv2.imshow("Threaded Video Show", self.frame)
            if cv2.waitKey(10) == ord("q"):
                self.stopped = True

    def start(self):
        Thread(target=self.show, args=()).start()
        return self
