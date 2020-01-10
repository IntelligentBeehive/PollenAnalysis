import cv2
import numpy as np
import os


# create image file
def create_image():
    img = np.zeros((250, 500, 3), np.uint8)
    img = cv2.rectangle(img, (250, 0), (500, 250), (255, 255, 255), -1)
    cv2.imwrite(file, img)
    print(f'Image saved as {file}')


# file name
file = 'image_1.png'
# check if file exists
if not os.path.isfile(file):
    # file doesn't exist, then create image file
    create_image()

img1 = np.zeros((250, 500, 3), np.uint8)
img1 = cv2.rectangle(img1, (200, 0), (300, 100), (255, 255, 255), -1)
img2 = cv2.imread(file)

bitAnd = cv2.bitwise_and(img1, img2)
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)
bitNot1 = cv2.bitwise_not(img1)
bitNot2 = cv2.bitwise_not(img2)

bitNot = cv2.bitwise_not(cv2.imread('BeesWithPollen.jpeg'))

cv2.imshow('img1', img1)
cv2.imshow('img2', img2)
cv2.imshow('bitAnd', bitAnd)
cv2.imshow('bitOr', bitOr)
cv2.imshow('bitXor', bitXor)
cv2.imshow('bitNot1', bitNot1)
cv2.imshow('bitNot2', bitNot2)

cv2.imshow('bitNot', bitNot)

cv2.waitKey(0)
cv2.destroyAllWindows()
