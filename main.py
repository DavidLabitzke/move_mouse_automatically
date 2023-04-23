import pyautogui
from random import randint
import time

RESET_TIME = 10

width = pyautogui.size().width
height = pyautogui.size().height

while True:
    time.sleep(RESET_TIME)
    new_x = randint(0, width)
    new_y = randint(0, height)
    pyautogui.moveTo(new_x, new_y)
