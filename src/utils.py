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