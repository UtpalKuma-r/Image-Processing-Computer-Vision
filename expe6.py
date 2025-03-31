import cv2
import numpy as np

image = cv2.imread('images/cartoon.jpeg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imshow("Original", image)

#--------------------<Erosion>--------------------#
eroded = ()
for i in range(0, 3):
    _ =  (cv2.erode(gray.copy(), None, iterations=i + 1), )
    eroded += _
cv2.imshow("Eroded images ({})".format(len(eroded)), np.hstack(eroded))

#--------------------<Dilation>--------------------#
dilated = ()
for i in range(0, 3):
    _ = (cv2.dilate(gray.copy(), None, iterations=i + 1),)
    dilated += _
cv2.imshow("Dilated images ({})".format(len(dilated)), np.hstack(dilated))

#--------------------<Opening>--------------------#
kernelSizes = [(3, 3), (5, 5), (7, 7)]
openings = ()
# loop over the kernels sizes
for kernelSize in kernelSizes:
# construct a rectangular kernel from the current size and then
# apply an "opening" operation
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    _ = (cv2.morphologyEx(gray, cv2.MORPH_OPEN, kernel),)
    openings += _
cv2.imshow("Openings images ({})".format(kernelSizes), np.hstack(openings))

#--------------------<Closing>--------------------#
closings = ()
for kernelSize in kernelSizes:
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    _ =  (cv2.morphologyEx(gray, cv2.MORPH_CLOSE, kernel),)
    closings += _
cv2.imshow("Closing images ({})".format(kernelSizes), np.hstack(closings))

#--------------------<Morphological gradient>--------------------#
gradient = ()
for kernelSize in kernelSizes:
# construct a rectangular kernel and apply a "morphological
# gradient" operation to the image
    kernel = cv2.getStructuringElement(cv2.MORPH_RECT, kernelSize)
    _ = (cv2.morphologyEx(gray, cv2.MORPH_GRADIENT, kernel),)
    gradient += _
cv2.imshow("Morphological gradient ({})".format(kernelSizes), np.hstack(gradient))

#--------------------<Top hat/white hat and black hat>--------------------#

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# construct a rectangular kernel (13x5) and apply a blackhat
# operation which enables us to find dark regions on a light
# background
rectKernel = cv2.getStructuringElement(cv2.MORPH_RECT, (13, 5))
blackhat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, rectKernel)
tophat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, rectKernel)
cv2.imshow("Black Hat\t\t\tTop Hat", np.hstack((blackhat, tophat)))

cv2.waitKey(0)
cv2.destroyAllWindows()