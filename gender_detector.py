from keras.models import load_model
import cv2
import numpy as np
import os
from cvlib import *
from tkinter import *
from PIL import Image, ImageTk

def gen(frame1,frame2):
    model = load_model("Models/model-010.model")
    cascade = "haarcascade_frontalface_default.xml"
    face_classifier = cv2.CascadeClassifier(cascade)

    # cap = cv2.VideoCapture("http://<IP Address>:4747/mjpegfeed")
    cap = cv2.VideoCapture(0)
    labels_dict = {0: "Male", 1: "Female"}
    color_dict = {0: (0, 255, 0), 1: (0, 0, 255)}
    canvas = Canvas(frame1, width=785, height=425)
    canvas.place(x=10, y=10)
    exit_button = Button(frame1, text='Close', fg="purple", font="serif 16 bold",
                         command=lambda: exit(cap, canvas, exit_button))
    exit_button.place(x=10, y=395)
    while cap.isOpened():
        try:
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            ret, frame = cap.read()
            frame = cv2.flip(frame, 1)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = face_classifier.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)


            for x, y, w, h in faces:
                face_img = gray[y:y+w, x:x+h]
                resized = cv2.resize(face_img, (100, 100))
                normalized = resized/255.0
                reshaped = np.reshape(normalized, (1, 100, 100, 1))
                result = model.predict(reshaped)

                label = np.argmax(result, axis=1)[0]
                if label == 1:
                    text = Label(frame2, text="Female", font=("Courier", 35), bg="black", fg="white")
                    text.place(x=150, y=40)

                if label ==0:
                    text = Label(frame2, text="male", font=("Courier", 35), bg="black", fg="white")
                    text.place(x=150, y=40)

                print(label)
                cv2.rectangle(frame, (x, y), (x + w, y + h), color_dict[label], 2)
                cv2.rectangle(frame, (x, y-40), (x + w, y), color_dict[label], -1)
                cv2.putText(frame, labels_dict[label], (x, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
                i = len(faces)


            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            cv2image = cv2.resize(rgb, (795, 435))
            img = Image.fromarray(cv2image)
            imgtk = ImageTk.PhotoImage(img)
            canvas.create_image(390, 210, image=imgtk)
            canvas.update()
            frame2.update()
        except:
            pass


    cap.release()
    cv2.destroyAllWindows()

def exit(cap,canvas,button):
    cap.release()
    cv2.destroyAllWindows()
    canvas.destroy()
    button.destroy()
