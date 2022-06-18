import cv2 as cv
import math
import numpy as np

low_bound, high_bound = (0, 0, 221), (180, 30, 255)
k_thres_ = 0.2


def preprocess(image):
    image = image[512:, :]
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    mask = cv.inRange(hsv, low_bound, high_bound)
    mask = cv.bitwise_not(mask)
    kernel = cv.getStructuringElement(cv.MORPH_RECT, (3, 3), (-1, -1))
    mask = cv.dilate(mask, kernel)
    mask = cv.erode(mask, kernel)
    return image, mask


def calculate_ratio(a, b):
    if abs(b[0][0] - a[0][0]) < 1e-3:
        if a[0][0] == 0 or a[0][0] == 1919:
            return 0
        else:
            return 999
    else:
        return (b[0][1] - a[0][1]) / (b[0][0] - a[0][0])


def get_distance(a, b):
    distance = pow(a[0][0] - b[0][0], 2) + pow(a[0][1] - b[0][1], 2)
    return math.sqrt(distance)


def set_point(p_vector, p):
    if len(p_vector) < 2:
        p_vector.append(p[:])
    else:
        if p[1] < p_vector[0][1]:
            p_vector[0] = p[:]
        elif p[1] < p_vector[1][1]:
            p_vector[1] = p[:]


def get_corner_point(mask):
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)  # 找轮廓
    contours_poly = []
    up_corner = []
    for i, contour in enumerate(contours):
        contours_poly.append(cv.approxPolyDP(contour, 5, True))  # 拟合多边形
        if len(contours_poly[i]) < 4 or len(contours_poly[i]) > 7: continue  # 筛掉奇怪边形
        mask = cv.drawContours(image, contours_poly, i, (0, 0, 255), 1, 8)
        cv.imshow('mask', mask)
        cad_point = []
        # print(contours_poly[i])
        for j in range(len(contours_poly[i])):
            k = calculate_ratio(contours_poly[i][j], contours_poly[i][(j + 1) % len(contours_poly[i])])  # 算斜率找关键点
            if abs(k) > k_thres_ and get_distance(contours_poly[i][j],
                                                  contours_poly[i][(j + 1) % len(contours_poly[i])]) > 10:
                if contours_poly[i][j][0][1] < contours_poly[i][(j + 1) % len(contours_poly[i])][0][1]:
                    set_point(cad_point, contours_poly[i][j][0])
                else:
                    set_point(cad_point, contours_poly[i][(j + 1) % len(contours_poly[i])][0])
            else:
                print('k:', k)
        if len(cad_point) == 2:
            up_corner.append(cad_point[0])
            up_corner.append(cad_point[1])
            cv.circle(image, tuple(cad_point[0]), 3, (255, 255, 0), 3)
            cv.circle(image, tuple(cad_point[1]), 3, (255, 255, 0), 3)
    return up_corner


image = cv.imread('hw2021/28.png')
image, mask = preprocess(image)
cv.imshow('mask', mask)
up_corner = get_corner_point(mask)
# print(len(up_corner))
# cv.imshow('test', image)
cv.waitKey(0)
