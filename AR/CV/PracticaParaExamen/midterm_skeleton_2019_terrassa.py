########################################################################
#                         CHRISTIAN MARTINEZ
########################################################################

import cv2
import numpy as np

def exercise1():
    img = cv2.imread("PracticaParaExamen/bart.jpg", cv2.IMREAD_COLOR)

    # TODO: Write your code here
    img = img / 255
    height, width, depth = img.shape

    #create kernel
    kernel = np.array([[1,4,6,4,1],[4,16,24,16,4],[6,24,36,24,6],[4,16,24,16,4],[1,4,6,4,1]]) / 256 #todo create automatically

    #frame
    ksize , _ = kernel.shape
    krad = int(ksize*0.5)
    frame = np.zeros((height + 2*krad, width + 2*krad, depth))
    frame[krad:-krad, krad:-krad] = img

    filtered = np.zeros(img.shape)

    #convolution
    for i in range(0, height):
        for j in range(0, width):
            filtered[i, j] = (frame[i:i+ksize, j:j+ksize] * kernel[:, :, np.newaxis]).sum(axis=(0, 1))
    
    cv2.imshow("Filter", filtered)
    cv2.imshow("Original", np.uint8(img*255))
    cv2.waitKey(0)

def Erosion(img, kernel, times):
    ksize, _ = kernel.shape
    krad = int(ksize * 0.5)

    height, width = img.shape

    framed = np.zeros((height + 2*krad, width + 2*krad))
    framed[krad:-krad, krad:-krad] = img

    filtered = np.zeros(img.shape)

    for t in range(times):
        for i in range(0, height):
            for j in range(0, width):
                all_1 = True
                for x in range(-1, 1):
                    for y in range(-1, 1):
                        if framed[i + x, j + y] != 1:
                            all_1 = False
                if all_1:
                    filtered[i, j] = 1
                else:
                    filtered[i, j] = 0
        framed[krad:-krad, krad:-krad] = filtered
    return filtered

def Dilation(img, kernel, times):
    ksize, _ = kernel.shape
    krad = int(ksize * 0.5)

    height, width = img.shape

    framed = np.zeros((height + 2*krad, width + 2*krad))
    framed[krad:-krad, krad:-krad] = img

    filtered = np.zeros(img.shape)

    for t in range(times):
        for i in range(0, height):
            for j in range(0, width):
                a_1 = False
                for x in range(-1, 1):
                    for y in range(-1, 1):
                        if framed[i + x, j + y] == 1:
                            a_1 = True
                if a_1:
                    filtered[i, j] = 1
                else:
                    filtered[i, j] = 0

        framed[krad:-krad, krad:-krad] = filtered
    return filtered


def exercise2():
    img = cv2.imread("PracticaParaExamen/binary.png", cv2.IMREAD_GRAYSCALE)
    img = img/255
    # TODO: Write your code here
    kernel = np.ones(shape=(3,3))
    

    cv2.imshow('cv2', cv2.erode(img, kernel, 0))
    cv2.imshow('Erosion', Dilation(Erosion(img, kernel, 2), kernel, 6)*255)

    cv2.imshow("Binary", img)
    cv2.waitKey(0)


if __name__ == '__main__':

    # Uncomment to execute exercise 1
    # exercise1()

    # Uncomment to execute exercise 2
    exercise2()

    pass
