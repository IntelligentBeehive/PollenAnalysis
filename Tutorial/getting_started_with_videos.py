import cv2

# VideoCapture's argument:
#   0 = use default front webcam
#   1 = use external webcam 1
#   file name = use movie file inside project
#   file path = use movie file outside project
cap = cv2.VideoCapture('25 bees with pollen entered.mp4')

# video frame sizes
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# FourCC, four character code - https://fourcc.org/
fourcc = cv2.VideoWriter_fourcc(*'XVID')

# VideoWriter's arguments:
#   file name for creating new movie
#   identifier for video codec
#   frame rate
#   video frame sizes: width and height
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (width, height))

# run loop
while cap.isOpened():
    # read frame from webcam
    ret, frame = cap.read()

    if ret:
        # write out frame
        out.write(frame)

        # turn in grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # show every frame in window with title 'frame'
        cv2.imshow('frame', gray)

        # stop loop by pressing key Q
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

        # stop loop by closing window
        if cv2.getWindowProperty('frame', 0) < 0:
            break
    else:
        break

# releasing capture and writer
cap.release()
out.release()

# close all related windows
cv2.destroyAllWindows()
