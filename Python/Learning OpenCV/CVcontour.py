import cv2 as cv
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cat', img)

blank = np.zeros(img.shape, dtype='uint8')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray', gray)
""" blur = cv.GaussianBlur(gray, (3,3), cv.BORDER_DEFAULT)

canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny) """

ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY) #based on intensity, sets pixel to black or white, 125-255 -> white
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
# RETR_LIST = all, RETR_EXTERNAL on the outside
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1) #-1:use all contours
cv.imshow('Contours drawn', blank)

cv.waitKey(0)