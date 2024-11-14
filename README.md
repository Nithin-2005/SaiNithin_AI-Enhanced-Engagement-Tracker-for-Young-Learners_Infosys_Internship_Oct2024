# SaiNithin_AI-Enhanced-Engagement-Tracker-for-Young-Learners_Infosys_Internship_Oct2024

infosys spring bord internship
Image Processing 

Libraries or Frame Works used - opencv 

Version - 4.10.0.84 

Developed Logics -

A) image_concatenation:- This resizes two images, to given trange of pixels and combines them both horizontally and vertically. Using np.hstack() and np.vstack(), the images are concatenated side-by-side and one on top of the other, respectively. The concatenated results are displayed in separate windows.

Input :-
![image](https://github.com/user-attachments/assets/34d5a2e4-86b7-44bc-b7d0-99610038a1da)

![image](https://github.com/user-attachments/assets/8f759da2-ee5c-43d7-a64a-5034b9c367ca)



Output :- 

![image](https://github.com/user-attachments/assets/ef0ca8f1-6af9-4960-b67f-6987dd471f7f)
![image](https://github.com/user-attachments/assets/282b0e32-22fa-4ce9-b999-933075ead530)




B) image_contour :- This detects contours in a grayscale image. First, it applies a binary threshold to the image to separate foreground from background. Then, it finds contours using cv2.findContours() and draws them onto the original image in green. The result, with highlighted contours, is displayed in a separate window.

Input :- 

![image](https://github.com/user-attachments/assets/a3156655-07fa-4bfb-acb0-265dc2b9312c)


Output :- 

![image](https://github.com/user-attachments/assets/c17d8d70-d5a1-4dc7-a29a-6874c998e14e)



C) image_crop :- It extracts a specific region from the original image, defined by the pixel range, and displays the cropped section in a separate window.

Input :-

![image](https://github.com/user-attachments/assets/42670ff2-ff27-47cb-bb0d-66bd82b86326)




Output :- 

![image](https://github.com/user-attachments/assets/2efd283a-dced-4835-97a9-2bda30f5ac59)



D) image_dilation & erosion :- A kernel matrix is used to perform dilation and erosion, which enhance and reduce certain features of the image, respectively. The results of these morphological operations, dilated and eroded images, are displayed in separate windows.

Input :- 

![image](https://github.com/user-attachments/assets/c8dbf563-c1e6-4723-bf19-6d465c3bb8d0)



Output :- 

![image](https://github.com/user-attachments/assets/a9c50ab2-6189-4647-a566-6c546819992a)
![image](https://github.com/user-attachments/assets/8e2d2076-8dac-4549-8e77-a5806c730eee)




E) image_edge detection:- This detects edges in a grayscale image using the **Canny edge detection** algorithm. The `cv2.Canny()` function is applied with threshold values of 100 and 200 to identify edges in the image. The resulting edge-detected image is displayed in a separate window.

Input :- 

![image](https://github.com/user-attachments/assets/ab924a84-f19a-4ed0-9f21-28017987de73)



Output :- 

![image](https://github.com/user-attachments/assets/74ec2a35-a138-46b5-9d81-b423f404cbd6)




F) image_histogram_equalization :- This performs **histogram equalization** on a grayscale image to improve the contrast of the image. The `cv2.equalizeHist()` function enhances the image by redistributing the intensity values across the full range, making the dark areas brighter and the bright areas darker. The resulting equalized image is displayed in a separate window.

Input :-

![image](https://github.com/user-attachments/assets/52480a03-6500-4189-8d02-9cd6833eca8e)



Output :- 

![image](https://github.com/user-attachments/assets/c1a62ddd-a9ef-479a-b095-ff1f3acbcd77)



G) image_hsv :- This converts a color image from the BGR color space (used by OpenCV) to the HSV color space using the `cv2.cvtColor()` function. The result is displayed in a separate window, where the image is represented in Hue, Saturation, and Value (HSV) instead of the standard Blue, Green, Red (BGR) format.

Input :- 

![image](https://github.com/user-attachments/assets/20e0bcf5-d6e4-46bc-b892-1724f06b25d2)



Output :- 

![image](https://github.com/user-attachments/assets/e617fad2-0cd4-4574-84db-9fb40b3f8245)



H) image_morphological_transformation :- This applies morphological operations, opening, and closing, to a grayscale image to process noise and gaps. `Opening` (erosion followed by dilation) removes small noise from the image, while `Closing` (dilation followed by erosion) fills small holes or gaps. The processed images are displayed in separate windows, showing the effects of noise removal and gap filling.

Input :- 

![image](https://github.com/user-attachments/assets/e94f2216-8f94-49bf-8253-80ed642723e0)



Output :- 

![image](https://github.com/user-attachments/assets/3f798323-4130-43f0-80d6-0ffcad8e82f8)
![image](https://github.com/user-attachments/assets/b2f2e9f2-35b6-4226-ad24-d0f688c3b0eb)



I) image_resize :- This resizes an input image, to the dimensions of a given range of pixels. The resized image is then displayed in a separate window.

Input :- 

![image](https://github.com/user-attachments/assets/1971ea47-027b-405a-81fa-ea52a9706d08)



Output :- 

![image](https://github.com/user-attachments/assets/73cfc0a2-c8e2-406a-bb04-08f8fb049ff3)



J) image_rgb2gray :- This converts a color image to grayscale using `cv2.cvtColor()` and saves the grayscale version image. The grayscale image is then displayed in a separate window.

Input :- 

![image](https://github.com/user-attachments/assets/6b262f14-d5cc-487d-9c2f-e2b126c5a893)



Output : - 

![image](https://github.com/user-attachments/assets/f1635591-4955-43f9-85b3-c91a666716a7)




K) image_rotate :- This rotates an image by 90 degrees around its center. It first calculates the center point and then creates a rotation matrix with a 90-degree angle. Using `cv2.warpAffine()`, the image is rotated and displayed in a separate window. 

Input :- 

![image](https://github.com/user-attachments/assets/ccc00cc6-0ef3-4751-bacf-442ed35be0c2)



Output :- 

![image](https://github.com/user-attachments/assets/e77748ce-7da7-40fa-81f5-c0cae10e9b6f)



L) image_blur :- This code applies a Gaussian blur to an image using a 15x15 kernel size, which helps in reducing image noise and detail. The blurred image is then displayed in a separate window.

Input :- 

 ![image](https://github.com/user-attachments/assets/5434ec70-2b3f-49b1-a121-537aa19a43c2)



Output :- 

![image](https://github.com/user-attachments/assets/0a2acfec-0e84-416a-a83d-cb7d24e51b7b)




#### M) `image_noise_removal & closing_gaps`
This function removes noise and fills gaps using morphological operations.

#### N) `image_template`
This function performs template matching to locate a template image within a larger image.

## Video Processing

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84

### Developed Logics:

#### A) `Video_multivideo`
This function reads and displays images from a specified folder, printing the dimensions of each image.

#### B) `Video_fps`
This function captures video from the webcam, displays it in real-time, and calculates the FPS.

#### C) `Video_save`
This function captures live video and saves it to a specified output file.

#### D) `Video_stack`
This function reads and resizes two video files, concatenating them horizontally.

#### E) `Video_stream`
This function captures live video from the webcam and displays it in real-time.

## Annotations

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6

### Developed Logics:

#### A) `data_segregate`
This function organizes images and their label files into matched and unmatched directories.

- **Input:**

![image](https://github.com/user-attachments/assets/6633ef0d-2652-429c-9179-30e76c634c63)



- **Output:**

![image](https://github.com/user-attachments/assets/771e1027-e364-4a9c-9892-f0b5edead711)



#### B) `label`
This function draws bounding boxes on images based on annotations in the label files.

- **Input:**
![image (1)](https://github.com/user-attachments/assets/0c228a17-beeb-41b6-9794-c74161cc3f9a)



- **Output:**

![image](https://github.com/user-attachments/assets/3b6acc6c-3a1f-45ab-a31b-70534573c4f0)



#### C) `label_manipulate`
This function updates class numbers in label files for object detection tasks.

- **Input:**

![image (2)](https://github.com/user-attachments/assets/bf6ed5bb-6a05-44c9-a46d-1e76e7f7922e)




- **Output:**

![image (3)](https://github.com/user-attachments/assets/f092a66d-ba9f-41b2-a3d8-8d878eca49e6)



