import cv2
import time

capture = cv2.VideoCapture(0)
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
size = (frame_width, frame_height)

# To calculate the FPS
previousTime = 0
currentTime = 0

# Enter participant number & action type & body side
part_num = input('What is the participant number?\n')
mov_type = input('What is the action type?\n')
side = input('Which side is being recorded?\n')

#Set the size
capture.set(3, 1280)
capture.set(4, 720)

# Set the video codec // add (640, 480) for setting size
fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter(f'/Users/capitan/Documents/ESN/TimeFrames/recorded_out/{part_num}_{mov_type}_{side}.avi', fourcc, 20.0, (1280, 720))

while True:
    # Capture the frame & flip
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)

    # Write the frame to the .avi file
    writer.write(frame)

    # Display the FPS on the screen
    currentTime = time.time()
    fps = 1 / (currentTime - previousTime)
    previousTime = currentTime
    cv2.putText(frame, str(int(fps)) + " FPS", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,140), 2)

    # Show the video with participant number, action type, and side of body    
    cv2.imshow('Participant Number_Action Type_Side: ' + part_num + '_' + mov_type + '_' + side, frame)

    # # Move the video to the center of the screen
    cv2.moveWindow('Participant Number_Action Type_Side: ' + part_num + '_' + mov_type + '_' + side, 80, 80)

    # Quit when the 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
         break

writer.release()
capture.release()
cv2.destroyAllWindows()