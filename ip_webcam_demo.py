import urllib
import cv2
import numpy as np
import urllib.request as ur

url = "http://192.168.1.6:8080/shot.jpg" # This is the image url that you will be receiving from mobile ip webcam

# imgResp = urllib.urlopen(url)

while True:
    imgResp = ur.urlopen(url)
    imgNp = np.array(bytearray(imgResp.read()), dtype=np.uint8) # Converting image Response into bytearray then into numpy image
    img = cv2.imdecode(imgNp, -1) # Convert into opencv image format
    cv2.imshow('IPWEBCAM', img)
    print(img)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break