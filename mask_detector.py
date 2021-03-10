from keras.models import load_model
import cv2 as cv
import numpy as np
import os
from cvlib import *

def mask():
    model = load_model("Models/model-004.model")
    cascade = "haarcascade_frontalface_default.xml"
    face_classifier = cv.CascadeClassifier(cascade)

    cap = cv.VideoCapture(0)
    labels_dict = {0: "MASK", 1: "NO MASK"}
    color_dict = {0: (0, 255, 0), 1: (0, 0, 255)}

    while True:
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
        ret, frame = cap.read()
        frame = cv.flip(frame, 1)
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

        if len(faces) == 0:
            warning_text = "No faces found ! ! !"
            cv.putText(frame, warning_text, (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        for x, y, w, h in faces:
            face_img = gray[y:y+w, x:x+h]
            resized = cv.resize(face_img, (100, 100))
            normalized = resized/255.0
            reshaped = np.reshape(normalized, (1, 100, 100, 1))
            result = model.predict(reshaped)

            label = np.argmax(result, axis=1)[0]
            cv.rectangle(frame, (x, y), (x + w, y + h), color_dict[label], 2)
            cv.rectangle(frame, (x, y-40), (x + w, y), color_dict[label], -1)
            cv.putText(frame, labels_dict[label], (x, y-10), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
            i = len(faces)
            face_display = f"Number of faces found == 0{i}"
            cv.putText(frame, face_display, (10, 20), cv.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
        cv.imshow("LIVE", frame)

    cap.release()
    cv.destroyAllWindows()
