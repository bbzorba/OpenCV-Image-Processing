import serial
import cv2
from datetime import datetime

ser = serial.Serial("/dev/ttyS0", 115200,timeout=0) # mini UART serial device

capture = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L) #stereo camera
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 2000)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 2000)

################MEASUREMENT OF DISTANCE USING BENEWAKE TF PRO LIDAR#####################
def read_tfluna_data():
    while True:
        counter = ser.in_waiting # count the number of bytes of the serial port
        if counter > 4:
            bytes_serial = ser.read(4) # read 9 bytes
            ser.reset_input_buffer() # reset buffer

            if bytes_serial[0] == 0x59 and bytes_serial[1] == 0x59: # check first two bytes
                distance = (bytes_serial[2] + bytes_serial[3]*256)/100.0 # distance data (in cm) is found in 2nd and 3rd bytes
                return distance

if ser.isOpen() == False:
    ser.open()
#########################################################################################

while(1):
    try:
        _, frame = capture.read()
        image = '/home/ubuntu/baris/escAerospace/sensors/LiDAR/image_outputs/stereoImage_{}_{}.tif'.format(datetime.now().strftime("%d_%m_%Y__%H_%M_%S"),'{0:0.2f}_meters'.format(read_tfluna_data()))
        cv2.imwrite(image, frame)
        
    except KeyboardInterrupt:
        ser.close()
