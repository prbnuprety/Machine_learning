from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from connect import *
import cv2 as cv
import os
import messaging
import numpy as np
import face_recognition
from machine_learning import final_eval_cvlib
import gender_detector
import mask_detector
import smoking
import weapon_detect

class Project:
    """ Initializing variables and login interface """

    def __init__(self, interface):

        self.interface = interface
        self.interface.geometry("1080x600")
        self.interface.title("Real World Project")
        self.interface.resizable(False, False)
        self.interface.config(bg="skyblue")

        self.ret = False
        self.file = "haarcascade_frontalface_default.xml"
        self.data = cv.CascadeClassifier(self.file)

        self.frame_left = Frame(self.interface, width=300, height=500, bg='grey')
        self.frame_left.grid(row=0, column=0, padx=8, pady=5)


        self.frame2_right = Frame(self.interface, width=750, height=580, bg='grey')
        self.frame2_right.grid(row=0, column=1, padx=10, pady=5)

        # loading images in fram2_right####
        self.bg = ImageTk.PhotoImage(file="face123.jpg")
        self.bg_image = Label(self.frame2_right, image=self.bg)
        self.bg_image.place(x=10, y=10, relwidth=1, relheight=1)

        self.label1 = Label(self.frame2_right, text="Human Activity Monitoring System", font="cambria 25 bold",
                            fg="blue")
        self.label1.place(x=10, y=10)

        self.label2 = Label(self.frame2_right, text="LogIn Here !!", font=("serif", 20, "bold"))
        self.label2.place(x=400, y=100)
        self.desc = Label(self.frame2_right, text="Login to Use the Program", font=("Goudy old sytly", 10, "bold"),
                          fg="red")
        self.desc.place(x=400, y=140)

        self.frame4 = Frame(self.frame2_right, bg="white")
        self.frame4.place(x=400, y=170, height=250, width=400)

        self.label_username = Label(self.frame4, text="Username", font="cambria 18 bold", fg="gray")
        self.label_username.place(x=10, y=10)

        self.label_username_entry = Entry(self.frame4, width=30, bg="lightgray", font="serif 12 ", fg="black")
        self.label_username_entry.place(x=15, y=45, width=300, height=30)

        self.label_password = Label(self.frame4, text="Password", font="cambria 18 bold", fg="gray")
        self.label_password.place(x=10, y=75)

        self.label_password_entry = Entry(self.frame4, show="*", width=30, bg="lightgray", font="serif 12  ",
                                          fg="black")
        self.label_password_entry.place(x=15, y=115, width=300, height=30)

        self.login_btn = Button(self.frame4, text="LogIn", fg="purple", font="serif 14 bold", command=self.login)
        self.login_btn.place(x=200, y=155)

        self.forget_btn = Button(self.frame4, text="Forget Password?", fg='red', font="serif 12 bold",command=self.face_login)
        self.forget_btn.place(x=15, y=200)

        self.btn_register = Button(self.frame4, text="Register here !!", command=self.register_here, fg="gray",
                                   font="serif 12 bold underline")
        self.btn_register.place(x=200, y=215)
        self.counter = 0

    """ Interface After login"""

    def load_backend(self):
        self.frame_left.grid_forget()
        self.frame2_right.grid_forget()
        self.interface.title('Internal')

        self.main_int = Frame(self.interface, width=1080, height=600, bg="green")
        self.main_int.place(x=0, y=0)



        Button(self.main_int, text="Face Recognition", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18, command=self.cam_access).place(x=5, y=5)
        Button(self.main_int, text="Gender Detection", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18, command=gender_detector.gen).place(x=5, y=85)
        Button(self.main_int, text="Mask Detection", font=("cambria", 15, "bold"), fg="green", height=2, width=18,command= mask_detector.mask).place(
            x=5, y=165)
        Button(self.main_int, text="Weapon Detection", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18, command=weapon_detect.weapon).place(x=5, y=245)
        Button(self.main_int, text="Smoking Detection", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18, command=smoking.smoke).place(x=5, y=325)
        Button(self.main_int, text="Overall interface", font=("cambria", 15, "bold"), fg="green", height=2, width=18,
               command=lambda: self.cam_access()).place(x=5, y=405)
        Button(self.main_int, text="Exit", font=("cambria", 15, "bold"), fg="green", height=2, width=18,
               command=lambda: self.back(self.main_int)).place(x=5, y=490)

        # Label(self.frame_dl, text="Information Panel",font=("Courier", 20), bg = "black", fg="white").place(x=150, y=0)
        # Label(self.frame_dl, text="No options selected",font=("Courier", 35), bg="black", fg="white").place(x=10, y=40)

        Label(self.main_int, text="Current User",font=("Courier", 12), bg="black", fg="white").place(x=900, y=0)
        Label(self.main_int, text=f"{self.username1}".upper(), bg="black",font=("Courier", 18), fg="white").place(x=900,y= 30)


        # Label(self.frame_dl, text=f"{self.username1}".upper(), bg="black", fg="white").place(x=0, y=20)
        # Label(self.frame_dl, text=f"{self.username1}".upper(), bg="black", fg="white").place(x=0, y=40)
        # Label(self.frame_dl, text=f"{self.username1}".upper(), bg="black", fg="white").place(x=0, y=60)
        # Label(self.frame_dl, text=f"{self.username1}".upper(), bg="black", fg="white").place(x=0, y=80)

    """Accesing cam after login to detect things"""

    def cam_access(self):
        """Camera Access for all processes"""

     #   Label(self.frame_dl, text="Gaining Camera Access", font=("Courier", 20), bg="black",
  #            fg="green").place(x=10, y=40)

        self.cap = cv.VideoCapture(0)
        # self.canvas2 =  Canvas(self.frame_r, width=785, height=425)
        # self.canvas2.place(x=10, y=10)

        while True:
            if cv.waitKey(1) & 0xFF == ord('q'):
                break

            """Video Capture after camera access"""
            self.ret, self.vid = self.cap.read()
            self.face = self.data.detectMultiScale(self.vid, scaleFactor=1.1, minNeighbors=4, minSize=(100, 100))


            if self.face != ():
                for x, y, h, w in self.face:
                    print("1")
                    self.crop_img = self.vid[y:y + h + 30, x:x + w + 30]
                    self.image = cv.cvtColor(self.crop_img, cv.COLOR_BGR2RGB)
            else:
                self.image = cv.cvtColor(self.vid, cv.COLOR_BGR2RGB)

            # self.image = cv.resize(self.image, dsize=(450, 350), interpolation=cv.INTER_CUBIC)
            # self.image = Image.fromarray(self.image)  # to PIL format
            # self.image = ImageTk.PhotoImage(self.image)  # to ImageTk format
            cv.imshow("Face Reconizer",self.image)



            print("pass")
        self.cap.release()
        cv.destroyAllWindows()

    """Camera access for Registering Facial data"""

    def photo_register(self):

        self.cap = cv.VideoCapture(0)
        self.interval = 1
        self.frame2 = Frame(self.frame1, width=1000, height=500, bg="red")
        self.frame2.place(x=50, y=50)
        self.canvas = Canvas(self.frame2, width=1000, height=400)
        self.canvas.place(x=0, y=0)
        self.cap_button = Button(self.frame2, text='Capture', command=lambda: self.take_pic, fg="purple",
                                 font="serif 16 bold")
        self.cap_button.place(x=220, y=430, width=100, height=50)
        self.sav_button = Button(self.frame2, text='Save', fg="purple",
                                 font="serif 16 bold", command=self.take_pic)
        self.sav_button.place(x=470, y=430, width=100, height=50)
        self.exit_button = Button(self.frame2, text='Exit', fg="purple",
                                  font="serif 16 bold", command=lambda: self.back(self.frame2))
        self.exit_button.place(x=720, y=430, width=100, height=50)
        self.update_image()

    """Resizing, converting and creating image in canvas to register facial data"""

    def update_image(self):
        self.ret, self.vid = self.cap.read()
        self.face = self.data.detectMultiScale(self.vid, scaleFactor=1.1, minNeighbors=4, minSize=(100, 100))

        try:
            if self.face != ():
                for x, y, h, w in self.face:
                    self.crop_img = self.vid[y:y + h + 30, x:x + w + 30]
                    self.image = cv.cvtColor(self.crop_img, cv.COLOR_BGR2RGB)
            else:
                self.image = cv.cvtColor(self.vid, cv.COLOR_BGR2RGB)

            self.image = cv.resize(self.image, dsize=(450, 350), interpolation=cv.INTER_CUBIC)
            self.image = Image.fromarray(self.image)  # to PIL format
            self.image = ImageTk.PhotoImage(self.image)  # to ImageTk format
            self.canvas.create_image(500, 200, image=self.image)

        except:
            pass



        if self.ret != False:
            self.frame2_right.after(self.interval, self.update_image)

        else:
            pass

    """Interface to register a user inorder to login"""

    def register_here(self):

        self.frame_left.grid_forget()
        self.frame2_right.grid_forget()
        self.interface.title('Registration Page')

        self.frame1 = Frame(self.interface, width=1080, height=600, bg="White")
        self.frame1.place(x=0, y=0)

        self.frame3 = Frame(self.frame1, width=400, height=500, bg="blue")
        self.frame3.place(x=50, y=50)

        self.label = Label(self.frame1, text="We kindly request you to register here!!", font=("serif", 14, "bold"),
                           fg="red")
        self.label.place(x=300, y=0)

        self.label_fname = Label(self.frame3, text="First Name", font=("calibri", 15, "bold"), fg="grey")
        self.label_fname.place(x=10, y=10)

        self.entry_fname = Entry(self.frame3, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_fname.place(x=130, y=10, height=30, width=200)

        self.label_middle_name = Label(self.frame3, text="Middle Name", font=("calibri", 15, "bold"), fg="grey")
        self.label_middle_name.place(x=10, y=45)

        self.entry_middle_name = Entry(self.frame3, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_middle_name.place(x=130, y=45, height=30, width=200)

        self.label_lname = Label(self.frame3, text="Last Name", font=("calibri", 15, "bold"), fg="grey")
        self.label_lname.place(x=10, y=80)

        self.entry_lname_name = Entry(self.frame3, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_lname_name.place(x=130, y=80, height=30, width=200)

        self.label_age = Label(self.frame3, text="Age", font=("calibri", 15, "bold"), fg="grey")
        self.label_age.place(x=10, y=115)

        self.entry_age_name = Entry(self.frame3, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_age_name.place(x=130, y=115, height=30, width=200)

        self.label_num = Label(self.frame3, text="Phone No.", font=("cambria", 15, "bold"), fg="grey")
        self.label_num.place(x=10, y=150)

        self.entry_num = Entry(self.frame3, font=('cambria', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_num.place(x=130, y=150, height=30, width=200)

        self.label_gender = Label(self.frame3, text="Gender", font=("calibri", 15, "bold"), fg="grey")
        self.label_gender.place(x=10, y=190)

        self.entry_gender = ttk.Combobox(self.frame3, state="readonly", values=["Male", "Female", "Others"],
                                         font=("calibri", 15, "bold"))
        self.entry_gender.place(x=130, y=190, height=30, width=200)
        self.entry_gender.set("Select")
        self.label_username = Label(self.frame3, text="Username", font=("calibri", 15, "bold"), fg="grey")
        self.label_username.place(x=10, y=225)

        self.entry_username = Entry(self.frame3, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_username.place(x=130, y=225, height=30, width=200)

        self.label_password = Label(self.frame3, text="Password", font=("calibri", 15, "bold"), fg="grey")
        self.label_password.place(x=10, y=260)

        self.entry_password = Entry(self.frame3, show="*", font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_password.place(x=130, y=260, height=30, width=200)

        self.label_confirm_password = Label(self.frame3, text="Confirm Password", font=("calibri", 15, "bold"),
                                            fg="grey")
        self.label_confirm_password.place(x=10, y=295)

        self.entry_confirm_password = Entry(self.frame3, show="*", font=('calibri', 15, 'bold'), fg="black",
                                            bg="lightgrey")
        self.entry_confirm_password.place(x=180, y=295, height=30, width=150)

        self.button_register = Button(self.frame3, text='Register', command=self.save, fg="purple",
                                      font="serif 16 bold")
        self.button_register.place(x=100, y=350, height=30, width=100)
        self.button_back = Button(self.frame3, text="Back", command=lambda: self.back(self.frame1), fg="Black",
                                  font="serif 16 bold")
        self.button_back.place(x=150, y=400, height=30, width=100)

    # def face_login(self):
    #     self.cap = cv.VideoCapture(0)
    #     self.interval = 10
    #     self.frame2 = Frame(self.frame1, width=450, height=350, bg="red")
    #     self.frame2.place(x=50, y=50)
    #     self.canvas = Canvas(self.frame2, width=400, height=300)
    #     self.canvas.place(x=0, y=0)
    #     self.cap_button = Button(self.frame2, text='Capture', command=lambda: self.take_pic(self.vid), fg="purple",
    #                              font="serif 16 bold")
    #     self.cap_button.place(x=180, y=270, width=30, height=30)
    #     self.update_image()

    """Method to access one step behind interface"""

    def back(self, frame):
        frame.place_forget()


        self.frame_left.grid(row=0, column=0, padx=8, pady=5)
        self.frame2_right.grid(row=0, column=1, padx=10, pady=5)
        self.interface.title("Real World Project")
        try:
            if self.ret != False:
                self.cap.release()
                cv.destroyAllWindows()

            else:
                pass

        except:
            pass

    """Clear register interface entries"""
    def clear(self):
        self.entry_fname.delete(0, END)
        self.entry_middle_name.delete(0, END)
        self.entry_lname_name.delete(0, END)
        self.entry_age_name.delete(0, END)
        self.entry_num.delete(0, END)
        self.entry_gender.set("Select")
        self.entry_username.delete(0, END)
        self.entry_password.delete(0, END)
        self.entry_confirm_password.delete(0, END)

    """Method to Save picture in folder"""
    def take_pic(self):
        path = os.getcwd() + "\\users_facial_data"

        if self.entry_username.get != None:
            self.gray = cv.cvtColor(self.crop_img, cv.COLOR_BGR2GRAY)
            cv.imwrite(os.path.join(path, f"{self.entry_username.get()}" + ".jpg"), self.gray)



        else:
            messagebox.showerror("error", "Enter valid username")

        cv.destroyAllWindows()
        self.cap.release()


        self.clear()
        self.back(self.frame1)

        messagebox.showinfo('Successful', 'Registered success')
    """Save the users data in the database for future access"""

    def save(self):
        self.con = Connection()
        self.cur = self.con.cur

        try:
            self.fname = self.entry_fname.get().upper()
            self.mname = self.entry_middle_name.get().upper()
            self.lname = self.entry_lname_name.get().upper()
            self.age = self.entry_age_name.get()
            self.phone = self.entry_num.get()
            self.gen = self.entry_gender.get()
            self.username = self.entry_username.get()
            self.password = self.entry_password.get()
            self.conform_pass = self.entry_confirm_password.get()

            if self.fname and self.lname and self.age and self.phone and self.gen and self.username and self.password and self.conform_pass:
                if self.password == self.conform_pass:


                    self.value = (self.fname, self.mname, self.lname, self.age, self.phone, self.gen, self.username, self.password)
                    self.query = 'insert into registration values(%s,%s,%s,%s,%s,%s,%s,%s)'
                    self.cur.execute(self.query, self.value)
                    self.photo_register()


                else:
                    messagebox.showerror("Error", "Password do not match")
            else:
                messagebox.showerror("Error", "Fill all Data")
        except mysql.connector.Error as e:
            messagebox.showerror('Error', e)
        self.con.close()


    """Face login system Using facial recognition system"""
    def face_login(self):
        saved_img = face_recognition.load_image_file("users_facial_data/"+self.label_username_entry.get()+".jpg")
        print(saved_img)
        saved_img_encodings = face_recognition.face_encodings(saved_img)[0]
        self.frame2 = Frame(self.frame2_right, width=750, height=580, bg="gray")
        self.frame2.grid(row=0, column=0)
        self.canvas = Canvas(self.frame2, width=1000, height=400)
        self.canvas.place(x=0, y=0)
        self.cap_button = Button(self.frame2, text='Capture', command=lambda: self.take_pic, fg="purple",
                                 font="serif 16 bold")

        self.cap = cv.VideoCapture(0)
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

                    self.live_img_encoding = face_recognition.face_encodings(self.image)[0]
                    print("encoding image = ", self.live_img_encoding)
                    self.compare = face_recognition.compare_faces(saved_img_encodings, self.live_img_encoding, tolerance=0.6)
                    print("Comparing",self.compare)

            self.cap.release()

    "Accessing database to login as a appropriate user"
    def login(self):
        self.con = Connection()
        self.cur = self.con.cur

        """ .................File handling for retrieving and comparing data to login..................."""
        self.username1 = self.label_username_entry.get()
        self.password1 = self.label_password_entry.get()

        try:
            if self.username1 and self.password1:
                self.query = f'select password from registration where username="{self.username1}"'
                self.cur.execute(self.query)
                self.result = self.cur.fetchone()
                if self.result == None:
                    messagebox.showerror("Error", "Username don't exist in database ")

                else:
                    if self.result[0] == self.password1:
                        messagebox.showinfo("login", "Successfully logged in")
                        self.load_backend()
                        self.counter = 0
                    else:
                        self.counter += 1
                        if self.counter >= 3:
                            messaging.send_error_login()
                        print(self.counter)
                        messagebox.showerror("Error", "Username or password do not matched")
            else:
                messagebox.showerror("Error", "Username or password is empty")


        except mysql.connector.Error as e:
            messagebox.showerror("Error", e)

        self.con.close()


interface = Tk()
gui = Project(interface)
interface.mainloop()
