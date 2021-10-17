import cv2 , datetime , json, time

from numpy.core.shape_base import block
from video_async import MultiCameraCapture
from add_datetime import add_timestamp
import asyncio
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor
from functools import partial

def yolo(frame):
    # time.sleep(0.2) # predict function here
    return frame


async def run_face_detection(frame):
    task1 = asyncio.create_task(add_timestamp(frame))
    await task1
    # await asyncio.gather(task1)
    await asyncio.sleep(0.001)

async def run_blocking_func(loop, frame):
    '''With Process Pool executor place here the CPU crunching functions & remove async from that function (It should be an ordinary function)'''
    with ProcessPoolExecutor() as pool:
        blocking_func = partial(yolo, frame) # When using the Process Pool executor make sure the func is not async its just ordinary function.
        frame = await loop.run_in_executor(pool, blocking_func) # also dont return the frame in add_timestamp function
    return frame

async def main(captured_obj):
    loop = asyncio.get_running_loop()
    while True:
        async for cam_name, cap in captured_obj.async_camera_gen():
            frame = await captured_obj.read_frame(cap)
            
            # frame = await add_timestamp(frame)
            # frame = .predict() put here the predict function

            # task1 = asyncio.create_task(add_timestamp(frame))
            # await asyncio.gather(task1)
            await run_face_detection(frame) # await till frame comes
            frame = await run_blocking_func(loop, frame)

            await captured_obj.show_frame(cam_name, frame)
        if cv2.waitKey(1)==27:
            break



            
            

if __name__ == "__main__":
    cameras = json.loads(open('D:\Data Science\Python-Code-Snippets\Concurrency in Python\camera_info.json').read())
    captured = MultiCameraCapture(sources=cameras)

    asyncio.run(main(captured_obj=captured))


    # while True:
    #     for cam_name, cap in multicam.captures.items():
            
    #         # reading the frames
    #         frame = multicam.read_frame(cap)
            
    #         # processing the frames
    #         frame = add_datetime.add_timestamp(frame)

    #         # showing the frames
    #         cv2.imshow(str(cam_name), frame)
    #     if cv2.waitKey(1)==27:
    #         break