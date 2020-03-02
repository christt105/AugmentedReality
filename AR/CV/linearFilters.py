import cv2
import numpy as np

img = cv2.imread('noise.png', 1)
img = img/255

kernel = np.ones((5, 5))/25

rows, col, a = img.shape

imgf = np.zeros((rows, col))
summ = np.zeros(9)

for i in range(1, rows - 1):
    for j in range(1, col - 1):
        summ[0] = img[i-1, j-1, 0]
        summ[1] = img[i, j-1,0]
        summ[2] = img[i+1, j-1,0]
        summ[3] = img[i-1, j,0]
        summ[4] = img[i, j,0]
        summ[5] = img[i+1, j,0]
        summ[6] = img[i-1, j+1,0]
        summ[7] = img[i, j+1,0]
        summ[8] = img[i+1, j+1,0]
        imgf[i, j] = summ.mean()

cv2.imshow('Hollow Knight', img)
cv2.imshow('Hollow filtered', imgf)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
