def run():
    #import blobs
    #import aruco_beta
    import numpy as np
    import cv2
    from cv2 import aruco
    import matplotlib.pyplot as plt

    from ar_markers import detect_markers
    control = []
    for i in range(475):
        control.append(i)
    frame = cv2.imread("sampleEDT.png")

    im = cv2.imread("sampleNET.png")
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
            #print(int(i.id) in missing, i.id)
            if int(i.id) in missing:
                xy.append(i.center)
        i2+=1

    return (xy)
