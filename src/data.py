import numpy as np
import os
import matplotlib.pyplot as plt

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
    img = np.mean(img, axis=2)
    img_normed = (img-np.min(img))/(np.max(img)-np.min(img))
    return img_normed


class ImageDataset():
    def __init__(s, base_path):
        s.img_paths = s.load_paths(base_path)

    def load_paths(s, p):
        labels = [l for l in os.listdir(p) if l.isdigit()]
        images = [(p+label+"/"+f, label)  for label in labels for f in os.listdir(p+label)]
        return images
    
    def __getitem__(s, idx):
        img_p, lbl = s.img_paths[idx]
        image = load_image(img_p)
        image = convert_image(image)
        label = int(lbl)
        return image, label
    
    def __len__(s):
        return len(s.img_objects)

    def show_batch(self, b):
        img,lbl = s.__getitem__(0)
        size = int(np.sqrt(b))
        figure = plt.figure(figsize=(2*size, 2*size))
        cols, rows = 2*size, size//2
        for i in range(1, cols * rows + 1):
            sample_idx = torch.randint(len(self), size=(1,)).item()
            img, label = s.__getitem__(sample_idx)
            figure.add_subplot(rows, cols, i)
            plt.title(str(label))
            plt.axis("off")
            plt.imshow(img.squeeze(), cmap="gray")
        plt.show()