from threading import Thread
import cv2
from queue import Queue



class VideoGet:
    """
    Class that continuously gets frames from a VideoCapture object
    with a dedicated thread.
    """

    def __init__(self, src=0):
        self.stream = cv2.VideoCapture(src)
        (self.grabbed, self.frame) = self.stream.read()
        self.stopped = False
        self.frame_data = Queue(maxsize=128)

    def stop(self):
        self.stopped = True

    def get(self):
        ctr=1
        while not self.stopped:
            if not self.grabbed:
                self.stop()
            else:
                (self.grabbed, self.frame) = self.stream.read()
                self.frame_data.put({'id': ctr, 'frame':self.frame, 'is_processed':0})
                ctr += 1
                # store in redis queue ===> queue
                # thread sleep if video read over 


    def start(self):
        Thread(target=self.get, args=()).start()
        return self


