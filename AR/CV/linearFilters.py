import cv2
import numpy as np

# solucion de profe

def boxFilter(img):
    #normalize
    img = img / 255.0

    # kernel
    ksize = 3
    krn = np.zeros((ksize, ksize))
    krn[:, :] = 1.0 / (ksize * ksize)

    # filter
    filtered = convolve(img, krn)

    return filtered

def convolve(img, krn):
    #kernel
    ksize, _ = krn.shape
    krad = int(ksize/2)

    #frame
    height, width, depth = img.shape
    framed = np.ones((height + 2*krad, width + 2*krad, depth))
    framed[krad:-krad, krad:-krad] = img
    #filter
    filtered = np.zeros(img.shape)
    for i in range(0, height):
        for j in range(0, width):
            filtered[i, j] = (framed[i:i+ksize, j:j+ksize] * krn[:, :, np.newaxis]).sum(axis=(0, 1))
          # filtered[i, j, 0] = (framed[i:i+ksize, j:j+ksize, 0] * krn)
          # filtered[i, j, 1] = (framed[i:i+ksize, j:j+ksize, 1] * krn)
          # filtered[i, j, 2] = (framed[i:i+ksize, j:j+ksize, 2] * krn)
    
    return filtered

img = cv2.imread('noise.png', 1)
imgprofe = boxFilter(img)
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
cv2.imshow('Hollow filtered Profe', imgprofe)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
