import cv2 as cv

# image read
""" img = cv.imread('Photos/cat_large.jpg')

cv.imshow('Cat', img) #display in window 
cv.waitKey(0)"""

# video read
capture = cv.VideoCapture('Videos/dog.mp4')

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(20) & 0xFF==ord('d'): # exit by typing d key
        break

capture.release()
cv.destroyAllWindows()
