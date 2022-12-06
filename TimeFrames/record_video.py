import cv2

capture = cv2.VideoCapture(0)
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
size = (frame_width, frame_height)

# Enter participant number & action type
part_num = input('What is the participant number?\n')
side = input('Which side is being recorded?\n')
mov_type = input('What is the action type?\n')

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter(f'/Users/capitan/Documents/ESN/TimeFrames/recorded_out/{part_num}_{side}_{mov_type}.avi', fourcc, 20.0, size)

while True:
    # Capture the frame & flip
    ret, frame = capture.read()
    frame = cv2.flip(frame, 1)

    # Write the frame to the .avi file
    writer.write(frame)

    # Show the image with specific action / participant name
    cv2.imshow('Participant Number_Action Type_Side: ' + part_num + '_' + mov_type + '_' + side, frame)

    # Quit when the 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
         break

writer.release()
capture.release()
cv2.destroyAllWindows()