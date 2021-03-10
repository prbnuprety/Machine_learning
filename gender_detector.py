from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import cvlib as cv

# load model
def gen():
    model = load_model("Models/man_woman.model")

    # open webcam
    cap = cv2.VideoCapture(0)

    classes = ['man', 'woman']

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
            face_crop = np.expand_dims(face_crop, axis=0)
            #expand_dims() function is used to expand the shape of an array.
            # Insert a new axis that will appear at the axis position in the expanded array shape
            print(face_crop)
            # apply gender detection on face
            confidence = model.predict(face_crop)[0]  # model.predict return a 2D matrix, ex: [[9.9993384e-01 7.4850512e-05]]
            #so inorder to use 1D matrix we use index zero at its last.

            # get label with max accuracy
            idx = np.argmax(confidence)
            #argmax is a function which gives the index of the greatest number in the given row or column
            labels = classes[idx]

            labels = "{}: {:.2f}%".format(labels, confidence[idx] * 100)

            if startY - 10 > 10:
                Y= startY-10
            else:
                Y=startY + 10
            # write label and confidence above face rectangle
            cv2.putText(frame, labels, (startX, Y), cv2.FONT_HERSHEY_SIMPLEX,0.7, (0, 255, 0), 2)

        # display output
        cv2.imshow("Gender Detection", frame)

        # press "Q" to stop
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # release resources
    cap.release()
    cv2.destroyAllWindows()

#That function returns an array of all the faces it found and an array of numbers to show how sure
# it is that those are faces. We will not be using the confidence array and only the array of faces, named face.
# To see if we have any faces in the data, we can just check the length of that array.
# So this means we could simply return the following to specify if we found a face or not.