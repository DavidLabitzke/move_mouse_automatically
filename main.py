import pyautogui
import keyboard
from random import randint
import time
import math

# Global Variables
mouse_new_coordinates = (None, None)

RESET_TIME = 0.02
MINIMUM_DISTANCE_THRESHOLD = 100

max_width = round(pyautogui.size().width * 0.9)
max_height = round(pyautogui.size().height * 0.9)

min_width = round(pyautogui.size().width - max_width)
min_height = round(pyautogui.size().height - max_height)


def get_new_mouse_coordinates():
    new_x = randint(min_width, max_width)
    new_y = randint(min_height, max_height)
    return new_x, new_y


def handle_mouse_movement():
    global mouse_new_coordinates

    mouse_current_pos = pyautogui.position()
    mouse_current_x, mouse_current_y = mouse_current_pos[0], mouse_current_pos[1]

    pos_needs_changed = mouse_new_coordinates == (None, None) or mouse_new_coordinates == mouse_current_pos
    if not pos_needs_changed:
        dx = mouse_new_coordinates[0] - mouse_current_x
        dy = mouse_new_coordinates[1] - mouse_current_y
        total_distance = math.sqrt(dx ** 2 + dy ** 2)
        move_speed = 10
        if total_distance < MINIMUM_DISTANCE_THRESHOLD:
            total_distance /= 1000
            pyautogui.moveRel(dx, dy, duration=total_distance / move_speed)
        else:
            pyautogui.move(dx / move_speed, dy / move_speed)

    else:
        mouse_new_coordinates = get_new_mouse_coordinates()


def main():
    try:
        while not keyboard.is_pressed("esc"):
            handle_mouse_movement()
            time.sleep(RESET_TIME)
    except KeyboardInterrupt:
        pass


if __name__ == '__main__':
    main()
