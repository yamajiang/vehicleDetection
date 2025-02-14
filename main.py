import cv2 
from ultralytics import YOLO
import torch
from collections import Counter

model= YOLO("yolov8x.pt")

# load in video by passing in video file name 
capture= cv2.VideoCapture("cars.mp4")

while True:
    # to read individual frame from video
    # store into two element tuple 
    is_frame, frame= capture.read()

    # make sure that the returned frame is valid
    if not is_frame:
        break

    # object detection save to results variable
    # if avaliable, use apple mps 
    if torch.backends.mps.is_available():
        results= model(frame, device= "mps")
    else: # else, use cpu
        results= model(frame)
    #print(results)

    all_detected_objects= []


    for result in results:
        # get xy coords of the bounding boxes of objects detected
        bboxes= result.boxes.xyxy.cpu().numpy().astype("int")
        # get ids
        class_ids= result.boxes.cls.cpu().numpy().astype("int")

        #store the detected objects
        detected_objects= [model.names[class_id] for class_id in class_ids]
        all_detected_objects.extend(detected_objects)

        print("Objects detected:", detected_objects)

        # draw box around detected objects and labels
        for bbox, class_id in zip(bboxes, class_ids):
            (x, y, x2, y2)= bbox
            label = model.names[class_id]

            # passing in the frame, top left point, bottom right point, color of rectangle, thickness of line
            cv2.rectangle(frame, (x,y), (x2,y2), (0, 255,0), 2)
            # print the objects detected on the frame
            cv2.putText(frame, label, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        object_counts= Counter(all_detected_objects)

        # display the object count in the frame
        y_offset = 50
        x_offset = 50
        for obj, count in object_counts.items():
            text= f"{obj}: {count}"
            #passing in frame, text, offset, font, font size, color, thickness
            cv2.putText(frame, text, (x_offset, y_offset), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            y_offset += 50


    # show frame on screen
    cv2.imshow("Video", frame)

    # block execution till a key is pressed on the keyboard
    # cv2.waitKey(0) = if you press a key, it moves onto the next frame 
    # cv2.waitKey(1) = wait one millisec before moving onto next frame 
    key= cv2.waitKey(1)

    # if key pressed is 27(code for esc key) then break from loop
    if key ==27:
        break


# cleanup 
capture.release()
cv2.destroyAllWindows()