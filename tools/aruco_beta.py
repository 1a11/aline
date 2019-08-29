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
        #print(marker.id)
        marks.append(marker.id)
    i+=1
plt.figure()
plt.imshow(frame)
plt.show()
#print(markers)

missing = []

for i in control:
    if i in marks:
        pass
    else:
        missing.append(i)

im[np.where((im == [0,0,0]).all(axis = 2))] = [255,255,255]
im[np.where((im == [18,18,18]).all(axis = 2))] = [255,255,255]
##im = cv2.imwrite("markers_test_res.png", crop_img)
plt.figure()
plt.imshow(im)
plt.show()

im = cv2.imwrite("markers_test_res.png", im)
im = cv2.imread("markers_test_res.png")

imgray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)

nim = cv2.resize(imgray,(360,480))

cv2.imshow('ImageWindow', nim)

ret, thresh = cv2.threshold(imgray, 20, 255,cv2.THRESH_BINARY)


nim = cv2.resize(thresh,(360,480))

cv2.imshow('ImageWindow', nim)
 
contours, hierarchy = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)



cnt = contours[4]
for contour in contours:
        cv2.drawContours(im, cnt, -1, (0, 255, 0), 3)

plt.figure()
plt.imshow(im)
plt.show()
