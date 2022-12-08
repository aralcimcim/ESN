import cv2
import numpy as np
import mediapipe as mp

mp_draw = mp.solutions.drawing_utils
mp_segment = mp.solutions.selfie_segmentation

# Gray Background
background = (192, 192, 192)
capture = cv2.VideoCapture(0)

# Set video parameters
width = int(capture.get(3))
height = int(capture.get(4))

# Use 0 to select the general model, and 1 to select the landscape model
with mp_segment.SelfieSegmentation(model_selection = 1) as selfie_segmentation:
  
  while capture.isOpened():
    success, image = capture.read()

    image = cv2.cvtColor(cv2.flip(image, 1), cv2.COLOR_BGR2RGB)

    image.flags.writeable = False
    results = selfie_segmentation.process(image)
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    cv2.imshow('Segmented Image', results.segmentation_mask)

    if cv2.waitKey(10) & 0xFF == ord('q'):
      break

capture.release()
cv2.destroyAllWindows





