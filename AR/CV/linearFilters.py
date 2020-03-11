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

img = cv2.imread('HollowKnight_SobelBLUE.png', 1)
imgf = boxFilter(img)

cv2.imshow('Hollow Knight', img)
cv2.imshow('Hollow filtered', imgf)

k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()
