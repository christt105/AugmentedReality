import cv2
import numpy as np

def gaussianKernel(krad):
    sigma = krad / 3
    ksize = krad * 2 + 1
    krn = np.zeros((ksize, ksize))
    for i in range(0, ksize):
        for j in range(0, ksize):
            d = np.sqrt((krad - i)**2 + (krad - j)**2)
            krn[i, j] = np.exp(-(d**2 / (2*sigma**2)))

    krn /= krn.sum()
    return krn



img = cv2.imread('noise.png', 0)

krn = gaussianKernel(10)

cv2.imshow("kernel", krn*10000)
filtered = convolve(img, krn)
cv2.imshow('gaussian', filtered)


k = cv2.waitKey(0)

if k == 27:
    cv2.destroyAllWindows()