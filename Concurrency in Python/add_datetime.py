import datetime, cv2
import asyncio
import time

async def add_timestamp(frame):
    dt = str(datetime.datetime.now().time())
    frame = cv2.putText(frame, dt, (10,100), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2, cv2.LINE_8)
    # time.sleep(0.5)
    asyncio.sleep(0.001)
    return frame
    