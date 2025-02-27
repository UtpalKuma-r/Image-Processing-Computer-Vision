import cv2
import numpy as np

origenal = cv2.imread('images/feather.jpg', 0)
cv2.imshow('original_image', origenal)
width, height = origenal.shape
print(width, height)

#--------------------<Image Translation>--------------------#
Tx = 100
Ty = 0
Transformation_Matrix = np.float32([[1, 0, -Tx], [0, 1, Ty]])
transformed_image = cv2.warpAffine(origenal, Transformation_Matrix, origenal.shape[::-1])
cv2.imshow('Transformed_image', transformed_image)

#--------------------<Image Reflection>--------------------#
M_Horizontal = np.float32([[1,  0, 0], [0, -1, width], [0,  0, 1]])
M_Vertical = np.float32([[-1, 0, height], [0, 1, 0], [0, 0, 1]])

reflected_hor = cv2.warpPerspective(origenal, M_Horizontal, (int(height), int(width)))
reflected_ver = cv2.warpPerspective(origenal, M_Vertical, (int(height), int(width)))
cv2.imshow('ReflectedImageHor', reflected_hor)
cv2.imshow('ReflectedImageVer', reflected_ver)

#--------------------<Image Rotation>--------------------#
# M_Rotation = np.float32([[1,  0, 0], [0, -1, width], [0,  0, 1]])
img_rotation = cv2.warpAffine(origenal, cv2.getRotationMatrix2D((height/2, width/2), 30, 0.6), (height, width))
cv2.imshow('imgRotation', img_rotation)

#--------------------<Image Shrink>--------------------#
img_shrinked = cv2.resize(origenal, (200, 100), interpolation = cv2.INTER_AREA) 
cv2.imshow('imgShrinked', img_shrinked)

#--------------------<Image Enlarged>--------------------#
img_enlarged = cv2.resize(origenal, None, fx=1.5, fy=1.5, interpolation=cv2.INTER_CUBIC)
cv2.imshow('imgEnlarged', img_enlarged)

#--------------------<Image croped>--------------------#
cropped_img = origenal[0:150, 50:194]
cv2.imshow('imgCropped', cropped_img)

#--------------------<Image shearing>--------------------#
M_ShearingX = np.float32([[1, 0.5, 0], [0, 1, 0], [0, 0, 1]])
sheared_img = cv2.warpPerspective(origenal, M_ShearingX, (int(height*1.5), int(width*1.5)))
cv2.imshow('imgShearingX', sheared_img)

M_ShearingY = np.float32([[1, 0, 0], [0.5, 1, 0], [0, 0, 1]])
sheared_img = cv2.warpPerspective(origenal, M_ShearingY, (int(height*1.5), int(width*1.5)))
cv2.imshow('imgShearingY', sheared_img)


#making the program wait for a key before treminating
cv2.waitKey(0)
cv2.destroyAllWindows()