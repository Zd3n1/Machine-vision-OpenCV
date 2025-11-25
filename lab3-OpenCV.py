import cv2
import numpy as np
import random as rng

rng.seed(1234)

gray = None

def detect(c):
    shape = "unidentified"
    peri = cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, 0.04 * peri, True)
    if len(approx) == 3:
        shape = "triangle"
    elif len(approx) == 4:
        (x, y, w, h) = cv2.boundingRect(approx)
        ar = w / float(h)
        shape = "square" if ar >= 0.95 and ar <= 1.05 else "rectangle"
    elif len(approx) == 5:
        shape = "pentagon"
    else:
        (x, y, w, h) = cv2.boundingRect(approx)
        (cx, cy), radius = cv2.minEnclosingCircle(approx)
        circleArea = np.pi * (radius ** 2)
        area = cv2.contourArea(c)
        if circleArea < 1.2 * area and circleArea > 0.8 * area:
            shape = "circle"
    return shape

def canny_tresh(val):
    print(val)
    global gray
    if gray is None:
        return
    blurred = cv2.GaussianBlur(gray, (5,5), 0)
    canny_out=cv2.Canny(blurred, val, val*2)
    cv2.imshow("Gray", canny_out)

    countours, hierarchy = cv2.findContours(canny_out, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mu = [None]*len(countours)
    for i in range(len(countours)):
        mu[i] = cv2.moments(countours[i])

    mc = [None]*len(countours)
    for i in range(len(countours)):
        if mu[i]['m00'] != 0:
            mc[i] = (mu[i]['m10']/mu[i]['m00'], mu[i]['m01']/mu[i]['m00'])
        else:
            mc[i] = (0, 0)
            
    
    drawing = np.zeros((canny_out.shape[0], canny_out.shape[1], 3), dtype=np.uint8)
    
    for i in range(len(countours)):
        shape = detect(countours[i])

        color = (rng.randint(0,256), rng.randint(0,256), rng.randint(0,256))
        cv2.drawContours(drawing, countours, i, color, 2)
        cv2.circle(drawing, (int(mc[i][0]), int(mc[i][1])), 4, color, -1)
        if int(mu[i]["m00"]) != 0:
            cv2.putText(drawing, shape, (int(mc[i][0]) - 20, int(mc[i][1]) - 20), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
    
 
    
    cv2.imshow('Contours', drawing)
    
 
    # Calculate the area with the moments 00 and compare with the result of the OpenCV function
    for i in range(len(countours)):
        print(' * Contour[%d] - Area (M_00) = %.2f - Area OpenCV: %.2f - Length: %.2f' % (i, mu[i]['m00'], cv2.contourArea(countours[i]), cv2.arcLength(countours[i], True)))

cap = cv2.VideoCapture(0)
cv2.namedWindow("first example")
cv2.createTrackbar("threshold", "first example", 0, 255, canny_tresh)

cv2.setTrackbarPos("threshold", "first example", 90)

while (True):
    ret, frame = cap.read()
    if frame is None:
        print ("Empty frame")
        break

    cv2.imshow("first example", frame)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()