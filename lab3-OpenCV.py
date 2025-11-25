import cv2

cap = cv2.VideoCapture(0)
cv2.namedWindow("first example")

while (True):
    ret, frame = cap.read()
    if frame is None:
        print ("Empty frame")
        break

    cv2.imshow("first example", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    
cap.release()
cv2.destroyAllWindows()