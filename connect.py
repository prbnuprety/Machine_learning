from tkinter import messagebox
import mysql.connector
from dotenv import load_dotenv
load_dotenv()
import os

class Connection:
    def __init__(self):
        try:
            self.con = mysql.connector.connect(
                host= os.getenv("host"),
                port= os.getenv("port"),
                user= os.getenv("user"),
                passwd= os.getenv("passwd"),
                database= os.getenv("database")
            )

            self.cur = self.con.cursor()

        except mysql.connector.Error as e:
            messagebox.showerror('Database Error', e)


    def close(self):
        self.con.commit()
        self.cur.close()
        self.con.close()