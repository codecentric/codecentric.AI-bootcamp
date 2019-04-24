# Funktionen, um die Landmarks umzurechnen

from math import atan2, degrees, sqrt


def back_transform(y, x, y_max, x_max):
    x = float(x)
    y = float(y)
    x_new = x + 1
    x_new = x_new / 2
    x_new = x_new * x_max

    y_new = y + 1
    y_new = y_new / 2
    y_new = y_new * y_max
    return int(x_new), int(y_new)


def mean_point(p1, p2):
    x = (p1[0] + p2[0]) // 2
    y = (p1[1] + p2[1]) // 2
    return x, y


def angle_between(p1, p2):
    x_diff = p2[0] - p1[0]
    y_diff = p2[1] - p1[1]
    return degrees(atan2(y_diff, x_diff))


def dist_points(p1, p2):
    return sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def get_image_center(image):
    return image.size[0] // 2, image.size[1] // 2
