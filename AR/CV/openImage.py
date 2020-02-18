import cv2
import numpy

img = cv2.imread('hk.png', 0)
cv2.imshow('Hollow Knight', img)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite('hk-grayscale.png', img)
    cv2.destroyAllWindows()