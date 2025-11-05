import cv2
import os 
import time
import uuid

image_path = 'C://Users//nehal//RealTimeObjectDetection//Tensorflow//workspace//images'
labels = ['hello', 'bye', 'yes', 'no', 'thankyou', 'i love you']
number_imgs = 15

for label in labels:
    label_path = os.path.join(image_path, label)
    os.makedirs(label_path, exist_ok=True)  # Create directory if it doesn't exist
    cap = cv2.VideoCapture(0)
    print('Collecting images for {}'.format(label))
    time.sleep(5)
    
    for imgnum in range(number_imgs):
        ret, img = cap.read()
        if ret:  # Check if frame was successfully captured
            imgname = os.path.join(label_path, label + '.' + '{}.jpg'.format(str(uuid.uuid1())))
            cv2.imwrite(imgname, img)
            cv2.imshow('frame', img)
            time.sleep(2)
        else:
            print("Failed to capture frame.")
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    cap.release()

cv2.destroyAllWindows()
