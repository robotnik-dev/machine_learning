import numpy as np
import matplotlib.pyplot as plt
import os
import torch

def load_image(path):
    file = open(path, "rb").read()
    image = []
    for i in range(22):
        temp = []
        for j in range(22):
            red = file[20 + (i*22+j)*3]
            green = file[20 + (i*22+j)*3+1]
            blue = file[20 + (i*22+j)*3+2]
            temp.append([red, green, blue])
        image.append(temp)
    return image

def convert_image(img):
    np_img = np.array(img)
    gray = np_img[:,:,0] * 0.299 + np_img[:,:,1] * 0.587 + np_img[:,:,2] * 0.114
    img_normed = (gray - np.min(gray)) / (np.max(gray) - np.min(gray))

    return img_normed

def show_images(grid_size: int, path_to_images: str) -> None:
    labels = [l for l in os.listdir(path_to_images) if l.isdigit()]
    images = [(path_to_images+label+"/"+f, label)  for label in labels for f in os.listdir(path_to_images+label)]
    columns, rows = grid_size, grid_size
    figure = plt.figure()
    figure.set_figheight(20)
    figure.set_figwidth(20)
    for idx in range(grid_size * grid_size):
        random_idx = np.random.randint(low=0, high=len(images))
        img = images[random_idx][0]
        label = images[random_idx][1]
        img = load_image(img)
        image_to_show = convert_image(img)
        axes = figure.add_subplot(columns, rows, idx + 1, )
        axes.imshow(image_to_show, cmap="gray")
        axes.set_title(label=label)
        axes.axis('off')
    plt.show()


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

def shift_x(a):
    shift = np.random.randint(5)
    kernel = np.array([1, 2, 1]) # Here you would insert your actual kernel of any size
    norm = np.sum(np.outer(kernel, kernel))
    a = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, a)
    a = np.apply_along_axis(lambda x: np.convolve(np.roll(x, shift), kernel, mode='same'), 1, a)
    return a/norm

def shift_y(a):
    shift = np.random.randint(5)
    kernel = np.array([1, 2, 1]) # Here you would insert your actual kernel of any size
    norm = np.sum(np.outer(kernel, kernel))
    a = np.apply_along_axis(lambda x: np.convolve(np.roll(x, shift), kernel, mode='same'), 0, a)
    a = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, a)
    return a/norm

def randomise_colors(a):
    kernel = np.array([1, 2, 1]) # Here you would insert your actual kernel of any size
    norm = np.sum(np.outer(kernel, kernel))
    a = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 0, a)
    a = np.apply_along_axis(lambda x: np.convolve(x, kernel, mode='same'), 1, a)
    return a/norm

def flip(img):
    return img[:, -1::-1]
