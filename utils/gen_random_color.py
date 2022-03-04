import cv2
import matplotlib.cm as cm
import numpy as np

from datetime import datetime
from pprint import pprint


def gen_zeros():
    return np.zeros((100, 100, 3))


def gen_random_color():
    num_classes = 60
    cmap = cm.rainbow(np.linspace(0.0, 1.0, num_classes))
    color_list = list()

    for i in range(len(cmap)):
        for j in range(len(cmap[i])):
            cmap[i][j] = cmap[i][j] * 256
    for i in range(len(cmap)):
        color_list.append(f'rgb({np.array(cmap[i][0]).astype(np.uint8)}, {np.array(cmap[i][1]).astype(np.uint8)}, {np.array(cmap[i][2]).astype(np.uint8)})')
    return color_list


if __name__ == '__main__':
    pprint(gen_random_color())
