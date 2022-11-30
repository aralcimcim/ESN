import cv2

capture = cv2.VideoCapture(0)
frame_width = int(capture.get(3))
frame_height = int(capture.get(4))
size = (frame_width, frame_height)

part_num = input('What is the participant number?\n')

fourcc = cv2.VideoWriter_fourcc(*'MJPG')
writer = cv2.VideoWriter(f'{part_num}.avi', fourcc, 20.0, size)

while True:
    # Capture the frame
    ret, frame = capture.read()

    # Write the frame to the .avi file
    writer.write(frame)

    # Show the image
    cv2.imshow('Recording Participant Number: ' + part_num, frame)

    # Quit when the 'q' key is pressed
    if cv2.waitKey(10) & 0xFF == ord('q'):
         break

writer.release()
capture.release()
cv2.destroyAllWindows()
    
