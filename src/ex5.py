#!/usr/bin/env python3
import numpy as np
import os
from utils import load_image, convert_image
import matplotlib.pyplot as plt
import torch


class ImageDataset():
    def __init__(self, base_path, transform=None):
        self.img_paths = self.load_paths(base_path)
        self.tranform = transform

    def load_paths(self, p):
        labels = [l for l in os.listdir(p) if l.isdigit()]
        images = [(p+label+"/"+f, label)  for label in labels for f in os.listdir(p+label)]
        return images
    
    def __getitem__(self, idx):
        img_p, lbl = self.img_paths[idx]
        image = load_image(img_p)
        image = np.array(image)
        image = convert_image(image)
        if self.tranform:
            image = self.tranform(image)
        label = int(lbl)
        return image, label
    
    def __len__(self):
        return len(self.img_objects)

    def show_batch(self, b):
        img,lbl = self.__getitem__(0)
        size = int(np.sqrt(b))
        figure = plt.figure(figsize=(2*size, 2*size))
        cols, rows = 2*size, size//2
        for i in range(1, cols * rows + 1):
            sample_idx = torch.randint(len(self), size=(1,)).item()
            img, label = self.__getitem__(sample_idx)
            figure.add_subplot(rows, cols, i)
            plt.title(str(label))
            plt.axis("off")
            plt.imshow(img.squeeze(), cmap="gray")
        plt.show()


def gaussian(a):
    kernel = np.array([1, 2, 1]) # Here you would insert your actual kernel of any size
    norm = np.sum(np.outer(kernel, kernel))
    a = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, a)
    a = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, a)
    return a/norm

def main():
    train_path = "./data/MYON/train/"
    train_dataset = ImageDataset(train_path, transform=gaussian)

    plt.imshow(train_dataset[0][0], cmap="gray")
    plt.show()


if __name__ == '__main__':
    main()