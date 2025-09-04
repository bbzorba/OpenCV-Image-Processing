import cv2
import time

def main():
    capture = cv2.VideoCapture('/dev/video0', cv2.CAP_V4L) # open camera

    capture.set(cv2.CAP_PROP_FRAME_WIDTH, 2560)
    capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 1440)

    file1 = '/home/ubuntu/baris/escAerospace/sensors/VideoCamera/outputs/randomVideo.mp4'
    recorder = None
    now = time.time()
    timer = 0

    while(timer <= 20):
        _, frame = capture.read()

        if recorder is None and file1 is not None:
            fourcc = cv2.VideoWriter_fourcc(*"mp4v") #take video
            recorder = cv2.VideoWriter(file1, fourcc, 24.0,(frame.shape[1],frame.shape[0]),True) #write video to a file
            
        timer = time.time() - now
        print(timer)

        filename = '/home/ubuntu/screenshot.jpg'
        cv2.imwrite(filename, frame)      

    capture.release()

    recorder.release()

if __name__ == "__main__":
    main()
