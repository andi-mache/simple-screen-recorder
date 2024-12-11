# Import necessary libraries
import datetime
from PIL import ImageGrab
import numpy as np
import cv2
#from win32api import GetSystemMetrics
import pyautogui as pag 


width , height = pag.size()
# Get system screen size



# Get current timestamp for filename

time_stamp = datetime.datetime.now().strftime('%Y-%m-%d %H-%M-%S')
file_name = f'{time_stamp}.mp4'  # Define file name

# Define video codec and create VideoWriter object
fourcc = cv2.VideoWriter_fourcc('m', 'p', '4', 'v')
capture_video = cv2.VideoWriter(file_name, fourcc, 20.0, (1200, 750))

# Flag to keep recording running
on = True
while on:
    # Capture screen using ImageGrab
    img = ImageGrab.grab(bbox=(0, 0, width, height))
    # Convert the image into numpy array representation
    img_np = np.array(img)
    # Convert the BGR image into RGB image
    img_final = cv2.cvtColor(img_np, cv2.COLOR_BGR2RGB)
    # Show the RGB image
    cv2.imshow('screen capture', img_final)
    # Write the RGB image to file
    capture_video.write(img_final)
    # Wait for the user to press 's' key to stop the recording
    if cv2.waitKey(10) == ord('s'):
        on = False
