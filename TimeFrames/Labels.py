import mediapipe as mp
import cv2
import csv
import os
import pandas as pd
import numpy as np
import pickle

mp_draw  = mp.solutions.drawing_utils
mp_hands = mp.solutions.hands

capture = cv2.VideoCapture(0)
with mp_hands.Hands(min_detection_confidence=0.5, min_tracking_confidence=0.5, max_num_hands=10) as hands:
    while capture.isOpened():
        success, image = capture.read()

        # Flip the image (initially the color space is BGR)
        image = cv2.flip(cv2.cvtColor(image, cv2.COLOR_BGR2RGB), 1)

        # image.flags.writable trick is used to improve algorithn performace
        image.flags.writeable = False
        results = hands.process(image)
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        image_height, image_width, _ = image.shape

        #For basic hand color-coding
        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_draw.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        # # For custom hand colors
        # if results.multi_hand_landmarks:
        #     for num, hand in enumerate(results.multi_hand_landmarks):
        #         mp_draw.draw_landmarks(image, hand, mp_hands.HAND_CONNECTIONS, mp_draw.DrawingSpec(color=(0,255,0), thickness=5, circle_radius=5),
        #         mp_draw.DrawingSpec(color=(186,235,52), thickness=4, circle_radius=5))

        try:

            num_coordinates = len(hand_landmarks.landmark)

            # print(num_coordinates)
            # prints the total length of the number of coodinates
            # in MediaPipe total is 21
            # export the coordinates to CSV as x,y,z

            landmarks = ['class']
            for val in range(num_coordinates+1):
                landmarks += ['x{}'.format(val), 'y{}'.format(val), 'z{}'.format(val)]
            
            #print(landmarks)
            #prints all hand coordinates as x,y,z

            with open('hand_coordinates.csv', mode='w', newline='') as f:
                csv_writer = csv.writer(f, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                csv_writer.writerow(landmarks)

            class_name = 'Hand Coordinates'

            hand = hand_landmarks.landmark
            hand_row = list(np.array([[landmark.x, landmark.y, landmark.y, landmark.z] for landmark in hand]).flatten())

            row = hand_row

            row.insert(0, class_name)

            with open('hand_coordinates.csv', mode = 'a', newline = '') as f:
                csv_writer = csv.writer(f, delimiter = ',', quotechar = '"', quoting = csv.QUOTE_MINIMAL)
                csv_writer.writerow(row)

        except:
            pass

        cv2.imshow('Labels', image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

capture.release()