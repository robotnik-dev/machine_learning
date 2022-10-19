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
