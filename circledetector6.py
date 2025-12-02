import cv2
import numpy as np


image = cv2.imread("circles6.jpg",cv2.IMREAD_COLOR)                                                                                         
cv2.imshow("circles and ovals",image)
cv2.waitKey(0)
#convert image into greyscale as it is easier for the computer to detect
grey = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
#convert image into grid of three by three
grid = cv2.blur(grey,(3,3))
#we will use HoughCircles to detect the circles
#this function will take a few permaters grid, code for Hough gradient, resolution, distance between circles parem1, parem2 (theese are for the threshold values)
#minimum radius and maximum radius
detectedcircles = cv2.HoughCircles(grid,cv2.HOUGH_GRADIENT,1,20,param1= 50,param2=30,minRadius=1,maxRadius=50)
#if it detects circles in the picture
if detectedcircles is not None:
    #converts the detectedcircles into numbers
    detectedcircles = np.uint16(np.around(detectedcircles))
    for i in detectedcircles[0,:]:
        x,y,z = i[0],i[1],i[2]
        cv2.circle(image,(x,y),z,(255,0,0),5)
        cv2.circle(image,(x,y),1,(0,255,0),5)
        cv2.imshow("detected circles",image)
        cv2.waitKey(0)
cv2.destroyAllWindows()