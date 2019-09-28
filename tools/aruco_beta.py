import numpy as np
import cv2
from cv2 import aruco
import matplotlib.pyplot as plt

from ar_markers import detect_markers

control = []

for i in range(100):
    control.append(i)
frame = cv2.imread("markers_test.png")

im = cv2.imread("markers_test - blank.png")
i=0
markers, c_markers = detect_markers(frame), detect_markers(im)
marks = []
for marker in markers:
    marker.highlite_marker(frame)
    if i%2 == 0:
        #print(marker.id)
        marks.append(marker.id)
    i+=1

missing = []

xy = []
i2=0
for i in control:
    if i in marks:
        pass
    else:
        missing.append(i)

for i in c_markers:
    if i2%2 == 0:
        print(int(i.id) in missing, i.id)
        if int(i.id) in missing:
            xy.append(i.center)
    i2+=1


import numpy as np
import matplotlib.pyplot as plt

# Create data
x = []
y = []


for i in xy:
    x.append(i[0])
    y.append(i[1])

color1 = (0,0,0)
color2 = (255,0,0)
area = np.pi*3

x2 = [897 ,
702 ,
2064 ,
2161 ,
2064 ,
2161 ,
1869 ,
1577 ,]
y2 = [2807 ,
2941 ,
2003 ,
1734 ,
1601 ,
1600 ,
1466 ,
1333 ,]

# Plot
plt.scatter(x, y, c='blue')
plt.scatter(x2, y2, c='red')
plt.title('Objects heatmap')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



