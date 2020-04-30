# Find already created folders
from __future__ import print_function
import os, sys

path = 'trainingImages'

if len(sys.argv) == 2:
    path = sys.argv[1]

files = os.listdir(path)
for name in files:
    filename = name

# Create Directory
directory = str(int(filename) + 1)
newDirec = os.path.join('trainingImages\\', directory)
os.mkdir(newDirec)

# Capture Images and Store in the above folder
import cv2

cap = cv2.VideoCapture(0)

count = 0

while True:
    ret, test_img = cap.read()
    if not ret:
        continue
    cv2.imwrite("trainingImages\\" + str(int(filename) + 1) + "\\frame%d.jpg" % count,
                test_img)  # save frame as JPG file
    count += 1
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('Collecting Training Data', resized_img)
    if count == 200:
        break
    if cv2.waitKey(10) == ord('q'):  # wait until 'q' key is pressed
        break

cap.release()
cv2.destroyAllWindows
