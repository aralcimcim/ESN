import mediapipe as mp
import numpy as np
import cv2
import csv

mp_hands = mp.solutions.hands
mp_draw = mp.solutions.drawing_utils
mp_holistic = mp.solutions.holistic
hands = mp_hands.Hands()

# Set O for the laptop webcam
capture = cv2.VideoCapture(0)

# Ask for participant number
part_num = input('What is the participant number?\n')
mov_type = input('What is the action type?\n')
side = input('Which side is being recorded?\n')

# Set hand points for tracking
with mp_holistic.Holistic(min_detection_confidence=0.5, min_tracking_confidence=0.5) as holistic:

    while capture.isOpened():
        ret, frame = capture.read()

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        image.flags.writeable = False

        results = hands.process(image)

        image.flags.writeable = True

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        if results.multi_hand_landmarks:
            for lms in results.multi_hand_landmarks:
                for id, lm in enumerate(lms.landmark):
                    print(id, lm)

                    # Write x,y,z coordinates to a .csv file as a column
                    col_names = ['id', 'x', 'y', 'z']
                    input_data = [id,lm]

                    file_name = f'/Users/capitan/Documents/ESN/TimeFrames/csv_out/{part_num}_{mov_type}_{side}.csv'

                    with open (file_name, 'a+', newline = "") as csvfile:
                        csv_writer = csv.writer(csvfile)
                        csv_writer.writerow(col_names)
                        csv_writer.writerows([[id,lm]])

                    # id O is the wrist
                    if id == 20:
                        # Convert decimal values to pixel values to draw a circle on any point
                        h, w, c = image.shape
                        cx, cy = int(lm.x * w) , int(lm.y * h)
                        cv2.circle(image, (cx, cy) , 25, (0,255,0), cv2.FILLED)

                mp_draw.draw_landmarks(image, lms, mp_hands.HAND_CONNECTIONS)

        # Flip the image & resize
        image_flip = cv2.flip(image, 1)
        resize = cv2.resize(image_flip, (854, 480))

        # Render the detected & highlighted points
        # Name the file after the participant number
        cv2.imshow('Participant Number_Action Type_Side: ' + part_num + '_' + mov_type + '_' + side, resize)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

capture.release()
cv2.destroyAllWindows