"""
读取png路径图片,在dat.txt读取剪裁xy坐标，剪裁图片，保存到指定路径
"""
import os
import cv2
import numpy as np
import matplotlib.pyplot as plt

def read_dat(dat_path):
    with open(dat_path, 'r') as f:
        lines = f.readlines()
    return lines

def crop_image(image_path, points, save_path):
    img = cv2.imread(image_path)
    x1, y1 = points[0]
    x2, y2 = points[1]
    crop_img = img[y1:y2, x1:x2, :]
    cv2.imwrite(save_path, crop_img)

if __name__ == '__main__':
    image_path = 'png'
    dat_path = 'dat.txt'
    save_path = 'res'
    lines = read_dat(dat_path)
    x1, y1 = lines[0].strip().split(' ')
    x2, y2 = lines[1].strip().split(' ')
    x1, x2, y1, y2 = int(x1), int(x2), int(y1), int(y2)
    points = [[x1, y1], [x2, y2]]
    for i in range(1, 51):
        crop_image(f'{image_path}/{i}.png', points, f'{save_path}/{i}.png')
