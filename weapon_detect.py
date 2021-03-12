from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
from tkinter import *
import cvlib as cv
from PIL import Image, ImageTk
def weapon(frame1,frame2):

    model = load_model("Models/weapon.model")
    # cap = cv2.VideoCapture("http://<IP Address>:4747/mjpegfeed")
    cap = cv2.VideoCapture(0)

    classes = ["Weapon Detected",'No weapon']
    canvas = Canvas(frame1, width=785, height=425)
    canvas.place(x=10, y=10)
    exit_button = Button(frame1, text='Close', fg="purple", font="serif 16 bold",
                         command=lambda: exit(cap, canvas, exit_button))
    exit_button.place(x=10, y=395)
    while (cap.isOpened()):
        try:

            ret, frame = cap.read()
           # print(ret)
            if ret == False:
                print("System is unable to read data")
                break

            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            data = cv2.resize(gray, (100, 100))
            #print(data)

            data = data.astype("float") / 255.0
            data = np.reshape(data, (100, 100, 1))
            #print(data)
            data = img_to_array(data)
           # print(data)
            data = np.expand_dims(data, axis=0)
          #  print(data)

            confidence = model.predict(data)
            print(confidence)
            # get label with max accuracy
            idx = np.argmax(confidence)
            print(idx)


            labels = classes[idx]
            labels = "{}".format(labels)

            # write label and confidence above face rectangle
            # cv2.putText(frame2, labels, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            text = Label(frame2, text=labels, font=("Courier", 35), bg="black", fg="white")
            text.place(x=150, y=40)
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
