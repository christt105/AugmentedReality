import math
import cv2
import numpy as np


# EXERCISE 1 ###########################################################

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

def convolve(img, krn):
    #kernel
    ksize, _ = krn.shape
    krad = int(ksize * 0.5)

    #frame
    height, width, depth = img.shape
    framed = np.zeros((height + 2*krad, width + 2*krad, depth))
    framed[krad:-krad, krad:-krad] = img
    #filter
    filtered = np.zeros(img.shape)
    for i in range(0, height):
        for j in range(0, width):
            filtered[i, j] = (framed[i:i+ksize, j:j+ksize] * krn[:, :, np.newaxis]).sum(axis=(0, 1))
    
    return filtered

def exercise1():

    original = cv2.imread("trs_exercise1_image.png", cv2.IMREAD_COLOR)
    assert original is not None
    cv2.imshow("Original", original)

    mask = cv2.imread("trs_exercise1_mask.png", cv2.IMREAD_GRAYSCALE)
    assert mask is not None
    cv2.imshow("Mask", mask)

    # TO DO: Insert exercise 1 code here

    original = original / 255

    height, width, depth = original.shape # assuming original and mask have de same width and height
    krad = 9
    kernel = gaussianKernel(krad)

    img_gauss = convolve(original, kernel)
    result = np.zeros(img_gauss.shape)

    mask = mask / 255.0

    result = mask[:, :, np.newaxis] * original + (1 - mask[:, :, np.newaxis]) * img_gauss


    cv2.imshow("Result", result)

    cv2.waitKey(0)


# EXERCISE 2 ###########################################################

# Canny edge detector
# Step 1: Blur
# Step 2: Edge detection
# Step 3: Non-maximum suppression
# Step 4: Hysteresis thresholding


def blur(img):

    # Don't use this in exercise 1 (use your own Gaussian filter)
    blurred = cv2.GaussianBlur(img, (5, 5), 0.5)

    return blurred


def sobel(img):

    # Using OpenCV
    G_x = cv2.Sobel(img, cv2.CV_64F, 1, 0)
    G_y = cv2.Sobel(img, cv2.CV_64F, 0, 1)

    # Gradient magnitudes
    G = np.sqrt(G_x ** 2 + G_y ** 2)

    # Gradient angles
    dirs = np.arctan2(G_x, G_y)
    dirs = 360.0 * dirs / (2.0 * math.pi)

    # Force gradient angles to steps of 45 degrees
    dirs[dirs < 0.0] += 180
    dirs = np.uint8(np.round((dirs + 23) - np.mod((dirs + 23), 45)))

    return G, dirs

def non_maximum_suppression(gradients, dirs):

    res = np.zeros(gradients.shape)
    
    # TO DO: Insert non maximum suppression code here
    
    for i in range (0, gradients.shape[0]):
        for j in range(0, gradients.shape[1]):
            if (dirs[i,j] == 0 or dirs[i,j] == 180):
                res[i,j] = suppresion_0(gradients, i, j)
            elif (dirs[i,j] == 45):
                res[i,j] = suppresion_45(gradients, i, j)
            elif (dirs[i,j] == 90):
                res[i,j] = suppresion_90(gradients, i, j)
            elif (dirs[i,j] == 135):
                res[i,j] = suppresion_135(gradients, i, j)

    return res

def suppresion_0(gradients, i, j):
    ni = i
    nj = j

    if i != 0:
        ni = i - 1

    if(np.maximum(gradients[i,j], gradients[ni, nj]) != gradients[i, j]):
        return 0
    
    ni = i + 1

    if ni == gradients.shape[0]:
        ni = gradients.shape[0] - 1

    if(np.maximum(gradients[i,j], gradients[ni, nj]) != gradients[i, j]):
        return 0

    return gradients[i, j]

def suppresion_45(gradients, i, j):
    ni = i + 1
    nj = j + 1

    if ni == gradients.shape[0]:
        ni = gradients.shape[0] - 1

    if nj == gradients.shape[1]:
        nj = gradients.shape[1] - 1

    if(np.maximum(gradients[i, j], gradients[ni, nj]) != gradients[i, j]):
        return 0
    
    ni = i - 1
    nj = j - 1

    if nj < 0:
        nj = 0

    if ni < 0:
        ni = 0

    if(np.maximum(gradients[i, j], gradients[ni, nj]) != gradients[i, j]):
        return 0

    return gradients[i, j]

def suppresion_90(gradients, i, j):
    ni = i
    nj = j - 1

    if nj < 0:
        nj = 0

    if(np.maximum(gradients[i,j], gradients[ni, nj]) != gradients[i, j]):
        return 0
    
    nj = j + 1
    if nj == gradients.shape[1]:
        nj = gradients.shape[1] - 1

    if(np.maximum(gradients[i,j], gradients[ni, nj]) != gradients[i, j]):
        return 0

    return gradients[i,j]

def suppresion_135(gradients, i, j):
    ni = i - 1
    nj = j + 1

    if ni < 0:
        ni = 0

    if nj == gradients.shape[1]:
        nj = gradients.shape[1] - 1

    if(np.maximum(gradients[i, j], gradients[ni, nj]) != gradients[i, j]):
        return 0
    
    ni = i + 1
    nj = j - 1

    if nj < 0:
        nj = 0

    if ni == gradients.shape[0]:
        ni = gradients.shape[0] - 1

    if(np.maximum(gradients[i, j], gradients[ni, nj]) != gradients[i, j]):
        return 0

    return gradients[i, j]

def hysteresis_thresholding(img, thres_min, thres_max):

    # Mark non-edges, sure edges, and possible edges
    marks = img.copy()
    marks[img < thres_min] = 0
    marks[img > thres_max] = 255
    marks[np.logical_and(img >= thres_min, img <= thres_max)] = 127
    marks = np.uint8(marks)

    result = marks.copy()
    rows, cols = marks.shape

    for i in range(1, rows-1):
        for j in range(1, cols-1):
            if result[i, j] == 127:
                if marks[i-1:i+2, j-1:j+2].sum() > 0:
                    result[i, j] = 255
                else:
                    result[i, j] = 0

    return result


def canny(img, thres_min, thres_max):

    # Step 1: Gaussian blur
    blurred = blur(img)

    # Step 2: Edge detection
    gradient, directions = sobel(blurred)

    # Step 3: Non-maximum suppression
    maximum = non_maximum_suppression(gradient, directions)

    # Step 4: Hysteresis thresholding
    result = hysteresis_thresholding(maximum, thres_min, thres_max)

    return result


def exercise2():

    img = cv2.imread("trs_exercise2_image.png", cv2.IMREAD_GRAYSCALE)
    assert img is not None

    edges = canny(img, 125, 200)
    cv2.imshow("Canny", np.uint8(edges))

    # You can uncomment this to see the right result
    # edges2 = cv2.Canny(img, 125, 200)
    # cv2.imshow("Canny 2", np.uint8(edges2))

    cv2.waitKey(0)


# MAIN #################################################################

def main():
    exercise1()
    exercise2()

main()
