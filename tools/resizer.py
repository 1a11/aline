import os
from os import listdir
from os.path import isfile, join
import PIL
import os
import threading
import time
from PIL import Image

global tn
tn = 0

def split_list(alist, wanted_parts=1):
    length = len(alist)
    return [ alist[i*length // wanted_parts: (i+1)*length // wanted_parts] 
             for i in range(wanted_parts) ]


def res(pics):
    global tn
    for file in pics:
        if '.JPG' in file:
            image = Image.open(file)
            image = image.resize((50,50),Image.ANTIALIAS)
            image.save(file,optimize=True,quality=95)
    tn+=1
    if tn>=10:
        print('Done. Files counter: {}'.format(len(files)))
        print()
        print('This window will close automatically after 30 seconds or close it yourself...')
        time.sleep(30)
        exit()
            

files = files = [os.path.join(r,file) for r,d,f in os.walk("./") for file in f]
for i in files:
    if '.py' in i:
        files.remove(i)
F1, F2, F3, F4, F5, F6, F7, F8, F9, F10 = split_list(files, wanted_parts=10)

t = threading.Thread(target=res, args=(F1,))
t.start()
t = threading.Thread(target=res, args=(F2,))
t.start()
t = threading.Thread(target=res, args=(F3,))
t.start()
t = threading.Thread(target=res, args=(F4,))
t.start()
t = threading.Thread(target=res, args=(F5,))
t.start()
t = threading.Thread(target=res, args=(F6,))
t.start()
t = threading.Thread(target=res, args=(F7,))
t.start()
t = threading.Thread(target=res, args=(F8,))
t.start()
t = threading.Thread(target=res, args=(F9,))
t.start()
t = threading.Thread(target=res, args=(F10,))
t.start()
