import cv2

#loading and displaying the image
flower = cv2.imread('images/flower.jpg') #color image
grayFlower = cv2.imread('images/flower.jpg',0) #gray image
cv2.imshow('flower', flower)
cv2.imshow('flower-gray', grayFlower)

#finding and displaying negative of an image
negative_flower = 255 - flower
negative_gray_flower = 255-grayFlower
cv2.imshow('negative_flower', negative_flower)
cv2.imshow('negative_flower_gray', negative_gray_flower)


#making the program wait for a key before treminating
cv2.waitKey(0)