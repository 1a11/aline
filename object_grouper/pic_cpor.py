from PIL import Image

im = Image.open("image.png")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения

for i in range(64):
    for j in range(48):
        if i != 64 and j != 48:
            im.crop(box=(x/64*i, y/48*j, x/64*(i+1)-1, y/48*(j+1)-1)).\
            save('image{}_{}.png'.format(str(i+1), str(j+1)))
