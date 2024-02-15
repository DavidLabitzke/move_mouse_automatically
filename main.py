import pyautogui
import keyboard
from random import randint
import time

# Global Variables
mouse_new_coordinates = (None, None)
x_increment = None
y_increment = None

RESET_TIME = 0.02

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


def handle_mouse_movement():
    global mouse_new_coordinates
    mouse_current_pos = pyautogui.position()
    mouse_current_x, mouse_current_y = mouse_current_pos[0], mouse_current_pos[1]
    pos_needs_changed = mouse_new_coordinates == (None, None) or mouse_new_coordinates == mouse_current_pos
    if pos_needs_changed:
        mouse_new_coordinates = get_new_mouse_coordinates()
        mouse_new_x, mouse_new_y = mouse_new_coordinates[0], mouse_new_coordinates[1]
    move_mouse(*mouse_new_coordinates)

def main():
    try:
        while not keyboard.is_pressed("esc"):
            handle_mouse_movement()
            time.sleep(RESET_TIME)
    except KeyboardInterrupt:
        print("keyboard interrupt")


if __name__ == '__main__':
    main()
    print("Successfully aborted")
