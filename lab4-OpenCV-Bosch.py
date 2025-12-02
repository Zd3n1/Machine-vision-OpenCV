# steps:

# 1 RGB2GRAY
# 2 threshold
# 3 angle of rotation
# 4 bounding rectangle ( 1 error check width, height, angle )

# 5  crop
# 6 check center of mass
# 7 check character width and height
# 8 check area

# 9 maybe check for 7 elements (bounding box, sign, 5 letters)


import cv2

frame = cv2.imread('Bosch_image.tif')

frame_s = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_CUBIC)

cv2.imshow('Resized_image', frame_s)

cv2.createTrackbar('T', 'Resized_image', 0, 255, lambda x: None)


#GRB 2 Gray
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  #grayscale image


t = cv2.getTrackbarPos('T', 'Resized_image')
_, frame_t = cv2.threshold(gray, t, 255, cv2.THRESH_BINARY)
cv2.imshow('Binary', frame_t)


cv2.waitKey()
cv2.destroyAllWindows()
