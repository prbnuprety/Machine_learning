from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from connect import *
import cv2 as cv
import os
import messaging
import numpy as np
import face_detection
import facecheck
import weapon_detect
import smoking
import mask_detector
import gender_detector
import face_recognition
from winsound import Beep
import time


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

        self.frame_left = Frame(self.interface, width=300, height=470, bg='lightblue')
        self.frame_left.grid(row=0, column=0, padx=8, pady=5)

        self.frame_green = Frame(self.frame_left, width=290, height=30)
        self.frame_green.place(x=4, y=8)

        self.Label123 = Label(self.frame_green, text='"YOU ARE UNDER CCTV SURVEILLANCE"', font='gothic 10 bold',
                              fg="red")
        self.Label123.place(x=3, y=5)
        self.Label2 = Label(self.interface, text="TEAM CODE:'P@SS ", bg="lightblue", font="mincho 17 bold", fg="red")
        self.Label2.place(x=50, y=485)

        self.frame_l = Frame(self.frame_left, width=280, height=430, bg="grey")
        self.frame_l.place(x=10, y=50)

        # loading images in frame2_right###
        self.bg = Image.open("frontface.PNG")
        # resized image
        self.resized = self.bg.resize((280, 360), Image.ANTIALIAS)
        self.image2 = ImageTk.PhotoImage(self.resized)

        # Image size
        self.bg_image = Label(self.frame_l, image=self.image2)
        self.bg_image.pack(pady=1)

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

        self.frame4 = Frame(self.frame2_right, bg="lightgreen")
        self.frame4.place(x=400, y=170, height=250, width=400)

        self.label_username = Label(self.frame4, text="Username", font="cambria 18 bold", bg="lightgreen")
        self.label_username.place(x=10, y=10)

        self.label_username_entry = Entry(self.frame4, width=30, bg="lightgray", font="serif 12 ", fg="black")
        self.label_username_entry.place(x=15, y=45, width=300, height=30)

        self.label_password = Label(self.frame4, text="Password", font="cambria 18 bold", bg="lightgreen")
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

        self.frame_l = Frame(self.main_int, width=240, height=580, bg="black")
        self.frame_l.place(x=10, y=10)

        self.frame_r = Frame(self.main_int, width=810, height=450, bg="black")
        self.frame_r.place(x=260, y=10)

        self.frame_dl = Frame(self.main_int, width=650, height=120, bg="black")
        self.frame_dl.place(x=260, y=470)

        self.frame_dr = Frame(self.main_int, width=150, height=120, bg="black")
        self.frame_dr.place(x=920, y=470)

        Button(self.frame_l, text="Face Detection", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18, command=lambda:face_detection.face(self.frame_r,self.frame_dl)).place(x=5, y=5)
        Button(self.frame_l, text="Gender Detection", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18, command=lambda: gender_detector.gen(self.frame_r,self.frame_dl)).place(x=5, y=85)
        Button(self.frame_l, text="Mask Detection", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18,command=lambda: mask_detector.mask(self.frame_r,self.frame_dl)).place(x=5, y=165)
        Button(self.frame_l, text="Weapon Detection", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18, command=lambda: weapon_detect.weapon(self.frame_r,self.frame_dl)).place(x=5, y=245)
        Button(self.frame_l, text="Smoking Detection", font=("cambria", 15, "bold"), fg="green", height=2,
               width=18, command=lambda: smoking.smoke(self.frame_r,self.frame_dl)).place(x=5, y=325)
        # Button(self.frame_l, text="Overall interface", font=("cambria", 15, "bold"), fg="green", height=2, width=18,
        #        command=lambda: self.cam_access()).place(x=5, y=405)
        Button(self.frame_l, text="Exit", font=("cambria", 10, "bold"), fg="green", height=1, width=12,
               command=lambda: self.back(self.main_int)).place(x=6, y=500)

        Label(self.frame_dl, text="Information Panel",font=("Courier", 20), bg = "black", fg="white").place(x=150, y=0)


        Label(self.frame_dr, text="Current User",font=("Courier", 12), bg="black", fg="white").place(x=20, y=0)
        Label(self.frame_dr, text=f"{self.username1}".upper(), bg="black",font=("Courier", 18), fg="white").place(x=0,y= 20)


        # Label(self.frame_dl, text=f"{self.username1}".upper(), bg="black", fg="white").place(x=0, y=20)
        # Label(self.frame_dl, text=f"{self.username1}".upper(), bg="black", fg="white").place(x=0, y=40)
        # Label(self.frame_dl, text=f"{self.username1}".upper(), bg="black", fg="white").place(x=0, y=60)
        # Label(self.frame_dl, text=f"{self.username1}".upper(), bg="black", fg="white").place(x=0, y=80)

    """Accesing cam after login to detect things"""

    def cam_access(self):
        """Camera Access for all processes"""
        try:
            self.cap.release()
            self.canvas2.delete("all")
            # Label(self.frame_dl, text="Camera in Use, Gaining Access", font=("Courier", 20), bg="black", fg="red").place(x=10, y=40)
        except:
            Label(self.frame_dl, text="Gaining Camera Access", font=("Courier", 20), bg="black",
                  fg="green").place(x=10, y=40)

        # self.cap = cv2.VideoCapture("http://<IP Address>:4747/mjpegfeed")
        self.cap = cv2.VideoCapture(0)
        self.canvas2 =  Canvas(self.frame_r, width=785, height=425)
        self.canvas2.place(x=10, y=10)
        self.video_cap()
        # self.cap2.release()

    """Resizing, converting and creating image in canvas"""

    def video_cap(self):
        """Video Capture after camera access"""
        try:
            self.ret, self.frame = self.cap.read()
            self.cv2image = cv.cvtColor(self.frame, cv.COLOR_BGR2RGB)
            self.cv2image = cv.flip(self.cv2image, 1)
            self.cv2image = cv.resize(self.cv2image, (795, 435))
            self.img = Image.fromarray(self.cv2image)
            self.imgtk = ImageTk.PhotoImage(self.img)
            self.canvas2.create_image(390, 210, image=self.imgtk)
            self.frame_r.after(1, self.video_cap)
        except:
            pass

    """Camera access for Registering Facial data"""

    def photo_register(self):

        # self.cap = cv2.VideoCapture("http://<IP Address>:4747/mjpegfeed")
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

        self.frame1 = Frame(self.interface, width=600, height=800, bg="grey")
        self.frame1.place(x=330, y=30)


        # loading images in frame2_right###

        self.bg_1 = Image.open('form.png')
        self.resized_1 = self.bg_1.resize((350, 550), Image.ANTIALIAS)
        self.image2_1= ImageTk.PhotoImage(self.resized_1)

        self.bg_image_1 = Label(self.frame1, image=self.image2_1)
        self.bg_image_1.pack(pady=1)

        self.boy_frame= Frame(self.frame1,width=265,height=365,bg="lightgrey")
        self.boy_frame.place(x=45,y=220)

    #
        self.label = Label(self.boy_frame, text="We kindly request you to register here!!", font=("serif", 10,"bold"),
                    fg="red",bg="lightgrey")
        self.label.place(x=5, y=0)
        #
        self.label_fname = Label(self.boy_frame, text="First Name ", font=("calibri", 13, "bold"), bg="lightgrey")
        self.label_fname.place(x=7, y=25)
        #
        self.entry_fname = Entry(self.boy_frame, font=('calibri', 13, 'bold'), bg="lightgrey")
        self.entry_fname.place(x=108, y=25, height=28,width=150)
        #
        self.label_middle_name = Label(self.boy_frame, text="Middle Name", font=("calibri", 13, "bold"), bg="lightgrey")
        self.label_middle_name.place(x=7, y=50)
        #
        self.entry_middle_name = Entry(self.boy_frame, font=('calibri', 13, 'bold'), bg="lightgrey")
        self.entry_middle_name.place(x=108, y=50, height=30, width=150)
        #
        self.label_lname = Label(self.boy_frame, text="Last Name", font=("calibri", 15, "bold"), bg="lightgrey")
        self.label_lname.place(x=7, y=80)
        #
        self.entry_lname_name = Entry(self.boy_frame, font=('calibri', 15, 'bold'), bg="lightgrey")
        self.entry_lname_name.place(x=108, y=80, height=30, width=150)
        #
        self.label_age = Label(self.boy_frame, text="Age", font=("calibri", 13, "bold"), bg="lightgrey")
        self.label_age.place(x=7, y=110)
        #
        self.entry_age_name = Entry(self.boy_frame, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_age_name.place(x=108, y=110, height=30, width=150)
        #
        self.label_num = Label(self.boy_frame, text="Phone No.", font=("cambria", 13, "bold"), bg="lightgrey")
        self.label_num.place(x=7, y=140)
        #
        self.entry_num = Entry(self.boy_frame, font=('cambria', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_num.place(x=108, y=140, height=30, width=150)
        #
        self.label_gender = Label(self.boy_frame, text="Gender", font=("calibri", 13, "bold"), bg="lightgrey")
        self.label_gender.place(x=7, y=170)
        #
        self.entry_gender = ttk.Combobox(self.boy_frame, state="readonly", values=["Male", "Female", "Others"],
                                          font=("calibri", 15, "bold"))
        self.entry_gender.place(x=108, y=170, height=30, width=150)
        self.entry_gender.set("Select")
        self.label_username = Label(self.boy_frame, text="Username", font=("calibri", 13, "bold"), bg="lightgrey")
        self.label_username.place(x=8, y=200)
        #
        self.entry_username = Entry(self.boy_frame, font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_username.place(x=108, y=200, height=30, width=150)
        #
        self.label_password = Label(self.boy_frame, text="Password", font=("calibri", 13, "bold"), bg="lightgrey")
        self.label_password.place(x=8, y=230)
        #
        self.entry_password = Entry(self.boy_frame, show="*", font=('calibri', 15, 'bold'), fg="black", bg="lightgrey")
        self.entry_password.place(x=108, y=230, height=30, width=150)
        #
        self.label_confirm_password = Label(self.boy_frame, text="Confirm Password", font=("calibri", 13, "bold"),
                                            bg="lightgrey")
        self.label_confirm_password.place(x=8, y=260)
        #
        self.entry_confirm_password = Entry(self.boy_frame, show="*", font=('calibri', 15, 'bold'), fg="black",
                                            bg="lightgrey")
        self.entry_confirm_password.place(x=140, y=260, height=30, width=120)
        #
        self.button_register = Button(self.boy_frame, text='Register', command=self.save, fg="purple",
                                      font="serif 16 bold")
        self.button_register.place(x=10, y=305, height=30, width=95)
        self.button_back = Button(self.boy_frame, text="Back", command=lambda: self.back(self.frame1), fg="Black",
                                  font="serif 16 bold")
        self.button_back.place(x=160, y=305, height=30, width=95)


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
    def err_sound(self):
        def do (time=200):
            Beep(261*2,time)

        def do_sharp (time=200):
            Beep(277*2,time)

        def rae (time=200):
            Beep(293*2,time)

        def rae_sharp (time=200):
            Beep(311*2,time)

        def me (time=200):
            Beep(329*2,time)

        def fa (time=time):
            Beep(349*2,time)

        def fa_sharp (time=200):
            Beep(369*2,time)

        def sol (time=200):
            Beep(392*2,time)
        def sol_sharp (time=200):
            Beep(415*2,time)
        def ra (time=200):
            Beep(440*2,time)
        def ra_shar (time=200):
            Beep(446*2,time)
        def si (time=200):
            Beep(493*2,time)

        def high_do (time=200):
            Beep(523*2,time)
        def high_do_sharp (time=200):
            Beep(554*2,time)

        def high_rae (time=200):
            Beep(587*2,time)
        def high_rae_sharp (time=200):
            Beep(622*2,time)
        def high_me (time=200):
            Beep(659*2,time)
        def high_fa (time=200):
            Beep(698*2,time)
        def high_fa_sharp (time=200):
            Beep(739*2,time)
        def high_sol (time=200):
            Beep(783*2,time)
        def high_sol_sharp (time=200):
            Beep(830*2,time)
        def high_ra (time=200):
            Beep(880*2,time)
        def high_ra_sharp (time=200):
            Beep(932*2,time)
        def high_si (time=200):
            Beep(987*2,time)


        def main_melody():
            fa_sharp()
            time.sleep(0.2)
            fa_sharp()
            high_do_sharp()
            si()
            time.sleep(0.2)
            ra()
            time.sleep(0.2)
            sol_sharp()
            time.sleep(0.2)
            sol_sharp()
            sol_sharp()
            si()
            time.sleep(0.2)
            ra()
            sol_sharp()
            fa_sharp()
            time.sleep(0.2)
            fa_sharp()
            high_ra()
            high_sol_sharp()
            high_ra()
            high_sol_sharp()
            high_ra()

            fa_sharp()
            time.sleep(0.2)
            fa_sharp()
            high_ra()
            high_sol_sharp()
            high_ra()
            high_sol_sharp()
            high_ra()

        def sub_melody():
            for i in range(4):
                ra(200)

            for i in range(4):
                high_do_sharp(200)

            for i in range(4):
                si(200)
            for i in range(4):
                high_me(200)

            for i in range(12):
                high_fa_sharp(200)

            si(200)
            ra(200)
            sol_sharp(200)
            me(200)
        main_melody()
        sub_melody()


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
        
# ***************************************************************************************************************************
    """Face login system Using facial recognition system"""
    def face_login(self, username):
        known_image = face_recognition.load_image_file("users_facial_data/"+f"{username}.jpg")
        cap = cv.VideoCapture(0)
        while cap.isOpened():
            try:
                if cv.waitKey(1) & 0xFF == ord("q"):
                    break
                ret, frame = cap.read()
                frame = cv.flip(frame, 1)
                cv.rectangle(frame,(175,40),(525,350),(0,255,0),3)
                if cv.waitKey(1) & 0xFF == 13:
                    frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
                    cv.imwrite("filename"+".jpg", frame)
                    known_encoding = face_recognition.face_encodings(known_image)[0]
                    unknown_image = face_recognition.load_image_file("filename.jpg")
                    unknown_encoding = face_recognition.face_encodings(unknown_image)[0]
                    results = face_recognition.compare_faces([known_encoding], unknown_encoding)
                    
                    if results[0]:
                        print("Matched")
                        final_result = True
                        break
                    else:
                        frequency = 2500  # Set Frequency To 2500 Hertz
                        duration = 1000  # Set Duration To 1000 ms == 1 second
                        winsound.Beep(frequency, duration)
            except IndexError:
                    print("No face is Detected ! ! !")
            cv.imshow("Live", frame)
        cap.release()
        cv.destroyAllWindows()
        return final_result
# **********************************************************************************************************************************

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
                    messagebox.showerror("Error", "Invalid Username/Password ! ! !")
                    self.login_clear()
                else:
                    if self.result[0] == self.password1:
                        if self.face_login(self.username1) == True:
                            messagebox.showinfo("login", "Successfully logged in")
                            self.load_backend()
                            self.login_clear()
                            self.counter = 0
                    else:
                        self.counter += 1
                        if self.counter >= 3:
                            messaging.send_error_login()
                            self.err_sound()
                        print(self.counter)
                        messagebox.showerror("Error", "Username or password do not matched")
                        self.login_clear()
            else:
                messagebox.showerror("Error", "Username or password is empty")


        except mysql.connector.Error as e:
            messagebox.showerror("Error", e)

        self.con.close()

    def login_clear(self):
        self.label_username_entry.delete(0, END)
        self.label_password_entry.delete(0, END)


interface = Tk()
gui = Project(interface)
interface.mainloop()
