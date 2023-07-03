import pyautogui as pag
import time 
import os

time.sleep(3)

file_path = os.path.dirname(__file__)

for i in range(1, 5):
    curr_time = time.strftime("%Y%m%d_%H%M%S")
    pag.screenshot(f"{file_path}/{curr_time}.png")
    time.sleep(1)
