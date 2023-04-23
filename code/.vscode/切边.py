import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


def findroi(src):
    orig = src.copy()
    gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
    blurred = cv.GaussianBlur(gray, (5, 5), 0)
    # eage = cv.Canny(blurred, 0, 50)
    ret, thresh = cv.threshold(blurred, 210, 255, cv.THRESH_BINARY_INV)
    image, contours, hierarchy = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
    cv.imshow("hao", image)
    contours = sorted(contours, key=cv.contourArea, reverse=True)
    cnt = contours[0]
    rect = cv.minAreaRect(cnt)
    degree = rect[2]
    box = cv.boxPoints(rect)
    box = np.int0(box)

    print([box], degree)
    rows, cols = image.shape
    image = cv.drawContours(image, [box], 0, (255, 255, 255), 10)
    M = cv.getRotationMatrix2D((cols/2, rows/2), degree, 1)
    dst = cv.warpAffine(src, M, (cols*2, rows*2))
    cv.imshow("image", image)
    cv.imshow("dst", dst)
    box = np.float32(box)
    a, b, c, d = box[0], box[1], box[2], box[3]
    pst1 = np.float32([b, c, a, d])
    pts2 = np.float32([[0, 0], [300, 0], [0, 500], [300, 500]])
    print(pst1, pts2)
    M2 = cv.getPerspectiveTransform(pst1, pts2)
    dst2 = cv.warpPerspective(orig, M2, (300, 450))

    cv.imshow("dst2", dst2)


src1 = cv.imread("C:/123.png")

cv.namedWindow("brain", cv.WINDOW_NORMAL)

cv.imshow("brain", src1)

# cv.namedWindow("output", cv.WINDOW_NORMAL)

findroi(src1)

cv.waitKey(0)
cv.destroyAllWindows()
