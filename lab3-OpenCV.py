import cv2


def canny_tresh(val):
    #print(val)
    canny_out=cv2.Canny(gray, val, val*2)
    cv2.imshow("Gray", canny_out)

    countours, hierarchy = cv2.findContours(canny_out, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    mu = [None]*len(countours)
    for i in range(len(countours)):
        mu[i] = cv2.moments(countours[i])

cap = cv2.VideoCapture(0)
cv2.namedWindow("first example")
cv2.createTrackbar("threshold", "first example", 0, 255, canny_tresh)

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