from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model
import numpy as np
import cv2
import cvlib as cv
def smoke():
    model = load_model("Models/smoke.model")
    cap = cv2.VideoCapture(0)

    classes = ['Smoking',"Not Smoking"]

    while (cap.isOpened()):
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
        if idx==1:
            print("Smoking")

        else:
            print("not")


        labels = classes[idx]
        labels = "{}".format(labels)

        # write label and confidence above face rectangle
        cv2.putText(frame, labels, (100, 100), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
        cv2.imshow("Gender Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break


    cap.release()
    cv2.destroyAllWindows()
