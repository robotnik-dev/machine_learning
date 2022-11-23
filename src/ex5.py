#!/usr/bin/env python3
import numpy as np
import os
from utils import load_image, convert_image, ImageDataset, gaussian, shift_x, shift_y, randomise_colors, flip
import matplotlib.pyplot as plt
import torch

def transforms(img):
    img = flip(img)
    img = gaussian(img)
    img = shift_x(img)
    img = shift_y(img)
    return img

def main():
    train_path = "./data/MYON/train/"
    train_dataset = ImageDataset(train_path, transform=transforms)
    # plt.subplot(1,3,1)
    plt.imshow(train_dataset[0][0], cmap="gray")
    # plt.subplot(1,3,2)
    # plt.imshow(train_dataset2[0][0], cmap="gray")
    # plt.subplot(1,3,3)
    # plt.imshow(train_dataset3[0][0], cmap="gray")

    plt.show()


if __name__ == '__main__':
    main()