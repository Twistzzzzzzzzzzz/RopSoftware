import cv2
import torch.nn as nn
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image


def clahe_apply(image):
    clahe = cv2.createCLAHE(clipLimit=1.5, tileGridSize=(16, 16))
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    clahe_image = clahe.apply(gray)
    clahe_image_rgb = cv2.cvtColor(clahe_image, cv2.COLOR_GRAY2RGB)
    # cv2.imwrite("cropped_image2.jpg", clahe_image_rgb)
    # clahe_image = cv2.cvtColor(clahe_image, cv2.COLOR_RGB2GRAY)
    return clahe_image_rgb


def pre_processing(image, size=(256, 256), color=(0, 0, 0)):
    cimage = image
    image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # 二值化图像以便于边界检测
    _, binary_image = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    col_nonzero = np.count_nonzero(binary_image, axis=0)

    # 找到第一个和最后一个非零元素的索引，裁剪边界
    left = np.nonzero(col_nonzero)[0][0]
    right = np.nonzero(col_nonzero)[0][-1]
    cropped_image = cimage[:, left : right + 1]

    h, w = cropped_image.shape[:2]
    # 计算新的尺寸以保持纵横比
    if h > w:
        scale = size[1] / h
        new_h, new_w = size[1], int(w * scale)
    else:
        scale = size[0] / w
        new_h, new_w = int(h * scale), size[0]
    # 调整图像尺寸并填充黑边
    resized = cv2.resize(cropped_image, (new_w, new_h), interpolation=cv2.INTER_AREA)
    padded = np.full((size[1], size[0], 3), color, dtype=np.uint8)
    x_offset = (size[0] - new_w) // 2
    y_offset = (size[1] - new_h) // 2

    padded[y_offset : y_offset + new_h, x_offset : x_offset + new_w] = resized

    # gray = cv2.cvtColor(padded, cv2.COLOR_BGR2GRAY)

    clahe_image = clahe_apply(padded)
    return clahe_image
