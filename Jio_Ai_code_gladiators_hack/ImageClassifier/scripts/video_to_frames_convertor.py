import cv2 
from os.path import join
import time

# Function to extract frames 
def FrameCapture(path): 
      
    # Path to video file 
    #fps = 0.5
    vidObj = cv2.VideoCapture(path) 
    #vidObj.set(cv2.CAP_PROP_FPS, fps)
    # Used as counter variable 
    count = 0
  
    # checks whether frames were extracted 
    success = 1

    dir_path = "/home/anton/Workspace/Hackathons/jio_car_parking_challenge/dataset6"
    #startTime = time.time()

    fpsLimit= 20
    prev = 0

    while success:
        # vidObj object calls read 
        # function extract frames
        #nowTime = time.time()
        time_elapsed = time.time() - prev
        success, image = vidObj.read()
        #if (int(nowTime - startTime)) < fpsLimit:
        if time_elapsed > 1./fpsLimit:
            prev = time.time()

            fpath = join(dir_path, "frame_{}.jpg".format(count))
            cv2.imwrite(fpath, image)
            print("{}, status: {}".format(fpath, success))


            count += 1
  
# Driver Code 
if __name__ == '__main__': 
	  
    # Calling the function 
    FrameCapture("/home/anton/Workspace/Hackathons/jio_car_parking_challenge/dataset6/video1.mp4")
