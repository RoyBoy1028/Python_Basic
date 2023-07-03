import pyautogui as pag
import time 
import os
import keyboard

file_path = os.path.dirname(__file__)

running = True
while running:

    if keyboard.is_pressed("ctrl"):
        curr_time = time.strftime("%Y%m%d_%H%M%S")
        pag.screenshot(f"{file_path}/{curr_time}.png")

    elif keyboard.is_pressed("esc"):
        running = False