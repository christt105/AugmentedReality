import cv2
import numpy as np

def Sobel(img):
    #normalize
    img = img / 255.0

    # kernel x
    krnx = np.array([[-1, 0, 1],[-2, 0, 2], [-1, 0, 1]])

    # filter
    filteredx = convolve(img, krnx)

    # kernel y
    krny = np.array([[-1, -2, -1],[0, 0, 0], [1, 2, 1]])

    # filter
    filteredy = convolve(img, krny)

    res = np.sqrt(filteredy[:, :]**2 + filteredx[:, :]**2)

    return res

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

img = cv2.imread('hk.png', 1)
#imgbw = cv2.imread('hk.png', 0)
imgsobel = Sobel(img)
# imgsobelbw = Sobel(imgbw)

cv2.imshow('Hollow Knight Sobel', imgsobel)
#cv2.imshow('Hollow Knight Sobel stylized', imgsobel/imgsobel.max())
#cv2.imshow('Hollow Knight', img)

O = np.vstack([imgsobel, imgsobel/imgsobel.max()])

cv2.imshow('Stack', O)

k = cv2.waitKey(0)

#if k == 27:
#    cv2.destroyAllWindows()
if k == ord('s'):
    cv2.imwrite('HollowKnight_Sobel.png', imgsobel*255.0)
    cv2.imwrite('HollowKnight_Sobel_stylized.png', imgsobel/imgsobel.max()*255.0)
    cv2.imwrite('Vertical.png', O*255.0)
    #cv2.imwrite('HollowKnight.png', img)
    #cv2.imwrite('HollowKnightOP.png', OP)
    #cv2.destroyAllWindows()