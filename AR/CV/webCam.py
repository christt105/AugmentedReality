import cv2
import numpy

dev = cv2.VideoCapture(0)

while True:
    ret, frame = dev.read()
    
    gray = cv2.cvtColor(frame, 1)
    gray = cv2.flip(gray,1)
    cv2.imshow('Video', gray)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

dev.release()
cv2.destroyAllWindows()