import cv2
import numpy as np
import json
import math
from utils import locate_col_row, get_square_size

if __name__ == "__main__":

    with open('settings.json', 'r') as f:
        settings = json.load(f)

    if settings["FRAME_WIDTH"] == -1 or settings["FRAME_HEIGHT"] == -1:

        cv2.namedWindow('Camera Feed', cv2.WINDOW_NORMAL) 

        cap = cv2.VideoCapture(0)
        if not cap.isOpened():
            print("Error: Could not open camera.")
            exit()

        ret, frame = cap.read()
        if not ret:
            print("Error: Could not read frame from camera.")
            exit()
        FRAME_HEIGHT, FRAME_WIDTH, _ = frame.shape

        settings["FRAME_WIDTH"] = FRAME_WIDTH
        settings["FRAME_HEIGHT"] = FRAME_HEIGHT

        with open('settings.json', 'w') as f:
            json.dump(settings, f)

        # close the camera
        cap.release()
        cv2.destroyAllWindows()

    FRAME_WIDTH = settings["FRAME_WIDTH"]
    FRAME_HEIGHT = settings["FRAME_HEIGHT"]
    GRID_COLS = settings["GRID_COLS"]
    GRID_ROWS = settings["GRID_ROWS"]

    square_width, square_height = get_square_size(FRAME_WIDTH, FRAME_HEIGHT, GRID_COLS, GRID_ROWS)

    # don't allow grid cols that are not divisible by 3
    if GRID_COLS % 3 != 0:
        print("Error: Grid cols are not divisible by 3.")
        exit()

    if (GRID_COLS / 3) % 2 != 0:
        print("Error: Grid cols for each player are not divisible by 2.")
        exit()

    black_image = np.zeros((FRAME_HEIGHT, FRAME_WIDTH, 3), dtype=np.uint8)

    for i in range(0, GRID_ROWS + 1):
        y = int(i * square_height)
        cv2.line(black_image, (0, y), (FRAME_WIDTH - 1, y), (255, 255, 255), 1)

    for i in range(0, GRID_COLS + 1):
        x = int(i * square_width)
        cv2.line(black_image, (x, 0), (x, FRAME_HEIGHT - 1), (255, 255, 255), 1)

    count = 0
    for i in range(GRID_ROWS):
        for j in range(GRID_COLS):
            x = int(j * square_width)
            y = int(i * square_height)
            cv2.putText(black_image, str(count), (x + 5, y + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.29, (255, 255, 255), 1)
            count += 1

    # Draw three vertical green lines at the thirds of the image
    third_width = FRAME_WIDTH / 3
    for i in range(1, 3):  # Lines at 1/3 and 2/3 positions
        x = int(i * third_width)
        cv2.line(black_image, (x, 0), (x, FRAME_HEIGHT - 1), (0, 255, 0), 2)

    # load the controls json file
    with open('control_settings.json', 'r') as f:
        controls = json.load(f)

    # draw the area for each control    
    for control in controls:
        grid_location = controls[control]["grid_numbers"]
        up_left_corner = locate_col_row(grid_location[0], GRID_COLS, square_width, square_height)

        bottom_right_corner = locate_col_row(grid_location[1], GRID_COLS, square_width, square_height)
        bottom_right_corner = (
            int(bottom_right_corner[0] + square_width), 
            int(bottom_right_corner[1] + square_height)
        )

        cv2.rectangle(black_image, up_left_corner, bottom_right_corner, (0, 255, 0), -1)
        cv2.putText(black_image, control, (int(up_left_corner[0] + (bottom_right_corner[0] - up_left_corner[0]) / 2), int(up_left_corner[1] + (bottom_right_corner[1] - up_left_corner[1]) / 2)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)


    cv2.imshow('Grid', black_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # export the grid as a png file
    cv2.imwrite('control_grid.png', black_image)
