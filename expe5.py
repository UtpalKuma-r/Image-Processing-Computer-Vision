import cv2
import numpy as np

original = cv2.imread('images/edge.jpeg')
cv2.imshow('Original', original)

#--------------------<Canny Edge Detection>--------------------#
edges = cv2.Canny(original,100,200)
cv2.imshow('Edge', edges)

#--------------------<Threshold-Based Image Segmentation>--------------------#
gray = cv2.cvtColor(original, cv2.COLOR_BGR2GRAY)
# Apply thresholding
ret, thresh = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
# Display thresholded image
cv2.imshow('thresholded', thresh)

#--------------------<Region-Based Image Segmentation>--------------------#
def region_growing(img, seed, threshold = 20):
    height, width =img.shape
    print(img.shape)
    mask = np.zeros((height, width), dtype=np.uint8)
    seed_value = img[seed[1], seed[0]]
    to_process = [seed]
    while to_process:
        x, y = to_process.pop()
        if mask[y, x] == 0:
            mask[y, x] = 255
            for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1), (-1, -1), (-1, 1), (1, -1), (1, 1)]:
                nx, ny = x+dx, y+dy
                if 0<=nx<width and 0<=ny <height:
                    if mask[ny, nx] == 0 and abs(int(img[ny, nx]) - int(seed_value)) < threshold:
                        to_process.append((nx, ny))
    return mask

img = cv2.imread('images/edge.jpeg', cv2.IMREAD_GRAYSCALE)
seed = (150, 80)
segmented_region = region_growing(img ,seed, threshold=30)
# cv2.imshow('original', original)
cv2.imshow('Segmented Region', segmented_region)


cv2.waitKey(0)
cv2.destroyAllWindows()