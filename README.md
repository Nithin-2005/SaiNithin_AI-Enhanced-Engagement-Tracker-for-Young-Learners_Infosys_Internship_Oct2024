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

![image](https://github.com/user-attachments/assets/149a405e-aaf4-43b2-8768-dad38679d1ef)




Output : - 

![image](https://github.com/user-attachments/assets/f1635591-4955-43f9-85b3-c91a666716a7)




K) image_rotate :- This rotates an image by 90 degrees around its center. It first calculates the center point and then creates a rotation matrix with a 90-degree angle. Using `cv2.warpAffine()`, the image is rotated and displayed in a separate window. 

Input :- 

![image](https://github.com/user-attachments/assets/a5b84ed0-7c40-4e84-a906-6de8fda60be1)




Output :- 

![image](https://github.com/user-attachments/assets/e77748ce-7da7-40fa-81f5-c0cae10e9b6f)



L) image_blur :- This code applies a Gaussian blur to an image using a 15x15 kernel size, which helps in reducing image noise and detail. The blurred image is then displayed in a separate window.

Input :- 

![image](https://github.com/user-attachments/assets/638efccf-f50f-4644-9b45-6f310a288d5c)




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



## Face Recognition

### Libraries or Frameworks Used:
- **OpenCV**: Version 4.10.0.84
- **LabelImg**: Version 1.8.6
- **dlib**: Version 19.24.6
- **face_recognition**: Version 1.3.0
- **imutils**: Version 0.5.4

### Developed Logics:

#### A) `Face_recognition`
This performs real-time face recognition to identify whether the person in live video frames a known image by comparing. His name is displayed if He/She is recognized; otherwise, "Not He/She" appears.

- **Input:**

![image](https://github.com/user-attachments/assets/e496c5f9-463e-4888-a543-7f3c156ba097)



- **Output:**

![image](https://github.com/user-attachments/assets/715020b2-ca3d-4a59-8365-b93a23438cd0)



#### B) `Attendence_save`
Using a live video stream, this performs real-time face recognition to identify He/She. When He/She's face is recognized, his/her name is displayed on the video feed, and the recognition event is logged with the date and time in an Excel file. After every 5 recognitions, the current log is saved to an Excel file, and the recognition counter and DataFrame are reset.

- **Input:**

![image](https://github.com/user-attachments/assets/a82028ec-12ac-4968-9507-f9b97dc48cb3)



- **Output:**

![Screenshot 2024-11-15 183555](https://github.com/user-attachments/assets/8860496e-9a93-4e9f-85c5-5311994642ba)



![image](https://github.com/user-attachments/assets/2bea5659-f059-4e59-80d8-e1fdb63d4e14)



#### C) `test`
This performs real-time face recognition to identify He/She in a live video feed, logging each recognition event with the date and time into an Excel file every 30 seconds. It tracks recognition intervals to avoid duplicate entries and displays He/She or "Not He/She" based on identification.

- **Input:**

![image](https://github.com/user-attachments/assets/8cb4a15b-0f56-4f71-924c-cc8cfd549b40)



- **Output:**

![Screenshot 2024-11-15 183555](https://github.com/user-attachments/assets/b909d555-7942-476f-aaf6-1ad401a704b0)



![image](https://github.com/user-attachments/assets/0b6b3996-f53c-45c2-a61e-97d8d73406c7)


#### D) `tools`
This performs real-time face recognition using the live camera feed to identify He/She. Each time a face is recognized, it records the name, date, and time in a data frame. Once a recognition count of 5 is reached, it saves the records to an Excel file, then resets the counter and DataFrame. It displays "He/She's name" or "Not He/She's name" over the video feed, and pressing 'q' exits the program with a final save of any remaining records.

- **Input:**

![image](https://github.com/user-attachments/assets/e070c031-26e9-4690-85d4-fa6c23253863)


- **Output:**

![Screenshot 2024-11-15 183555](https://github.com/user-attachments/assets/abd92242-6cd1-43fb-8773-a07357183186)



![image](https://github.com/user-attachments/assets/01e2673a-119e-4838-a7bd-d8a10567102c)




#### E) `excel_sc`
This is for face recognition with time-based logging looks well-structured and includes the logic to save screenshots and log attendance into an Excel file.

1. **Efficiency**: Resizing frames to 640x480 is good for speed. You can reduce the size further if needed.
2. **File Saving**: Screenshots are saved in `"Teja_screenshots(5)"`, and Excel is updated every 30 seconds.
3. **Recognition Timings**: Logs every 30 seconds for the same person and logs every 5 minutes to avoid multiple entries in short time frames.
4. **Error Handling**: Proper `try-except` block for handling errors.
5. **Termination**: Exits when the 'q' key is pressed.

- **Input:**

![image](https://github.com/user-attachments/assets/c4afc135-4a7a-4785-a00d-38b0305ea47b)



- **Output:**

![image](https://github.com/user-attachments/assets/bb6f7eb5-486a-4977-882b-42d951517ced)



![image](https://github.com/user-attachments/assets/93587ba6-36ec-4c26-8b47-4486b93268f9)



#### F) `excel_sc_dt`
This uses OpenCV and `face_recognition` to detect and recognize a specific face (His/Her's) from a webcam feed. Upon recognition, a screenshot is saved, and the attendance (name, date, time, screenshot path) is logged into an Excel file. The script processes every second frame, saves data every 30 seconds, and ensures attendance is only logged every 5 minutes for the same person. The attendance data is stored in a DataFrame and periodically exported to an Excel file.

Key Features:
- Real-time face detection and recognition
- Saves screenshots with timestamp
- Logs attendance to Excel every 30 seconds
- Avoids multiple logs within a 5-minute interval for the same person

- **Input:**

![image](https://github.com/user-attachments/assets/5697e3f2-f0c9-4e86-9fed-bc21722c0210)



- **Output:**

![Sai_Nithin_2024-11-15_18-50-57](https://github.com/user-attachments/assets/8417c92b-d8e6-4afc-af0e-cc50f7b3073e)




![Screenshot 2024-11-15 184749](https://github.com/user-attachments/assets/4e52a567-441e-4e0f-a595-819eab2e5738)



#### G) `landmark`
This code is a face recognition and attentiveness tracking system that operates in real time. Key functions include:

1. **Face Recognition**: Detects and recognizes "His/Her's face" from the camera using a pre-loaded image.
2. **Attentiveness Detection**: Uses facial landmarks and head pose estimation to assess if the subject is attentive.
3. **Logging**: Records each recognition event with a timestamp, attentiveness status, and screenshot in an Excel file, saving every 30 seconds.
4. **Live Feedback**: Displays "Attentive" or "Not Attentive" on the video feed along with facial landmarks.

The system continues until you press 'q' to exit.

- **Input:**

![image](https://github.com/user-attachments/assets/b90653f8-f4f2-4ecc-839a-fab0a777b18b)



- **Output:**

![Sai Nithin_2024-11-14_21-17-14](https://github.com/user-attachments/assets/292912e7-4f87-4d17-9b4c-311901cf2141)



![image](https://github.com/user-attachments/assets/b27e9f06-d78f-4273-b5e9-6cede61a8cd2)



#### H) `atten_score`
This script captures real-time webcam video to recognize "His/Her's face" and assess attentiveness based on head pose:

1. **Setup**: Loads His/Her's face data and initializes detectors.
2. **Face Recognition**: Compares detected faces with the known face, identifying if it's a match.
3. **Attentiveness Check**: Estimates head orientation (yaw/pitch) to compute an attentiveness score.
4. **Logging**: Logs details (name, date, time, attentiveness, screenshot) in an Excel file every 30 seconds if attentive.
5. **Display**: Shows video with face labels, attentiveness status, and facial landmarks. 

Exits on 'q' press, ensuring the final save to Excel.

- **Input:**

![image](https://github.com/user-attachments/assets/23432c08-e9b1-472a-be53-13f7e0d11f9b)



- **Output:**

![Sai Nithin_2024-11-14_19-07-24](https://github.com/user-attachments/assets/4393b77b-3c8a-4a61-9e26-f3d1e165ab41)



![image](https://github.com/user-attachments/assets/ce093544-ef33-44d8-8354-3a131de69c83)



#### I) `avg_atten_score`
This captures webcam video, performs face recognition for "His/Her's face," calculates attentiveness based on the head pose, and logs the data into an Excel file every 30 seconds. Here is a summary of its key actions:

1. **Face Recognition**: Uses `face_recognition` to identify "His/Her's face" by comparing face encodings.
2. **Head Pose Detection**: Calculates the head pose (yaw, pitch) using `dlib`'s facial landmark predictor to assess attentiveness.
3. **Attentiveness Calculation**: Computes an attentiveness score based on yaw and pitch, with values between 0 (not attentive) and 1 (fully attentive).
4. **Logging**: Every 30 seconds, the script saves recognized face data (name, date, time, attentiveness, attention score, and screenshot) into an Excel file.
5. **Display and Feedback**: Shows real-time video with facial landmarks, attentiveness status, and face bounding boxes.

The final output includes an Excel file with logged details and an average attentiveness score at the end of the session. The user can stop the video stream by pressing 'q'.

- **Input:**

![image](https://github.com/user-attachments/assets/b1723565-2e74-4bf2-927a-70c89a6a79d4)



- **Output:**

![Sai Nithin_2024-11-07_20-51-21](https://github.com/user-attachments/assets/86482a4e-b54c-468a-9886-4f9b826da29f)


![image](https://github.com/user-attachments/assets/2f09b946-719b-42da-9cd9-54756117a38c)

![image](https://github.com/user-attachments/assets/01174c4c-5454-40f2-9886-a70792f09b20)

