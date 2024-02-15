import pyautogui
import keyboard
from random import randint
import time

RESET_TIME = 0.1

max_width = round(pyautogui.size().width * 0.9)
max_height = round(pyautogui.size().height * 0.9)

min_width = round(pyautogui.size().width - max_width)
min_height = round(pyautogui.size().height - max_height)


def get_new_mouse_coordinates():
    new_x = randint(min_width, max_width)
    new_y = randint(min_height, max_height)
    return new_x, new_y


def move_mouse(new_x, new_y):
    pyautogui.moveTo(new_x, new_y, duration=RESET_TIME)


def on_key_event(e):
    if e.name == "esc":
        print("escape key pressed")
        return False


def main():
    try:
        while not keyboard.is_pressed("esc"):
            new_coords = get_new_mouse_coordinates()
            move_mouse(*new_coords)
            time.sleep(RESET_TIME)
    except KeyboardInterrupt:
        print("keyboard interrupt")


if __name__ == '__main__':
    main()
    print("Successfully aborted")
