import cv2
source = r"D:\Data Science\Upwork\Video 76.mp4"
cap = cv2.VideoCapture(0)
global captured_frame
while True:
    ret, frame = cap.read()
    cv2.imshow('Frame window', frame)

    if cv2.waitKey(10) & 0xFF == ord('c'):
        captured_frame = frame
        cv2.imshow('Second window', captured_frame)
    elif cv2.waitKey(10) & 0xFF == ord('q'):
        break
print('outside break')
cap.release()
cv2.destroyAllWindows()
# while True:
cv2.imshow('Detections', captured_frame)
cv2.waitKey(0)
