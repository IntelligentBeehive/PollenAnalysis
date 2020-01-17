import numpy as np
import cv2

img = cv2.imread('BeesWithPollen.jpeg')
img2 = cv2.imread('BeesWithPollen_copy.jpeg')

print(f'shape: {img.shape}')  # returns a tuple of number of rows, columns, and channels
print(f'size: {img.size} pixels')  # returns total number of pixels is accessed
print(f'datatype: {img.dtype}')  # returns image datatype is obtained
b, g, r = cv2.split(img)
img = cv2.merge((b, g, r))

pollen = img[280:340, 330:390]
img[273:333, 100:160] = pollen

img = cv2.resize(img, (512, 512))
img2 = cv2.resize(img2, (512, 512))

# dst = cv2.add(img, img2)
dst = cv2.addWeighted(img, .2, img2, .8, 0.0)

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
