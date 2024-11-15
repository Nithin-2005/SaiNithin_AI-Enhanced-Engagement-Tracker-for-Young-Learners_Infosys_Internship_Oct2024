import cv2

img = cv2.imread("C:/Users/nithi/OneDrive/Desktop/Infosys Springboard/Infosys Springboard/Image_processing/image1.jpg", 0)
equalized = cv2.equalizeHist(img)

cv2.imshow('Equalized Image', equalized)
cv2.waitKey(0)
cv2.destroyAllWindows()
