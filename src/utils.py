import numpy as np
import matplotlib.pyplot as plt
import os

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
        image_to_load = images[random_idx][0]
        label = images[random_idx][1]
        image_to_show = load_image(image_to_load)
        axes = figure.add_subplot(columns, rows, idx + 1, )
        axes.imshow(image_to_show)
        axes.set_title(label=label)
        axes.axis('off')
    plt.show()