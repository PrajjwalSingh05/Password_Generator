from tkinter import *
from PIL import Image,ImageTk
import  random
import tkinter.messagebox as tmsg

from  tkinter.ttk import Combobox
parent=Tk()
parent.geometry("700x700")
parent.maxsize(700,700)
parent.minsize(700,700)
parent.config(bg="cadet blue")
parent.title("My Password generator")
Label(text="MY PASSWORD GENERATOR ",font="aerial 20 bold").place(x=100,y=20)
Sc1=StringVar()
#MAKING OF PASSOWRD MAKEER FUNCTION
def password_maker():
    global  Sc1
    password=""
    length=int(length_entry.get())
    Uppercase="ABCDEFGHIJKLMNOPQRSTQVWXYZ"
    lowercase="abcdefghijklmonpqrstuvwxyz"
    special="!@#$%^&*()"
    Mix=Uppercase+lowercase+"123456789"
    Protective=Uppercase+lowercase+"123456789"
    if(combo.get()=="Low_Strength"):
        for i in range(0,length):
            password=password+random.choice(Uppercase)
            Sc1.set(password)
    if (combo.get() == "Medium_Strength"):
        for i in range(0, length):
            password = password + random.choice(Mix)
            Sc1.set(password)
    if (combo.get() == "High_Strength"):
        for i in range(0, length):
            password = password + random.choice(Protective)
            Sc1.set(password)

#function to store the password in database
def save_password():
    purpose=Purpose_entry.get()
    pass1=Sc1.get()
    import mysql.connector
    mydb = mysql.connector.connect(host="localhost", user="root", password="admin", database="password_recorder")
    cur = mydb.cursor()
    sql = "INSERT INTO RECORDER(PURPOSE ,PASSWORD) VALUES( %s, %s  )"
    val =(purpose,pass1)
    cur.execute(sql, val)
    mydb.commit()
    print("your Password has been saved")


#inserting Image in the passwordd generator
Photo_png=Image.open("passwordgen.jpg")
Photo_jpg=ImageTk.PhotoImage(Photo_png)
New_image=Label(image=Photo_jpg).place(y=80,x=150)
#
password_label=Label(parent,text="password",font="aerial 15 bold",borderwidth=7,relief=RAISED).place(x=10,y=400)
password_entry=Entry(parent,textvariable=Sc1,font="aerial 15 italic",borderwidth=7,relief=RAISED,width=35).place(x=150,y=400)
#drop Down MENU

strength=Label(parent,text="strength-:",font="aerial 15 bold",borderwidth=7,relief=RAISED).place(x=10,y=450)
lis=["Low_Strength","Medium_Strength","High_Strength"]
combo=Combobox(parent,values=lis,width=50,font="aerial 10 bold")
combo.place(x=140,y=460)
combo.set("Select")
#LENGTH
length_label=Label(parent,text="LENGTH",font="aerial 15 bold",borderwidth=7,relief=RAISED).place(x=10,y=500)
length_entry=Entry(parent,font="aerial 15 italic",borderwidth=7,relief=RAISED)
length_entry.place(x=150,y=500)
Purpose_label=Label(parent,text="Purpose",font="aerial 15 bold",borderwidth=7,relief=RAISED).place(x=10,y=550)
Purpose_entry=Entry(parent,font="aerial 15 italic",borderwidth=7,relief=RAISED)
Purpose_entry.place(x=150,y=550)
Generate_Button=Button(parent,text="Genrate",command=password_maker,font="aerial 15 bold",borderwidth=7,relief=RAISED).place(y=620,x=10)
save_button=Button(parent,text="save",command=save_password,font="aerial 15 bold",borderwidth=7,relief=RAISED).place(y=620,x=200)
parent.mainloop()
