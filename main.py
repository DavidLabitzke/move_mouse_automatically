import pyautogui
from random import randint
import time

RESET_TIME = 5

max_width = round(pyautogui.size().width * 0.9)
max_height = round(pyautogui.size().height * 0.9)

min_width = round(pyautogui.size().width - max_width)
min_height = round(pyautogui.size().height - max_height)


def main():
    while True:
        time.sleep(RESET_TIME)
        new_x = randint(min_width, max_width)
        new_y = randint(min_height, max_height)
        pyautogui.moveTo(new_x, new_y, duration=RESET_TIME)


if __name__ == '__main__':
    main()
