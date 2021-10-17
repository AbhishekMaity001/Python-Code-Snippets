import cv2
import json
import numpy as np
import asyncio

class MultiCameraCapture:

    def __init__(self, sources:dict)->None:
        assert sources
        # print(sources)
        self.captures = {}   # creating a empty dictionary for storing all the cap objects for different files/cams
        
        # Looping over all the cameras
        for cam_id, link in sources.items():
            cap = cv2.VideoCapture(link)
            print("Camera Name is ==> ", cam_id)
            assert cap.isOpened()
            self.captures[cam_id] = cap # Storing the objects for every cams

    @staticmethod
    async def read_frame(capture):
        '''This is just a static method which will read the frames from the capture'''
        capture.grab()  # grab will make sure that frame is grabbed True or False
        ret, frame = capture.retrieve() # retrieve will fetch the actual frame array
        # print(frame)
        if not ret:
            print("Empty frame")
            return 
        return frame

    @staticmethod
    async def show_frame(window_name:str, frame:np.array):
        '''This is just a static method which will display the frames with a particular window name'''
        cv2.imshow(window_name, frame)
        await asyncio.sleep(0.001)


    async def async_camera_gen(self):
        '''This method generates the camera objects as mentioned in json file ===> stored in captures dict during initialization of the class'''
        for cam_name, capture in self.captures.items():
            # cap = cv2.VideoCapture(capture)
            # print("Camera Name is ==> ", cam_name)
            yield cam_name, capture
            await asyncio.sleep(0.001)



    





