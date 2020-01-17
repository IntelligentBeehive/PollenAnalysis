import numpy as np
import cv2

events = [i for i in dir(cv2) if 'EVENT' in i]
print(events)


def click_event(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        # ### put text in image ###
        # print(f'{x}, {y}')
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # strXY = f'{x}, {y}'
        # cv2.putText(img, strXY, (x, y), font, 1, (255, 225, 0), 2)
        # cv2.imshow('image', img)
        # ###
        # ### right button down event ###
        # if event == cv2.EVENT_RBUTTONDOWN:
        #     blue = img[y, x, 0]
        #     green = img[y, x, 1]
        #     red = img[y, x, 2]
        #     font = cv2.FONT_HERSHEY_SIMPLEX
        #     strBGR = f'{blue}, {green}, {red}'
        #     cv2.putText(img, strBGR, (x, y), font, 1, (0, 225, 255), 2)
        #     cv2.imshow('image', img)
        # ###
        # ###
        # cv2.circle(img, (x, y), 3, (0, 0, 255), -1)
        # points.append((x, y))
        # if len(points) >= 2:
        #     cv2.line(img, points[-1], points[-2], (255, 0, 0), 5)
        # cv2.imshow('image', img)
        # ###

        blue = img[x, y, 0]
        green = img[x, y, 1]
        red = img[x, y, 2]
        my_color_image = np.zeros((512, 512, 3), np.uint8)
        my_color_image[:] = [blue, green, red]
        cv2.imshow('color', my_color_image)


# img = np.zeros((512, 512, 3), np.uint8)
img = cv2.imread('BeesWithPollen.jpeg')
cv2.imshow('image', img)
points = []
cv2.setMouseCallback('image', click_event)

cv2.waitKey(0)
cv2.destroyAllWindows()
