import cv2
import numpy as np
import os
from PIL import Image, ImageDraw


def find_dot(image_path):
    image = cv2.imread(image_path)

    mask = np.any(image != [255, 255, 255], axis=2)

    y_coords, x_coords = np.where(mask)

    if len(x_coords) == 0:
        return None

    x = round(x_coords.mean(), 2)
    y = round(y_coords.mean(), 2)

    colour = image[y_coords[0], x_coords[0]].tolist()

    return x, y, colour


def get_layer_number(filename):
    return int(filename.split()[1].split(".")[0])


files = [f for f in os.listdir("assets") if f.endswith(".png")]
files.sort(key=get_layer_number)

canvas = Image.new("RGB", (512, 512), "white")
draw = ImageDraw.Draw(canvas)

previous_point = None
previous_colour = None

for filename in files:
    result = find_dot(os.path.join("assets", filename))

    if result is None:
        previous_point = None
        previous_colour = None
        continue

    x, y, colour = result
    current_point = (int(x), int(y))

    if previous_point is not None:
        rgb_colour = tuple(reversed(previous_colour))
        draw.line(
            [previous_point, current_point],
            fill=rgb_colour,
            width=2
        )

    previous_point = current_point
    previous_colour = colour

canvas.save("output.png")
