from graph_grouper import *
import matplotlib.pyplot as plt
from matplotlib import colors as mcolors
import random

colors = dict(mcolors.BASE_COLORS, **mcolors.CSS4_COLORS)
by_hsv = sorted((tuple(mcolors.rgb_to_hsv(mcolors.to_rgba(color)[:3])), name)
                for name, color in colors.items())
sorted_names = [name for hsv, name in by_hsv]


fig = plt.figure()
dots = group()
i2 = 0
for i in dots:
    i2 = random.randint(0,len(colors)-1)
    for j in i:
        plt.scatter(j[0],j[1], c = colors[sorted_names[i2]])
plt.show()

