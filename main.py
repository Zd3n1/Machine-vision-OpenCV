#does everything work?
import matplotlib.pyplot as plt
import cv2


mylist = [1, 2, 3, 4, "banana"]
mylist.append("apple")
mylist[1] = "orange"


plt.plot(1, 2, 3, 4, 5, 6)
#plt.show()

print("OpenCV version:", cv2.__version__)
print(mylist)

Img = cv2.imread("test.jpg",0)

cv2.imshow("Image", Img)

cv2.waitKey(0)
cv2.destroyAllWindows()
