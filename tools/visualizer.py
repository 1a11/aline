from matplotlib import pyplot as plt
import numpy as np
import mpl_toolkits.mplot3d.axes3d as p3
from matplotlib import animation
import time

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
def vis():
    fig = plt.figure()

    ax = p3.Axes3D(fig)
    #ax = fig.add_subplot(111, projection='3d')
    import keyboard
    # create the parametric curve

##    x=[0]
##    y=[0]
##    z=[1]

    # create the first plot

    with open('machine.avis','r') as infile:
        code = infile.read()
    print(code)
    while True:
        exec(code)
##        ax.scatter([0], [0], [0], zdir='z', s=20,c='r')
##        point = ax.scatter(x, y, z, zdir='z', s=20,c='g')
##        point.remove()


    plt.show()

