import os
import time 
import cv2 as cv #opencv
import uuid
IMAGES_PATH = "Desktop/SignalPython/photo"
labels = ['hello', 'thanks', 'yes', 'no', 'I love you']
number_imgs = 15
for label in labels:
    os.makedirs('Desktop\SignalPython\photo\\'+ label)
    cap = cv.VideoCapture(0)
    print('Collucting images for ()'.format(label))
    time.sleep(0)
    for imgnum in range(number_imgs):
        ret, frame = cap.read()
        imagename = os.path.join(IMAGES_PATH, label, label+ '.'+'{}.jpg'.format(str(uuid.uuid1())))
        cv.imwrite(imagename, frame)
        cv.imshow('frame', frame)
        time.sleep(1)

        if cv.waitKey(1) & 0xFF == ord('d'):
            break
    cap.release()
    cv.destroyAllWindows()