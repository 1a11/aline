from PIL import Image

im = Image.open("sample.png")
pixels = im.load()  # список с пикселями
x, y = im.size  # ширина (x) и высота (y) изображения

for i in range(3):
    for j in range(4):
        if i != 3 and j != 4:
            im.crop(box=(x/3*i, y/4*j, x/3*(i+1)-1, y/4*(j+1)-1)).\
            save('image{}_{}.png'.format(str(i+1), str(j+1)))
