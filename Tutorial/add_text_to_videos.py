import cv2
import datetime

cap = cv2.VideoCapture(1)
print(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
print(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

# cap.set(3, 3000)
# cap.set(4, 3000)
#
# print(cap.get(3))
# print(cap.get(4))

while cap.isOpened:
    ret, frame = cap.read()
    if ret:

        text = f'Width: {str(cap.get(3))} Heigth: {str(cap.get(4))}'
        datet = str(datetime.datetime.now())
        font = cv2.FONT_HERSHEY_SIMPLEX
        cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, datet, (10, 100), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.imshow('frame', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()