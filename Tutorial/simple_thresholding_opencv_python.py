import cv2 as cv
import numpy as np

img = cv.imread('color_wheel.jpg', 0)

cv.imshow('image', img)

cv.waitKey(0)
cv.destroyAllWindows()
