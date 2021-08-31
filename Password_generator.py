from tkinter import *
from PIL import Image, ImageTk
import random
import tkinter.messagebox as tmsg
from tkinter.ttk import Combobox
parent = Tk()
parent.geometry("700x700")
parent.maxsize(700, 700)
parent.minsize(700, 700)
# **************************************************************************Giving max and min size for pPop up Window**************************************
Max_window = 400
Min_window = 400
parent.config(bg="cadet blue")
parent.title("My Password generator")
Sc1 = StringVar()
# ss="Welcome to password Generator"
# count=0
# text=""
# Slider_label=Label(text=ss,font="aerial 20 bold").place(x=100,y=20)
# Welcome_box()
# Sc1=StringVar()
# Entered_pin
# MAKING OF PASSOWRD MAKEER FUNCTION


def Welcome_box():
    global count, text
    if(count >= len(Welcome_statement)):
        count = -1
        text = ""
        Welcome_label.config(text=text)
    else:
        text = text+Welcome_statement[count]
        Welcome_label.config(text=text)
    count = count+1
    Welcome_label.after(200, Welcome_box)


def password_maker():
    global Sc1
    password = ""
    length = int(length_entry.get())
    Uppercase = "ABCDEFGHIJKLMNOPQRSTQVWXYZ"
    lowercase = "abcdefghijklmonpqrstuvwxyz"
    special = "!@#$%^&*()"
    Mix = Uppercase+lowercase+"123456789"
    Protective = Uppercase+lowercase+"123456789"
    if(combo.get() == "Low_Strength"):
        for i in range(0, length):
            password = password+random.choice(Uppercase)
            Sc1.set(password)
    if (combo.get() == "Medium_Strength"):
        for i in range(0, length):
            password = password + random.choice(Mix)
            Sc1.set(password)
    if (combo.get() == "High_Strength"):
        for i in range(0, length):
            password = password + random.choice(Protective)
            Sc1.set(password)


# **************************************************************function to store the password and datain database********************************************************
def save_password():
    purpose = Purpose_entry.get()
    print(type(purpose))
    pass1 = Sc1.get()
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="admin", database="password_recorder")
    cur = mydb.cursor()
    sql = "INSERT INTO RECORDER(PURPOSE ,PASSWORD) VALUES( %s, %s  )"
    val = (purpose, pass1)
    cur.execute(sql, val)
    mydb.commit()
    print("your Password has been saved")
# *******************************************************************************Function to display the database**************************************************************


def display_password():
    FirstToplevel = Toplevel(parent)
    FirstToplevel.geometry("300x300")
    FirstToplevel.maxsize(Max_window, Min_window)
    FirstToplevel.minsize(Max_window, Min_window)
  # ***************************************************************************************************************************** making labels**********************************
    Pin_label = Label(FirstToplevel, text="Enter your pin").place(x=0, y=0)
    Entrey_pinlabel = Entry(FirstToplevel)
    Entrey_pinlabel.place(x=100, y=0)
    Entered_pin1 = Entrey_pinlabel.get()
 #*********************************************************************   # global Entered_pin=Entered_pin1
    Confirmbutton = Button(FirstToplevel, text="Submit",
                           command=ShowFiles).place(x=0, y=20)


def ShowFiles():
    import mysql.connector
    mydb = mysql.connector.connect(
        host="localhost", user="root", password="admin", database="password_recorder")
    cur = mydb.cursor()

    cur.execute("select pin from pin")
    querry = cur.fetchall()

    Second_TopLevel = Toplevel(parent)
    Second_TopLevel.maxsize(Max_window, Min_window)
    Second_TopLevel.minsize(Max_window, Min_window)
    cur.execute("SELECT * FROM recorder")
    i = 0
    for password in cur:
        for j in range(len(password)):
            e = Entry(Second_TopLevel, font="20,bold", width=10, fg='blue')
            e.grid(row=i, column=j)
            e.insert(END, password[j])
        i = i + 1

#*********************************************************Making Welcome Box**********************************************************************************
Welcome_statement = "Welcome to Password Generator"
count = 0
text = ""
Welcome_label = Label(text=Welcome_statement,
                      font="aerial 20 bold", borderwidth=7, relief=RAISED)
Welcome_label.place(x=100, y=20)
Welcome_box()

# ***********************************************************Inserting Image in the passwordd generator******************************************************************
Photo_png = Image.open("passwordgen.jpg")
Photo_jpg = ImageTk.PhotoImage(Photo_png)
New_image = Label(image=Photo_jpg).place(y=80, x=150)
#
password_label = Label(parent, text="Password", font="aerial 15 bold",
                       borderwidth=7, relief=RAISED).place(x=10, y=400)
password_entry = Entry(parent, textvariable=Sc1, font="aerial 15 italic",
                       borderwidth=7, relief=RAISED, width=35).place(x=150, y=400)
password_entry.configure(state='disabled')
# ****************************************************************Drop Down MENU***************************************************************************************
strength = Label(parent, text="Strength-:", font="aerial 15 bold", borderwidth=7, relief=RAISED).place(x=10, y=450)
lis = ["Low_Strength", "Medium_Strength", "High_Strength"]
combo = Combobox(parent, values=lis, width=50, font="aerial 10 bold")
combo.place(x=140, y=460)
combo.set("Select")
#********************************************************************************************** LENGTH Tab****************************************************
length_label = Label(parent, text="LENGTH", font="aerial 15 bold",
                     borderwidth=7, relief=RAISED).place(x=10, y=500)
length_entry = Entry(parent, font="aerial 15 italic",
                     borderwidth=7, relief=RAISED)
length_entry.place(x=150, y=500)
# purpose tab*****************************************************************
Purpose_label = Label(parent, text="Purpose", font="aerial 15 bold",
                      borderwidth=7, relief=RAISED).place(x=10, y=550)
Purpose_entry = Entry(parent, font="aerial 15 italic",
                      borderwidth=7, relief=RAISED)
Purpose_entry.place(x=150, y=550)
# Generate tab**************************************************
Generate_Button = Button(parent, text="Genrate", command=password_maker,
                         font="aerial 15 bold", borderwidth=7, relief=RAISED).place(y=620, x=10)
# Save button********************************************************
save_button = Button(parent, text="Save", command=save_password,
                     font="aerial 15 bold", borderwidth=7, relief=RAISED).place(y=620, x=200)
# adding menu bar
menubar = Menu(parent, font="bold")
menubar.add_command(label="Display password", command=display_password)
menubar.add_command(label="Quit", command=parent.quit)
parent.config(menu=menubar)
parent.mainloop()
