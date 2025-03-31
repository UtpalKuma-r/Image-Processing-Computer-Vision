import cv2
from matplotlib import pyplot as plt

rgb_img = cv2.imread('images/colour.jpeg')
# convert from RGB color-space to YCrCb
ycrcb_img = cv2.cvtColor(rgb_img, cv2.COLOR_BGR2YCrCb)
# equalize the histogram of the Y channel
ycrcb_img[:, :, 0] = cv2.equalizeHist(ycrcb_img[:, :, 0])
# convert back to RGB color-space from YCrCb
equalized_img = cv2.cvtColor(ycrcb_img, cv2.COLOR_YCrCb2BGR)
cv2.imshow('equalized_img', equalized_img)
cv2.imshow('original_img', rgb_img)
plt.hist(equalized_img.ravel(),256,[0,256])
# plt.hist(rgb_img.ravel(),256,[0,256])
plt.show()
cv2.waitKey(0)