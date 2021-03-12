from face_recognition import *
import cv2
import os

capture = cv2.VideoCapture(0)

def face_matched(username):

    known_face = load_image_file(f"/users_facial_data"+f"/{username}.jpg")



    return True

def face_login(self):
        saved_img = load_image_file("users_facial_data/"+self.label_username_entry.get()+".jpg")
        print(saved_img)
        saved_img_encodings = face_detection.face_encodings(saved_img)[0]

        # self.cap = cv2.VideoCapture("http://<IP Address>:4747/mjpegfeed")
        self.cap = cv2.VideoCapture(0)
        _, self.vid = self.cap.read()

        for i in range(1, 1000):

            self.face = self.data.detectMultiScale(self.vid, scaleFactor=1.1, minNeighbors=4, minSize=(100, 100))

            while self.face != ():
                for x, y, h, w in self.face:
                    self.crop_img = self.vid[y:y + h + 30, x:x + w + 30]
                    self.image = cv.cvtColor(self.crop_img, cv.COLOR_BGR2GRAY)

                    self.image = cv.resize(self.image, dsize=(450, 350), interpolation=cv.INTER_CUBIC)
                    self.image = Image.fromarray(self.image)  # to PIL format
                    self.image = ImageTk.PhotoImage(self.image)  # to ImageTk format
                    self.canvas.create_image(500, 200, image=self.image)

                    self.live_img_encoding = face_encodings(self.image)[0]
                    print("encoding image = ", self.live_img_encoding)
                    self.compare = compare_faces(saved_img_encodings, self.live_img_encoding, tolerance=0.6)
                    if self.compare:
                        return True
                        break
                    else:
                        return True
                        break
                    print("Comparing",self.compare)

            self.cap.release()

