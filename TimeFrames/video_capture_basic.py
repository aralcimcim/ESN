# cmd K + C shortcut comments on-off entire code blocks
# The first block of code just opens the webcam and exit on when # "q" is pressed.
# Shift + TAB unindents the entire code block

import mediapipe as mp
import cv2
import numpy as np
import time
import os

mp_drawing = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
mp_hands = mp.solutions.hands

### Works with that 0xFF TAKE A LOOK AT WHY IT IS SUPPOSED TO DO
### ACHTUNG ---> LANDMARKS ARE THE JOINTS

capture = cv2.VideoCapture(0)

# To calculate the FPS
previousTime = 0
currentTime = 0

# min_detection_confidence ranges in ([0.0, 1.0]) for the hand detection to be successful
with mp_holistic.Holistic(min_detection_confidence=0.8, min_tracking_confidence=0.5) as holistic:

    while capture.isOpened():
        ret, frame = capture.read()

        # Colorspace of the feed
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        # Mark image as not writable to improve performance
        image.flags.writeable = False

        # Detect
        results = holistic.process(image)
        image.flags.writeable = True

        print(results.left_hand_landmarks, results.right_hand_landmarks)
        
        # Change image color space to RGB
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        # Image, Landmarks, Connections
        # First argument is for the circle color
        # the second argument is for the line color

        # Draw the LEFT hand keypoints
        mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS,mp_drawing.DrawingSpec(color=(81,48,230), thickness=5, circle_radius=5),
        mp_drawing.DrawingSpec(color=(49,5,247), thickness=4, circle_radius=5),)

        # Draw the RIGHT hand keypoints
        mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS, mp_drawing.DrawingSpec(color=(0,255,0), thickness=5, circle_radius=5),
        mp_drawing.DrawingSpec(color=(186,235,52), thickness=4, circle_radius=5),
        )

        # Flip the image and resize
        image_flip = cv2.flip(image, 1)
        resize = cv2.resize(image_flip,(854,480))

        # Display the FPS on the screen
        currentTime = time.time()
        fps = 1 / (currentTime - previousTime)
        previousTime = currentTime
        cv2.putText(resize, str(int(fps)) + " FPS", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,140), 2)

        # Show the video feed
        cv2.imshow("Hand Joints v.01", resize)

        # Quit by pressing "q"
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()

### Until here the code detects x, y, z coordinates of both hands
