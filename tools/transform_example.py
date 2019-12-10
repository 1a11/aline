import sys
import numpy as np
import cv2 as cv
from numpy import * 
    # USAGE
    # python transform_example.py --image images/example_01.png --coords "[(73, 239), (356, 117), (475, 265), (187, 443)]"
    # python transform_example.py --image images/example_02.png --coords "[(101, 185), (393, 151), (479, 323), (187, 441)]"
    # python transform_example.py --image images/example_03.png --coords "[(63, 242), (291, 110), (361, 252), (78, 386)]"

def cir(img):
    
    import cv2 
    import numpy as np 
      
    # Read image. 
    img = cv2.imread(img, cv2.IMREAD_COLOR) 
      
    # Convert to grayscale. 
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) 
      
    # Blur using 3 * 3 kernel. 
    gray_blurred = cv2.blur(gray, (5, 5)) 
      
    # Apply Hough transform on the blurred image. 
    detected_circles = cv2.HoughCircles(gray_blurred,  
                       cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, 
                   param2 = 30, minRadius = 0, maxRadius = 50) 
      
    # Draw circles that are detected. 
    if detected_circles is not None: 
      
        # Convert the circle parameters a, b and r to integers. 
        detected_circles = np.uint16(np.around(detected_circles)) 
        dots = []
        for pt in detected_circles[0, :]: 
            a, b, r = pt[0], pt[1], pt[2] 
      
            # Draw the circumference of the circle. 
            cv2.circle(img, (a, b), r, (0, 255, 0), 2) 
            print(a,b,r)
            dots.append((a,b))
            # Draw a small circle (of radius 1) to show the center. 
            cv2.circle(img, (a, b), 1, (0, 0, 255), 3) 
##            cv2.imshow("Detected Circle", img)
        cv2.imwrite('res.png',img)
##            cv2.waitKey(0) 
        return(dots)

def shit(img, cords):
    # import the necessary packages
    from transform import four_point_transform
    import numpy as np
    import argparse
    import cv2

    # construct the argument parse and parse the arguments
   
    # load the image and grab the source coordinates (i.e. the list of
    # of (x, y) points)
    # NOTE: using the 'eval' function is bad form, but for this example
    # let's just roll with it -- in future posts I'll show you how to
    # automatically determine the coordinates without pre-supplying them
    image = cv2.imread(img)
    pts = np.array(cords, dtype = "float32")

    # apply the four point tranform to obtain a "birds eye view" of
    # the image
    warped = four_point_transform(image, pts)

    # show the original and warped images
##    cv2.imshow("Original", image)
##    cv2.imshow("Warped", warped)
##    cv2.waitKey(0)
    cv2.imwrite('cropped.png',warped)
res = cir('tst.jpg')
shit('tst.jpg', [res[0], res[1], res[2], res[3]])
