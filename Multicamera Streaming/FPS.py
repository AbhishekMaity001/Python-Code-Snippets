import datetime

class FPS:
    def __init__(self):
        self._start = None
        self._end = None
        self._numFrames = 0

    def start(self):
        self._start = datetime.datetime.now()
        return self
    
    def stop(self):
        self._end = datetime.datetime.now()
        return self
    
    def update(self):
        # updating the frames examined during start and end timestamp
        self._numFrames +=1

    def elapsed(self):
        # grabbing the total number of seconds elapsed based on start and end timestamp
        return (self._end-self._start).total_seconds()

    def fps(self):
        return self._numFrames/self.elapsed()

