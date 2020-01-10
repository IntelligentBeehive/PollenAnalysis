import cv2

# image read's second argument:
#    1 = Load image in color
#    0 = Load image in grayscale
#   -1 = Load image as original
img = cv2.imread('BeesWithPollen.jpeg', 0)

# print image in matrix
print(img)

# show image in window
cv2.imshow('image', img)

# hold image in window until pressing key S or K, or until closing window
while True:
    k = cv2.waitKey(0) & 0xFF
    if k == ord('s') or k == ord('k'):
        break
    if cv2.getWindowProperty('image', 0) < 0:
        break

# save image as a new file because of pressed key S
if k == ord('s'):
    file = 'BeesWithPollen_copy.jpeg'
    cv2.imwrite(file, img)
    print(f'Saved as {file}')

# close all related windows
cv2.destroyAllWindows()
