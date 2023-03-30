import cv2
import numpy as np
cap = cv2.VideoCapture(0)
def mouse_callback(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        pixel_color = frame[y, x]
        square_size = 200
        square = np.zeros((square_size, square_size, 3), dtype=np.uint8)
        square[:] = pixel_color
        cv2.imshow('square', square)
cv2.namedWindow('frame')
cv2.setMouseCallback('frame', mouse_callback)

while True:
    ret, frame = cap.read()
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()