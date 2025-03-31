import numpy as np
import pandas as pd
import cv2

original = cv2.imread('images/flowerThorn.jpeg', cv2.IMREAD_UNCHANGED)
cv2.imshow('original', original)

#--------------------<Domain Filter>--------------------#
domainFilter = cv2.edgePreservingFilter(original, flags=1, sigma_s=60, sigma_r=0.6)
cv2.imshow('Domain Filter',domainFilter)

#--------------------<Gaussian Blur Method>--------------------#
gaussBlur = cv2.GaussianBlur(original,(5,5),cv2.BORDER_DEFAULT)
cv2.imshow("Gaussian Smoothing",gaussBlur)

#--------------------<Gaussian Blur Method>--------------------#
kernel = np.ones((10,10),np.float32)/25
meanFilter = cv2.filter2D(original, -1, kernel)
cv2.imshow("Mean Filtered Image", meanFilter)

#--------------------<Gaussian Blur Method>--------------------#
medianFilter = cv2.medianBlur(original,5)
cv2.imshow("Median Filter", medianFilter)

#--------------------<Bilateral Filtering Techniques>--------------------#
bilFil = cv2.bilateralFilter(original, 60, 60, 60)
cv2.imshow("Bilateral Filter", bilFil)

#--------------------<Frequency Band Filtering Techniques>--------------------#
## For High Band Pass Filter
highPass = original - gaussBlur

## For Low Band Pass Filter
lowPass = cv2.filter2D(original, -1, kernel)
lowPass = original - lowPass

cv2.imshow("High Pass\t\t\t\t     Low Pass", np.hstack((highPass, lowPass)))

cv2.waitKey(0)
cv2.destroyAllWindows()