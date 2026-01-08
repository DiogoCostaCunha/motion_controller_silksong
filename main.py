import cv2
import numpy as np
from pynput.keyboard import Key, Controller
import threading
import time
from grid import locate_col_row
import json
from utils import get_square_size
with open('settings.json', 'r') as f:
    settings = json.load(f)

LOWER_COLOR_BOUND = np.array(settings["LOWER_COLOR_BOUND"])
UPPER_COLOR_BOUND = np.array(settings["UPPER_COLOR_BOUND"])
DETECTION_THRESHOLD = settings["DETECTION_THRESHOLD"]
FRAME_WIDTH = settings["FRAME_WIDTH"]
FRAME_HEIGHT = settings["FRAME_HEIGHT"]
GRID_COLS = settings["GRID_COLS"]
GRID_ROWS = settings["GRID_ROWS"]
square_width, square_height = get_square_size(FRAME_WIDTH, FRAME_HEIGHT, GRID_COLS, GRID_ROWS)

keyboard = Controller()

cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL) 

cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

ret, frame = cap.read()
if not ret:
    print("Error: Could not read frame from camera.")
    exit()

print("Starting camera feed. Press 'q' to quit.")

with open('control_settings.json', 'r') as f:
    controls = json.load(f)

def keys_to_press_for(control_key):
    data = controls[control_key]
    if 'keys_to_press' in data and isinstance(data['keys_to_press'], list):
        return data['keys_to_press']
    return [data['key_to_press']]

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    hsv_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    mask = cv2.inRange(hsv_frame, LOWER_COLOR_BOUND, UPPER_COLOR_BOUND)

    should_be_active = set()

    for control in controls:
        grid_location = controls[control]["grid_numbers"]
        up_left_corner = locate_col_row(grid_location[0], GRID_COLS, square_width, square_height)

        bottom_right_corner = locate_col_row(grid_location[1], GRID_COLS, square_width, square_height)
        bottom_right_corner = (
            int(bottom_right_corner[0] + square_width), 
            int(bottom_right_corner[1] + square_height)
        )

        zone_roi = mask[up_left_corner[1]:bottom_right_corner[1], up_left_corner[0]:bottom_right_corner[0]]
        green_pixel_count = cv2.countNonZero(zone_roi)
        is_triggered = green_pixel_count > DETECTION_THRESHOLD

        if is_triggered:
            should_be_active.add(control)

        zone_color = (0, 0, 255) if is_triggered else (0, 255, 0)
        cv2.rectangle(frame, up_left_corner, bottom_right_corner, zone_color, 2)
        cv2.putText(frame, control, (int(up_left_corner[0] + (bottom_right_corner[0] - up_left_corner[0]) / 2), int(up_left_corner[1] + (bottom_right_corner[1] - up_left_corner[1]) / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
        pixel_text = f"{green_pixel_count}"
        cv2.putText(frame, pixel_text, (int(up_left_corner[0] + 5), int(bottom_right_corner[1] - 5)), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (255, 255, 255), 2)

    are_active = {key for key, zone_data in controls.items() if zone_data['active']}

    if should_be_active != are_active:
        
        for key in are_active:
            for _key in keys_to_press_for(key):
                if _key == 'Bind':
                    keyboard.release(Key.left)
                else:
                    keyboard.release(_key)

        for key in should_be_active:
            for _key in keys_to_press_for(key):
                if _key == 'Bind':
                    keyboard.press(Key.left)
                else:
                    keyboard.press(_key)

        for key, zone_data in controls.items():
            zone_data['active'] = key in should_be_active

    cv2.imshow('Camera Feed', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

print("Exiting program.")
cap.release()
cv2.destroyAllWindows()