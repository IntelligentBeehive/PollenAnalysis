import numpy as np
import cv2

# image matrix
#   img = cv2.imread('BeesWithPollen.jpeg', 1)
img = np.zeros([512, 1024, 3], np.uint8)

# drawing line, arrow line, rectangle and circle
#   coordination: (x, -y) from top-left
#   color: BGR (blue, green, red)
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 3)
img = cv2.arrowedLine(img, (100, 0), (355, 255), (255, 0, 0), 3)
img = cv2.rectangle(img, (390, 210), (440, 270), (0, 0, 255), 3)
img = cv2.circle(img, (665, 280), 25, (0, 255, 0), 3)

# add text
font = cv2.FONT_HERSHEY_SIMPLEX
img = cv2.putText(img, '#347', (390, 190), font, 0.5, (0, 255, 255), 1, cv2.LINE_AA)

# show image and hold
cv2.imshow('image', img)
cv2.waitKey(0)

# close all related windows
cv2.destroyAllWindows()
