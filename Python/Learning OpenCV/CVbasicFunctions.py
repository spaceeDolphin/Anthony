import cv2 as cv

img = cv.imread('Photos/cat.jpg')
cv.imshow('Cat', img)

# convert to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blur
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge cascade, good to combine with blur
canny = cv.Canny(blur, 125, 175)
cv.imshow('Canny Edges', canny)

# dilate image, thicker lines
dilated = cv.dilate(canny, (3,3), iterations=3)
cv.imshow('Dilated', dilated)

# eroding, thinner lines
eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

# resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
# use INTER_AREA when downscaling, INTER_CUBIC when upscaling
cv.imshow('Resized', resized)

# cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)