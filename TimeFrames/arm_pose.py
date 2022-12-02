import cv2
import mediapipe as mp
import numpy as np

mp_draw = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose

capture = cv2.VideoCapture(0)
img = cv2.imread("body_landmarks.png", cv2.IMREAD_ANYCOLOR)

with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while capture.isOpened():
        ret, frame = capture.read()
        
        image = cv2.flip(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), 1)
        image.flags.writeable = False
        results = pose.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    
        try:
            landmarks = results.pose_landmarks.landmark
            
        except:
            pass

        # Detections
        mp_draw.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        #print(results.pose_landmarks, mp_pose.POSE_CONNECTIONS)
        cv2.imshow('Arm Positions', image)

        #print body landmark naming convention of MediaPipe
        cv2.imshow("Body Landmark Numbering", img)


        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows()

# Choose a body part from the landmark array
print(landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value])