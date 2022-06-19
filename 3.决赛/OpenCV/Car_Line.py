import cv2 as cv

# low_bound, high_bound = (0, 0, 221), (180, 30, 255)
low1, high1 = (0, 0, 180), (180, 255, 255)
low2, high2 = (0, 0, 221), (180, 30, 255)
low3, high3 = (0, 30, 180), (180, 255, 221)


def preprocess(image, low, high):
    image = image[512:, :]
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, low, high)
    mask = cv.bitwise_not(mask)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3))
    mask = cv.dilate(mask, kernel)
    mask = cv.erode(mask, kernel)
    return mask


image = cv.imread('pictures/10.png')

mask1 = preprocess(image, low1, high1)
cv.imshow('mask1', mask1)
mask2 = preprocess(image, low2, high2)
cv.imshow('mask2', mask2)
mask = cv.bitwise_xor(mask1, mask2)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (5, 5))
mask = cv.erode(mask, kernel)
mask = cv.erode(mask, kernel)

mask = cv.dilate(mask, kernel)

# cv.imshow('mask1',mask1)
# cv.imshow('mask2',mask2)
# mask3=preprocess(image,low3,high3)
cv.imshow('mask', mask)

cv.waitKey(0)
