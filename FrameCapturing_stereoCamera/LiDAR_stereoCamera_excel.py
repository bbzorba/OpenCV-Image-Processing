import serial
import cv2
import imutils
from datetime import datetime
import xlsxwriter

ser = serial.Serial("/dev/ttyS0", 115200,timeout=0) # mini UART serial device

capture = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L) #stereo camera


############################CREATING EXCEL FILES#################################
SensorBook = xlsxwriter.Workbook('/home/ubuntu/baris/escAerospace/sensors/LiDAR/excel_outputs/LiDAR_Data.xlsx')
sheet = SensorBook.add_worksheet()
#################################################################################

################MEASUREMENT AND WRITING THE DATA TO TEXT FILE#####################
def writeTime():
    now = datetime.now()
    current_time = now.strftime("%d_%m_%Y__%H:%M:%S")    
    return current_time
#################################################################################

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

#initial row and column
row = 0
column = 0

#Header of column0
initColumn0 = 'Distance(m)'
sheet.write(row, column, initColumn0)
column += 1

#Header of column1
initColumn1 = 'Date-Time(DD/MM/YYYY HH/MM/SS)'
sheet.write(row, column, initColumn1)
row += 1

while(1):
    try:
        column = 0
        
        distance = read_tfluna_data()
        LiDARData = '{0:0.2f}'.format(distance)
        sheet.write(row, column, LiDARData)

        column += 1
        
        current_time = writeTime()
        sheet.write(row, column, current_time)
        
        row += 1

        _, frame = capture.read()
        frame = imutils.resize(frame, width=1080)
        image = '/home/ubuntu/baris/escAerospace/sensors/LiDAR/image_outputs/stereoImage_{}.jpg'.format(datetime.now().strftime("%d_%m_%Y__%H:%M:%S"))
        cv2.imwrite(image, frame)
        
    except KeyboardInterrupt:
        ser.close()
        SensorBook.close()
