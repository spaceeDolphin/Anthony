import cv2 as cv
import numpy as np

blank = np.zeros((500, 1000, 3), dtype='uint8') # blank image 500x500 with 3 color channels
cv.imshow('Blank', blank)

# paint color
""" blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank) """

# draw rectangle
""" cv.rectangle(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank) """

# draw circle
""" cv.circle(blank, (blank.shape[1]//2, blank.shape[0]//2), 40, (0,0,255), thickness=-1)
cv.imshow('Circle', blank) """

# draw line
""" cv.line(blank, (0,0), (blank.shape[1]//2, blank.shape[0]//2), (0,255,0), thickness=3)
cv.imshow('Line', blank) """

# write text on image
cv.putText(blank, 'TARGET AQUIRED', (255,255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
cv.imshow('Text', blank)

""" img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img) """

cv.waitKey(0)