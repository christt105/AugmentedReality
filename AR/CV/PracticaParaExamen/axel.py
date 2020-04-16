import numpy as np
import cv2

def boxFilter(img):
    #normalize for better calculations as float
    img = img/255.0

    #kernel
    ksize = 11
    krn = np.zeros((ksize,ksize))
    krn[:,:]= 1.0/(ksize*ksize)

    #filter
    filtered = convolve(img,krn)

    return filtered

def gaussianFilter(img, radius):
    #normalize for better calculations as float
    img = img/255.0

    krn = gaussianKernel(radius)

    #filter
    filtered = convolve(img,krn)

    return filtered


def convolve(img, krn):
    #kernel
    ksize, _ = krn.shape
    krad = int(ksize/2)

    #frame
    height, width = img.shape
    framed = np.ones((height + 2*krad, width + 2*krad))
    framed[krad:-krad, krad:-krad] = img

    #filter
    filtered = np.zeros(img.shape)
    for i in range (0,height):
        for j in range(0, width):
            filtered[i,j] = (framed[i:i+ksize, j:j+ksize]*krn[:,:]).sum(axis=(0,1))
    
    return filtered

def gaussianKernel(krad):
    sigma = krad/3
    ksize = krad*2 + 1
    krn = np.zeros((ksize,ksize))
    for i in range (0, ksize):
        for j in range (0,ksize):
            distance = np.sqrt((krad - i)**2)+((krad - j)**2) #5HEAD
            krn[i,j] = np.exp(-distance**2 / (2*sigma**2))
    return krn/krn.sum()

def bilateralKernel(krad, img, px, py, sigmaColor):
    sigma = krad/3
    ksize = krad*2 + 1
    krn = np.zeros((ksize, ksize))
    for i in range (0, ksize):
        for j in range (0, ksize):
            neighbour_x = px - (krad - i)
            neighbour_y = py - (krad - j)
            if neighbour_x >= len(img):
                neighbour_x -= len(img)
            if neighbour_y >= len(img[0]):
                neighbour_y -= len(img[0])

            distance = np.sqrt((krad - i)**2)+((krad - j)**2) #5HEAD   
            po_rgb = img[px][py]
            pn_rgb = img[neighbour_x][neighbour_y]
            po_intensity = (po_rgb.max()-po_rgb.min())/po_rgb.max()
            pn_intensity = (pn_rgb.max()-pn_rgb.min())/pn_rgb.max()
            c_range = pn_intensity - po_intensity

            #krn[i,j] =  np.exp(- distance**2 / (2*sigma**2) - c_range**2 / (2*sigmaColor**2))
            exp_1 = np.exp(- distance**2 / (2*sigma**2))
            exp_2 = np.exp(- c_range**2 / (2*sigmaColor**2))
            krn[i,j] = exp_1*exp_2

    return krn/krn.sum()

def bilateralFilter(img, krad, sigmaColor):
    img = img/255.0
    ksize = krad*2 + 1

    #frame
    height, width, depth = img.shape
    framed = np.ones((height + 2*krad, width + 2*krad, depth))
    framed[krad:-krad, krad:-krad] = img

    filtered = np.zeros(img.shape)
    for i in range (0,height):
        for j in range(0, width):
            krn = bilateralKernel(krad, img, i, j, sigmaColor)
            filtered[i,j] = (framed[i:i+ksize, j:j+ksize]*krn[:,:, np.newaxis]).sum(axis=(0,1))

    return filtered

def sobelOperator(img):
    gx = np.array([[-1, 0, 1],[-2, 0, 2],[-1, 0, 1]])
    gy = np.array([[-1, -2, -1],[0, 0, 0],[1, 2, 1]])

    filtered_x = convolve(img, gx)
    filtered_y = convolve(img, gy)

    filtered = np.sqrt(filtered_x**2 + filtered_y**2)

    return filtered/filtered.max(), filtered_x/filtered_x.max(), filtered_y/filtered_y.max()


def maxCheck0(gradients, i, j, width):
    neighbour_i = i
    neighbour_j = j - 1

    if neighbour_j < 0:
        neighbour_j = 0

    if(np.maximum(gradients[i,j], gradients[neighbour_i, neighbour_j]) != gradients[i][j]):
        return 0
    
    neighbour_j = j + 1
    if neighbour_j == width:
        neighbour_j = width - 1

    if(np.maximum(gradients[i,j], gradients[neighbour_i, neighbour_j]) != gradients[i][j]):
        return 0

    return gradients[i][j]

def maxCheck45(gradients, i, j, width, height):
    neighbour_i = i - 1
    neighbour_j = j + 1

    if neighbour_i < 0:
        neighbour_i = 0

    if neighbour_j == width:
        neighbour_j = width - 1

    if(np.maximum(gradients[i,j], gradients[neighbour_i, neighbour_j]) != gradients[i][j]):
        return 0
    
    neighbour_i = i + 1
    neighbour_j = j - 1

    if neighbour_j < 0:
        neighbour_j = 0

    if neighbour_i == height:
        neighbour_i = height - 1

    if(np.maximum(gradients[i,j], gradients[neighbour_i, neighbour_j]) != gradients[i][j]):
        return 0

    return gradients[i][j]

def maxCheck90(gradients, i, j, height):
    neighbour_i = i - 1
    neighbour_j = j

    if neighbour_i < 0:
        neighbour_i = 0

    if(np.maximum(gradients[i,j], gradients[neighbour_i, neighbour_j]) != gradients[i][j]):
        return 0
    
    neighbour_i = i + 1

    if neighbour_i == height:
        neighbour_i = height - 1

    if(np.maximum(gradients[i,j], gradients[neighbour_i, neighbour_j]) != gradients[i][j]):
        return 0

    return gradients[i][j]

def maxCheck135(gradients, i, j, width, height):
    neighbour_i = i + 1
    neighbour_j = j + 1

    if neighbour_i == height:
        neighbour_i = height - 1

    if neighbour_j == width:
        neighbour_j = width - 1

    if(np.maximum(gradients[i,j], gradients[neighbour_i, neighbour_j]) != gradients[i][j]):
        return 0
    
    neighbour_i = i - 1
    neighbour_j = j - 1

    if neighbour_j < 0:
        neighbour_j = 0

    if neighbour_i < 0:
        neighbour_i = 0

    if(np.maximum(gradients[i,j], gradients[neighbour_i, neighbour_j]) != gradients[i][j]):
        return 0

    return gradients[i][j]

def cannyEdgeDetector(img, minVal, maxVal):
    filtered = gaussianFilter(img, 2)
    filtered, gx, gy = sobelOperator(filtered)

    directions = gradientComputation(gx, gy)
    
    filtered = nonMaximumSupression(filtered, directions)
    filtered = hystersisThresholding(filtered, minVal, maxVal)


    return filtered


def gradientComputation(gx, gy):
    height, width = gx.shape
    filtered = np.zeros(gx.shape)

    for i in range (0,height):
        for j in range(0, width):
            angle = np.arctan2(gy[i,j], gx[i,j])
            angle = np.rad2deg(angle)
            if (angle > 0 and angle <= 22):
                angle = 0
            elif (angle > 22 and angle <= 67):
                angle = 45
            elif (angle > 67 and angle <= 112):
                angle = 90
            else:
                angle = 135

            filtered[i,j] = angle

    return filtered

def nonMaximumSupression(gradients, directions):
    height, width = gradients.shape
    filtered = np.zeros(gradients.shape)
    
    for i in range (0,height):
        for j in range(0, width):
            if (directions[i,j] == 0):
                filtered[i][j] = maxCheck0(gradients, i, j, width)
            elif (directions[i,j] == 45):
                filtered[i][j] = maxCheck45(gradients, i, j, width, height)
            elif (directions[i,j] == 90):
                filtered[i][j] = maxCheck90(gradients, i, j, height)
            else:
                filtered[i][j] = maxCheck135(gradients, i, j, width, height)


    return filtered

def hystersisThresholding(img, minVal, maxVal):
    height, width = img.shape
    filtered = np.zeros(img.shape)
    
    for i in range (0, height):
        for j in range(0, width):
            if(img[i][j] > maxVal):
                filtered[i][j] = 1
            elif(img[i][j] < minVal):
                filtered[i][j] = 0
            else:
                filtered[i][j] = 2

    #frame
    framed = np.ones((height + 2, width + 2))
    framed[1:-1, 1:-1] = filtered
    filtered_2 = filtered.copy()

    for i in range (0, height):
        for j in range(0, width):
            if(filtered[i][j] == 2):
                if(framed[i:i + 3, j:j + 3].any() == 1):
                    filtered_2[i][j] = 1
                else:
                    filtered_2[i][j] = 0
            
    return filtered_2


img = cv2.imread('perrete.jpg', 0)
ourcanny = cannyEdgeDetector(img, 0.2, 0.6)
cv2.imshow("MonkaW", ourcanny)

#cvcanny = cv2.Canny(img, 30, 150)
#cv2.imshow("MonkaW", cvcanny)

k = cv2.waitKey(0)

if k==27:
    cv2.destroyAllWindows()