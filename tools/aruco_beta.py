import numpy as np
import cv2
from cv2 import aruco
import matplotlib.pyplot as plt

from ar_markers import detect_markers


im = cv2.imread("sampleNET.png")
i=0
c_markers = detect_markers(im)
marks = []
for marker in c_markers:
    marks.append(marker.center)
    i+=1

import get_missing
xy = get_missing.run()

import numpy as np
import matplotlib.pyplot as plt

# Create data
x = []
y = []


x1 =[]
y1 = []

for i in marks:
    x1.append(-i[1])
    y1.append(-i[0])

for i in xy:
    x.append(-i[1])
    y.append(-i[0])

color1 = (0,0,0)
color2 = (255,0,0)
area = np.pi*3



# Plot
plt.scatter(y1, x1, c='red')
plt.scatter(y, x, c='blue')

plt.title('Objects heatmap')
plt.xlabel('x')
plt.ylabel('y')
plt.show()



