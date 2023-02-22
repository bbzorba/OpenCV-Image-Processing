import cv2
import numpy
from time import sleep
from datetime import datetime

# Open the ZED camera
cap = cv2.VideoCapture(0)
if cap.isOpened() == 0:
    exit(-1)

# Set the video resolution to HD720 (2560*720)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

while True :
    # Get a new frame from camera
    retval, frame = cap.read()
    # Extract left and right images from side-by-side
    combined_image = numpy.split(frame, 2, axis=1)
    #Save images
    left_image = '/home/ubuntu/image_outputs/stereoImage_left_{}.tif'.format(datetime.now().strftime("%d_%m_%Y__%H_%M_%S"))
    right_image = '/home/ubuntu/image_outputs/stereoImage_right_{}.tif'.format(datetime.now().strftime("%d_%m_%Y__%H_%M_%S"))
    cv2.imwrite(right_image, combined_image[0])
    cv2.imwrite(left_image, combined_image[1])

    sleep(0.5)

    if cv2.waitKey(30) >= 0 :
        break

exit(0)
