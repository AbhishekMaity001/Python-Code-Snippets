import argparse
import cv2
from CountsPerSec import CountsPerSec
from VideoGet import VideoGet
from VideoShow import VideoShow


def putIterationsPerSec(frame, iterations_per_sec):
    """
    Add iterations per second text to lower-left corner of a frame.
    """

    cv2.putText(frame, "{:.0f} iterations/sec".format(iterations_per_sec),
                (10, 450), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 0, 0))
    return frame


def noThreading(source):
    """Grab and show video frames without multithreading. ie... All on a single Thread!!"""

    cap = cv2.VideoCapture(source)
    cps = CountsPerSec().start()

    while True:
        (grabbed, frame) = cap.read()  # reading from source
        if 0xFF & cv2.waitKey(10) == ord("q"):
            break
        frame = putIterationsPerSec(frame, cps.countsPerSec())  # writing into the frame
        cv2.imshow("Video", frame)  # displaying the frame
        cps.increment()


def threadVideoGet(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Main thread shows video frames.
    """

    video_getter = VideoGet(source).start()  # Starting the 2nd thread (1st thread will be default daemon thread)
    cps = CountsPerSec().start()
    # 100 frames ==> queue ==> queue access  ==> queue remove

    while True:
        if (cv2.waitKey(10) == ord("q")) or video_getter.stopped:
            video_getter.stop()
            break

        # frame_only = video_getter.frame  # Getting the latest frame from the running Thread
        frame = video_getter.frame_data.get()
        print(frame)
        frame_only = frame['frame']

        frame = putIterationsPerSec(frame_only, cps.countsPerSec())  # Processing the frame
        cv2.imshow("Threaded Video Frames", frame_only)  # Displaying the frame
        cps.increment()


def threadVideoShow(source=0):
    """
    Dedicated thread for showing video frames with VideoShow object.
    Main thread grabs video frames.
    """

    cap = cv2.VideoCapture(source)
    (grabbed, frame) = cap.read()
    video_shower = VideoShow(frame).start()  # Starting a new thread which is only dedicated to showing frames!
    cps = CountsPerSec().start()

    while True:
        (grabbed, frame) = cap.read()
        if not grabbed or video_shower.stopped:
            video_shower.stop()
            break

        frame = putIterationsPerSec(frame, cps.countsPerSec())
        video_shower.frame = frame  # setting the VideoShow object to current frame
        cps.increment()


def threadBoth(source=0):
    """
    Dedicated thread for grabbing video frames with VideoGet object.
    Dedicated thread for showing video frames with VideoShow object.
    Main thread serves only to pass frames between VideoGet and
    VideoShow objects/threads.
    """

    video_getter = VideoGet(source).start()  # Starting Thread 1
    # Store the frames in Queue
    # Fetch the frames from Queue then pass to the next function & show
    video_shower = VideoShow(video_getter.frame).start()  # Starting Thread 2
    cps = CountsPerSec().start()

    while True:
        if video_getter.stopped or video_shower.stopped:
            video_shower.stop()
            video_getter.stop()
            break

        frame = video_getter.frame  # Thread 1

        # Processor - thread - main
        frame = putIterationsPerSec(frame, cps.countsPerSec())  # Main Thread just taking the frames processing it then displaying it back!
        
        video_shower.frame = frame  # Thread 2
        cps.increment()


source = r'D:\Data Science\Upwork\Vechicle Detection\sample1.mp4'
# noThreading(source)
threadVideoGet(source)
# threadVideoShow(source)
# threadBoth(source)
