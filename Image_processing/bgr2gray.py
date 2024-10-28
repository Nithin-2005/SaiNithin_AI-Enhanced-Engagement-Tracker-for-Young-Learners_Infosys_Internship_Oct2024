import cv2
image = cv2.imread("C:/Users/nithi/OneDrive/Desktop/Infosys Springboard/Infosys Springboard/Image_processing/image2.jpg")
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
cv2.imwrite("C:/Users/nithi/OneDrive/Desktop/Infosys Springboard/Infosys Springboard/Image_processing/image2.jpg", gray_image)
cv2.imshow('Grayscale Image', gray_image)
cv2.waitKey(0)
cv2.destroyAllWindows()