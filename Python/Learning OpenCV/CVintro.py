import cv2

#capture video
cap = cv2.VideoCapture(0)

# get frames
_,pre_frame = cap.read() #0 cap.read() has two ouputs
_,cur_frame = cap.read() #1
_,next_frame = cap.read() #2

#resize
scalingFactor = 1
pre_frame = cv2.resize(pre_frame, None, fx=scalingFactor, fy=scalingFactor, 
                       interpolation=cv2.INTER_AREA)
cur_frame = cv2.resize(cur_frame, None, fx=scalingFactor, fy=scalingFactor, 
                       interpolation=cv2.INTER_AREA)
next_frame = cv2.resize(next_frame, None, fx=scalingFactor, fy=scalingFactor, 
                       interpolation=cv2.INTER_AREA)

# cvt: from RGB to grayscale
pre_frame = cv2.cvtColor(pre_frame, cv2.COLOR_RGB2GRAY)
cur_frame = cv2.cvtColor(cur_frame, cv2.COLOR_RGB2GRAY)
next_frame = cv2.cvtColor(next_frame, cv2.COLOR_RGB2GRAY)

#
haar_cascade = cv2.CascadeClassifier('Chapter18/haar_cascade_files/haarcascade_frontalface_default.xml')

while True:
    """
    diff_frame1 = cv2.absdiff(cur_frame, pre_frame)
    diff_frame2 = cv2.absdiff(next_frame, cur_frame)
    frame_diff = cv2.bitwise_and(diff_frame1, diff_frame2)
    
    # show image
    cv2.imshow('frame diff', frame_diff)
    
    # update frame
    pre_frame = cur_frame
    cur_frame = next_frame
    _,next_frame = cap.read()
    next_frame = cv2.resize(next_frame, None, fx=scalingFactor, fy=scalingFactor, 
                           interpolation=cv2.INTER_AREA)
    next_frame = cv2.cvtColor(next_frame, cv2.COLOR_RGB2GRAY)
    """
    
    # face detection
    _,frame = cap.read()
    frame = cv2.resize(frame, None, fx=scalingFactor, fy=scalingFactor, 
                           interpolation=cv2.INTER_AREA)
    gray = cv2.cvtColor(frame, cv2.COLOR_RGB2GRAY)
    face_rects = haar_cascade.detectMultiScale(gray, 1.1, 5)
    
    # markup face detection
    for (x,y,w,h) in face_rects:
        xText = x
        yText = y-20
        #cv2.rectangle(frame, (x,y), (x+w, y+h), (0,0,255), 3)
        cv2.circle(frame, (int(x+(w/2)), int(y+(h/2))), int(w/2), (0,0,255), thickness=2)
        cv2.line(frame, (x-20,int(y+(h/2))), (x+w+20, int(y+(h/2))), (0,0,255), thickness=2)
        cv2.line(frame, (int(x+(w/2)),int(y-20)), (int(x+(w/2)), int(y+h+20)), (0,0,255), thickness=2)
        cv2.putText(frame, 'TARGET AQUIRED', (xText,yText), cv2.FONT_HERSHEY_TRIPLEX, 1.0, (0,0,255), 2)
        
    # show image
    cv2.imshow('face detection', frame)
    
    # quit if "ESC"
    key = cv2.waitKey(10)
    if key == 27:
        break
    
cv2.destroyAllWindows()