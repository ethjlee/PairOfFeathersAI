
import subprocess
import os
os.startfile("D:\SteamLibrary\steamapps\common\A Pair of Feathers Squawk Together\A Pair of Feathers Squawk Together.exe")

import cv2
import pyautogui
import numpy as np
import time
import sys
import random

print("hello")
# img = cv.imread(cv.samples.findFile("testimage.jpg"))
 
# if img is None:
#     sys.exit("Could not read the image.")
 
# cv.imshow("Display window", img)
# k = cv.waitKey(0)
 
# if k == ord("s"):
#     cv.imwrite("screenshot"+ str(random.randint(0,100000)) + ".png" , img)


import pygetwindow as gw

time.sleep(3)
# Get the game window's handle
game_window = gw.getWindowsWithTitle('A Pair of Feathers Squawk Together')[0]

# print(game_window)
start_time = time.time()
fps = 0


def startNewGame():
    time.sleep(2)
    pyautogui.press('down')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.press('space')
    time.sleep(1)
    pyautogui.keyDown('esc')
    time.sleep(5)
    pyautogui.keyUp('shift')


started = False
opened = False

while True:
# Capture the game window's output
    
    img = pyautogui.screenshot(region=(game_window.left, game_window.top, game_window.width, game_window.height))
    
    frame = np.array(img)
    
    # Convert the frame to BGR format
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    #cv2.imwrite('saved_image' + str(fps) + '.jpg', frame)
    # Display the frame in the OpenCV window
    cv2.imshow('Game Capture', frame)

    game_window.activate()
    
    if opened == False:
        time.sleep(3)
        opened = True
    
    if started == False:
        print("started")
        startNewGame()
        print("finished")
        started = True

    fps += 1
    # Exit on key press
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

end_time = time.time()
elapsed_time = end_time - start_time
cv2.destroyAllWindows()

print(f"FPS: {fps / elapsed_time}")
print(f"Time taken: {elapsed_time} seconds")


