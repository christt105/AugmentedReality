import cv2
import numpy as np

img = cv2.imread('hk.png', 1)
img = img/255

kernel = np.ones((5, 5))/25

rows, col, a = img.shape

imgf = np.zeros((rows, col))

for i in range(0, col):
    for j in range(0, rows):
        summ = np.zeros(3)
        for k in range(i - 5, i+5):
            for l in range(j - 5, j+5):
                summ += img[j, i]/25
        imgf[j, i] = summ.mean()

cv2.imshow('Hollow Knight', img)
cv2.imshow('Hollow filtered', imgf)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()