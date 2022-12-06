import numpy as np
import mediapipe as mp
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
fig.subplots_adjust(left=0, right=1, bottom=0, top=1)

def body_plot(plt, ax, landmarks, visibility=0.5):
    landmark_set = []

    for index, landmark in enumerate(landmarks.landmark):
        landmark_set.append([landmark.visibility, (landmark.x, landmark.y, landmark.z)])

    # List of landmarks

    face_list = [0,1,2,3,4,5,6,7,8,9,10]

    left_arm_list = [11,13,15,17,19,21]

    right_arm_list = [12,14,16,18,20,22]

    shoulder_list = [11,12]

    waist_list = [23,24]

    face_x, face_y, face_z = [], [], []
    for index in face_list:
        point = landmark_set[index][1]
        face_x.append(point[0])
        face_y.append(point[2])
        face_z.append(point[1]) * (-1)

    left_arm_x, left_arm_y, left_arm_z = [], [], []
    for index in left_arm_list:
        point = landmark_set[index][1]
        left_arm_x.append(point[0])
        left_arm_y.append(point[2])
        left_arm_z.append(point[1]) * (-1)

    right_arm_x, right_arm_y, right_arm_z = [], [], []
    for index in right_arm_list:
        point = landmark_set[index][1]
        right_arm_x.append(point[0])
        right_arm_y.append(point[2])
        right_arm_z.append(point[1]) * (-1)

    shoulder_x, shoulder_y, shoulder_z = [], [], []
    for index in left_arm_list:
        point = landmark_set[index][1]
        shoulder_x.append(point[0])
        shoulder_y.append(point[2])
        shoulder_z.append(point[1]) * (-1)

    waist_x, waist_y, waist_z = [], [], []
    for index in left_arm_list:
        point = landmark_set[index][1]
        left_arm_x.append(point[0])
        left_arm_y.append(point[2])
        left_arm_z.append(point[1]) * (-1)

    ax.cla()
    ax.set_xlim3d(-1,1)
    ax.set_ylim3d(-1,1)
    ax.set_zlim3d(-1,1)

    ax.scatter(face_x, face_y, face_z)
    ax.plot(right_arm_x, right_arm_y, right_arm_z)
    ax.plot(left_arm_x, left_arm_y, left_arm_z)
    ax.plot(shoulder_x, shoulder_y, shoulder_z)
    ax.plot(waist_x, waist_y, waist_z)

    return fig