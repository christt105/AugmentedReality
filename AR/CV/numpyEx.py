import numpy as np
import cv2

# 1. Create a vector of 10 floats (zeros)
def e1():
    return np.zeros(10)

# 2. Create a vector of 10 float (zeros) whose 5th element is one
def e2():
    arr = e1()
    arr[5] = 1
    return arr

# 3. Create a vector of integers going from 10 to 49
def e3():
    return np.arange(10, 50)

# 4. Create a matrix of 3x3 floats going from 1 to 9
def e4():
    arr = np.arange(1,10)
    return arr.reshape(3,3)

# 5. Create a matrix of 3x3 floats going from 1 to 9 and flip it horizontally
def e5():
    return np.flip(e4(), 1)

# 6. Create a matrix of 3x3 floats going from 1 to 9 and flip it vertically
def e6():
    return np.flip(e4(), 0)

# 7. Create a 3x3 identity matrix
def e7():
    return np.identity(3)

# 8. Create a 3x3 matrix of random values
def e8():
    return np.random.random_sample((3,3))

# 9. Create a random vector of 10 numbers and compute the mean value
def e9():
    arr = np.random.randint(0, 100, 10)
    print('Mean = {}'.format(np.mean(arr)))
    return arr

# 10. Create a 10x10 array of zeros surrounded/framed by ones
def e10():
    arr = np.ones((10,10))
    arr[1:9,1:9] = 0 # arr[1:-1,1:-1] = 0
    return arr

# 11. Create a 5x5 matrix of rows from 1 to 5
def e11():
    arr = np.zeros((5,5))
    arr[:] = np.arange(1,6)
    return arr

# 12. Create an array of 9 random integers and reshape it to a 3x3 matrix of floats
def e12():
    arr = np.random.randint(0, 9, 9)
    arr.reshape((3,3))
    return arr.astype(float)

# 13. Create a 5x5 matrix of random values and subtract its average from it
def e13():
    arr = np.random.random_sample((5,5))
    print("Mean: {}".format(np.mean(arr)))
    return arr

# 14. Create a 5x5 matrix of random values and subtract the average of each row to each row
def e14():
    np.random.seed(123)
    arr = np.random.random_sample((5,5))
    for i in range(5):
        print("Mean{}: {}".format(i, np.mean(arr[i])))
    return arr

# 15. Create an array of 5x5 random values and return the value that is closer to 0.5
def e15():
    np.random.seed(123)
    arr = np.random.random_sample((5, 5))
    arr = arr.flatten()
    index = (np.abs(arr - 0.5)).argmin()
    return arr[index]
    
# 16. Make a 3x3 matrix of random numbers from 0 to 10 and count how many of them are > 5
def e16():
    np.random.seed(123)
    arr = np.random.randint(0, 11, (3, 3))
    return arr[arr > 5]

# 17. Create a horizontal gradient image of 64x64 that goes from black to white
def e17():
    img = np.zeros((64, 64), np.uint8)
    img[:] = np.arange(0, 255, 255/64)
    cv2.imshow('Degradado b/n', img)
    cv2.waitKey(0)
    
# 18. Create a vertical gradient image of 64x64 that goes from black to white
def e18():
    img = np.zeros((64, 64), np.float)
    c = np.arange(0.0, 64.0)
    print(c)
    c = c/64.0
    print(c)
    img[0, :] = c
    cv2.imshow('Degradado b/n', img)
    cv2.waitKey(0)
# 19. Create a 3-component white image of 64x64 pixels and set the blue component to zero
# (the result should be yellow)
# 20. Create a 3-component white image of 64x64 pixels, set the blue component of the
# top-left part to zero (the result should be yellow) and the red component of the
# bottom-right part to zero (the result should be cyan
# 21. Open an image and insert black horizontal scan lines at 50%
# 22. Open an image and insert black vertical scan lines at 50%
# 23. Open an image, convert it to float64, normalize it, darken it 50%, and show it

#print(e17())
e18()