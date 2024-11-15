import cv2 as cv
import face_recognition

# Load and encode the known image of Sai Nithin
known_image = face_recognition.load_image_file("C:/Users/nithi/OneDrive/Pictures/Camera Roll/WIN_20241107_19_04_38_Pro.jpg")
known_face_encoding = face_recognition.face_encodings(known_image, num_jitters=50, model='large')[0]

# Initialize the live camera feed
cam = cv.VideoCapture(0)
if not cam.isOpened():
    print("Error: Could not open camera.")
    exit()

# Confidence threshold
confidence_threshold = 0.6

# Start the live video feed
while True:
    ret, frame = cam.read()
    if not ret:
        print("Error: Could not read frame.")
        break

    # Detect faces and their encodings in the frame
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)

    # Flag for recognizing the target face
    is_recognized = False

    # Compare each detected face to the known face
    for face_encoding, face_location in zip(face_encodings, face_locations):
        distance = face_recognition.face_distance([known_face_encoding], face_encoding)[0]

        # Check if the distance is below the threshold
        if distance < confidence_threshold:
            is_recognized = True
            top, right, bottom, left = face_location
            cv.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
            cv.putText(frame, 'Nithin Talasu', (left, top - 10), cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)

    # Display 'Not Nithin Talasu' if no match is found
    if not is_recognized:
        cv.putText(frame, 'Not Nithin Talasu', (30, 55), cv.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

    # Show the frame
    cv.imshow('Face Recognition', frame)

    # Press 'q' to exit
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cam.release()
cv.destroyAllWindows()
