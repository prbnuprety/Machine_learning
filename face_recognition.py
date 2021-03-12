from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import cvlib as cv
from tkinter import *
from PIL import Image, ImageTk

# load model
def face(frame1,frame2):

    # open webcam
    # cap = cv2.VideoCapture("http://<IP Address>:4747/mjpegfeed")
    cap = cv2.VideoCapture(0)



    canvas = Canvas(frame1, width=785, height=425)
    canvas.place(x=10, y=10)
    exit_button = Button(frame1, text='Close', fg="purple", font="serif 16 bold",
                         command=lambda: exit(cap, canvas, exit_button))
    exit_button.place(x=10, y=395)
    # loop through frames
    while (cap.isOpened()):
        # read data from webcam
        ret, frame = cap.read()
        print(ret)
        if ret==False:
            print("System is unable to read data")
            break

        # apply face detection
        face, confidence = cv.detect_face(frame)
        if len(face)>0:
            print("User is facing to the camera")
        else:
            print("webcam couldn't detect user")
        print(face)
        print(confidence)

        # loop through detected faces
        for idx, f in enumerate(face):
            print(f)
            print(idx)
            # get corner points of face rectangle
            (startX, startY) = f[0], f[1]
            print(startX,startY)
            (endX, endY) = f[2], f[3]
            print(endX,endY)

            # draw rectangle over face
            cv2.rectangle(frame, (startX, startY), (endX, endY), (255, 0, 0), 3)

            # crop the detected face region
            face_crop = np.copy(frame[startY:endY, startX:endX])

            if (face_crop.shape[0]) < 10 or (face_crop.shape[1]) < 10:

                continue

            # preprocessing for gender detection model
            face_crop = cv2.resize(face_crop, (96, 96)) #because our model is trained in particular dimension.
            print(face_crop)
            face_crop = face_crop.astype("float") / 255.0
            print(face_crop)
            face_crop = img_to_array(face_crop)
            print(face_crop)

            text = Label(frame2, text="No. of Faces", font=("Courier", 35), bg="black", fg="white")
            text.place(x=150, y=40)
        rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        cv2image = cv2.resize(rgb, (795, 435))
        img = Image.fromarray(cv2image)
        imgtk = ImageTk.PhotoImage(img)
        canvas.create_image(390, 210, image=imgtk)
        canvas.update()
        frame2.update()

    # release resources
    cap.release()
    cv2.destroyAllWindows()

def exit(cap,canvas,button):
    cap.release()
    cv2.destroyAllWindows()
    canvas.destroy()
    button.destroy()

#That function returns an array of all the faces it found and an array of numbers to show how sure
# it is that those are faces. We will not be using the confidence array and only the array of faces, named face.
# To see if we have any faces in the data, we can just check the length of that array.
# So this means we could simply return the following to specify if we found a face or not.