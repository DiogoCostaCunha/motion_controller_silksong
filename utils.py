import math

def locate_col_row(grid_number, grid_cols, square_width, square_height):
    row = math.floor(grid_number/grid_cols)
    col = grid_number % grid_cols
    x = int(col * square_width)
    y = int(row * square_height)
    return x, y

def get_square_size(frame_width, frame_height, grid_cols, grid_rows):
    return frame_width / grid_cols, frame_height / grid_rows
