# 2 points - pixel for pixel, draw a line between them
from PIL import Image


def slope_and_const(point1: tuple, point2: tuple) -> tuple:
    if point1[1] == point2[1]:
        return "infinity", point1[0]
    slope = (point2[1] - point1[1]) / (point2[0] - point1[0])
    return slope, point1[1] - point1[0] * slope


def draw_line_segment(point1: tuple, point2: tuple, color: tuple = (0, 0, 0), width: float = 1, bckgrnd_color: str = "white"):
    img = Image.new("RGB", (256, 256), bckgrnd_color)
    pixels = img.load()
    if point1[0] > point2[0]:
        point1, point2 = point2, point1
        # Switch the order of points if x coordinate of the first point is greater to avoid problems with iterating

    line = slope_and_const(point1, point2)

    if line != "infinity" and line[0] < 1:
        for x in range(point1[0], point2[0]):
            y = int(line[0] * x + line[1])
            pixels[x, y] = color

    if point1[1] > point2[1]:
        point1, point2 = point2, point1
        # switch if y coordinate of the first point is greater to avoid problems with iterating

    if line != "infinity" and line[0] >= 1

    if line[0] == "infinity":
        for y in range(point1[1], point2[1]):
            pixels[line[1], y] = (0, 0, 0)
