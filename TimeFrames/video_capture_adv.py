import mediapipe as mp
import cv2
import numpy as np
import matplotlib.pyplot as plt

mp_draw = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

# Show the MediaPipe hand joint numbering
img = cv2.imread("hand_landmarks.png", cv2.IMREAD_ANYCOLOR)

# Draw the joint points
capture = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.5) as hands:

  while capture.isOpened():
    ret, frame = capture.read()
    image = cv2.flip(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB), 1)
    image.flags.writeable = False
    results = hands.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    #print(results)

    if results.multi_hand_landmarks:
      for num, hand in enumerate(results.multi_hand_landmarks):
        mp_draw.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0,255,0), thickness=5, circle_radius=5),
        mp_draw.DrawingSpec(color=(186,235,52), thickness=4, circle_radius=5))

    cv2.imshow("Hand Joints with Labels", image)
    cv2.imshow("Hand Landmark Numbering", img)

    if cv2.waitKey(5) & 0xFF == ord('q'):
      break

capture.release()
cv2.destroyAllWindows