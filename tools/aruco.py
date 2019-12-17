import numpy as np
import cv2
from cv2 import aruco
import matplotlib.pyplot as plt
import matplotlib as mpl
from ar_markers import detect_markers

control = []

for i in range(100):
    control.append(i)
frame = cv2.imread("markers_test.png")

im = cv2.imread("markers_test.png")
i=0
markers = detect_markers(frame)
marks = []
for marker in markers:
    marker.highlite_marker(frame)
    if i%2 == 0:
        print(marker.id)
        marks.append(marker.id)
    i+=1
plt.figure()
plt.imshow(frame)
plt.show()
print(markers)

missing = []

for i in control:
    if i in marks:
        pass
    else:
        missing.append(i)
mmin = min(missing) - 1
mmincord = 0
mmax = max(missing) + 1
mmaxcord = 0
for i in markers:
    if i.id == min(missing)-13:
        mmincord = i.center
    elif i.id == max(missing)+13:
        mmaxcord = i.center
    
crop_img = im[mmincord[1]:mmaxcord[1], mmincord[0]:mmaxcord[0]]
crop_img[np.where((crop_img == [0,0,0]).all(axis = 2))] = [255,255,255]
crop_img[np.where((crop_img == [18,18,18]).all(axis = 2))] = [255,255,255]
im = cv2.imwrite("markers_test_res.png", crop_img)
plt.figure()
plt.imshow(crop_img)
plt.show()
