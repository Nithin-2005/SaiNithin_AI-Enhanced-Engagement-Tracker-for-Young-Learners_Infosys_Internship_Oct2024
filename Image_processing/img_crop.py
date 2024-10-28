import cv2

img = cv2.imread("C:/Users/nithi/OneDrive/Desktop/Infosys Springboard/Infosys Springboard/Image_processing/image2.jpg")
cropped = img[50:200, 100:300]

cv2.imshow('Cropped Image', cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()