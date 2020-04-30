import cv2
import FaceRecognitionAtd.haarCascade as hc
import pandas as pd
from datetime import date
from openpyxl import load_workbook
from FaceRecognitionAtd.testDict import finalDict

today = date.today()
# dd-mm-YY
currentDate = today.strftime("%d-%m-%Y")

face_recognizer = cv2.face.LBPHFaceRecognizer_create()
face_recognizer.read('trainingData.yml')

name = finalDict

cap = cv2.VideoCapture(0)

imgCount = 0

atCandidate = []
atCandidateUnique = []
count = 0
while True:
    ret, test_img = cap.read()  # captures frame and returns boolean value and captured image
    faces_detected, gray_img = hc.faceDetection(test_img)

    for (x, y, w, h) in faces_detected:
        cv2.rectangle(test_img, (x, y), (x + w, y + h), (255, 0, 0), thickness=7)

    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face detection Tutorial ', resized_img)
    cv2.waitKey(10)

    for face in faces_detected:
        (x, y, w, h) = face
        roi_gray = gray_img[y:y + w, x:x + h]
        label, confidence = face_recognizer.predict(roi_gray)
        print("Confidence:", confidence)
        print("Name:", name[label][0])
        print("SC Code:", name[label][1])
        print("Branch:", name[label][2])

        imgCount = imgCount + 1

        hc.draw_rect(test_img, face)
        predicted_name = name[label][0]
        hc.put_text(test_img, predicted_name, x, y)
        if confidence < 40:
            hc.put_text(test_img, predicted_name, x, y)
        else:
            atCandidate.append([name[label][0],
                                name[label][1],
                                name[label][2],
                                currentDate])
            for i in atCandidate:
                if i not in atCandidateUnique:
                    atCandidateUnique.append([name[label][0],
                                              name[label][1],
                                              name[label][2],
                                              currentDate])

            atCandidate = []
    resized_img = cv2.resize(test_img, (1000, 700))
    cv2.imshow('face recognition tutorial ', resized_img)

    if cv2.waitKey(10) == ord('q'):
        break

dataFrame = pd.DataFrame(atCandidateUnique[0:], columns=["Name", "SC Code", "Department", "Date"])
dataFrame = dataFrame.rename(columns={'Department': 'Branch'})

cap.release()
cv2.destroyAllWindows

path = r"attendance.xlsx"

book = load_workbook(path)
writer = pd.ExcelWriter(path, engine='openpyxl')
writer.book = book

dataFrame.to_excel(writer, sheet_name=currentDate)
writer.save()
writer.close()

dataFrame = dataFrame.rename(columns={'SC Code': 'sccode'})
