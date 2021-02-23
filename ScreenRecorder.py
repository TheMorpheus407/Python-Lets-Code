import cv2
import numpy as np
import pyautogui

screen = (3840,2160)
fourcc = cv2.VideoWriter_fourcc(*"MP4V")
output = cv2.VideoWriter("output.mp4", fourcc, 30, screen)

for i in range(30*5):
    img = pyautogui.screenshot() #TODO region
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    output.write(frame)
    #TODO: Track Time and sleep for exact 30fps

output.release()