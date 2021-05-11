print("I love Python!")

#Imported Modules, tkinter and mysql connector
import tkinter as tk
from tkinter import *
import mysql.connector

#The main Window from where we can select multiple options for required services
def mainWindow():
    window = tk.Tk()
    window.geometry('430x300')
    window.title("Student Manager")
    title = Label(window,text="STUDENT MANAGEMENT SYSTEM",bg="blue",fg="white",bd=5,relief=RAISED,padx=5,font=("cambria",20))
    title.pack()

    #Main Frame with options to select
    frame = Frame(window,bg="#487fff",width=400,height=400)
    frame.pack()
    studentProfileOption = Label(frame,text="STUDENT PROFILE",font=("cambria",20),bg="#487fff")
    studentProfileOption.grid(row=0,column=0)

    btn1= Button(frame,text="GO",font=("cambria",20),relief=RAISED,command=lambda:profileDetails(),bg="#99ff22")
    btn1.grid(row=0,column=2)

    attendanceOption = Label(frame, text="STUDENT ATTENDANCE", font=("cambria", 20), bg="#487fff")
    attendanceOption.grid(row=1, column=0)

    btn2 = Button(frame, text="GO", font=("cambria", 20), relief=RAISED,command=lambda:studentAttendance(),bg="#99ff22")
    btn2.grid(row=1, column=2)

    updatesOption = Label(frame, text="LATEST UPDATES", font=("cambria", 20), bg="#487fff")
    updatesOption.grid(row=2, column=0)

    btn3 = Button(frame, text="GO", font=("cambria", 20), relief=RAISED,command=lambda:latestUpdates(),bg="#99ff22")
    btn3.grid(row=2, column=2)

    scheduleOption = Label(frame, text="TODAY'S SCHEDULE", font=("cambria", 20), bg="#487fff")
    scheduleOption.grid(row=3, column=0)

    btn4 = Button(frame, text="GO", font=("cambria", 20), relief=RAISED, command=lambda:studentTimeTable(),bg="#99ff22")
    btn4.grid(row=3, column=2)

    window.mainloop()

# Profile Details Window
def profileDetails():
    global sn
    window1 = tk.Tk()
    window1.geometry('650x400')
    window1.title("Student profile")
    title1 = Label(window1, text="STUDENT PROFILE", bg="blue", fg="white", bd=5, relief=RAISED, padx=5,font=("cambria", 20))
    title1.pack()

    frame1 = Frame(window1)
    frame1.pack(side = TOP)
    # Take details from user to fetch all records
    lab = Label(frame1, text="ROLL NO :-", bd=5, relief=FLAT, padx=5,font=("cambria", 14))
    lab.grid(row=0, column=0)

    roll1 = Entry(frame1, font=("cambria", 12))
    roll1.grid(row=0, column=1)

    lb = Label(frame1,text="Div:-", bd=5, relief=FLAT, padx=5,font=("cambria", 14))
    lb.grid(row=0,column=2)

    getDivision = Entry(frame1, font=("cambria", 12))
    getDivision.grid(row=0, column=3)

    btn = Button(frame1,text="ENTER",font=("cambria", 12),command=lambda:getDatad())
    btn.grid(row=1,column=1)

    # Next Frame to show all Student Details.
    frame2 = Frame(window1,width = 200, height = 200)
    frame2.pack(side = LEFT)

    # Declared Variables to set values in the entry section
    nameFetch = StringVar(frame2)
    divisionFetch = StringVar(frame2)
    courseFetch = StringVar(frame2)
    uin_noFetch = StringVar(frame2)

    label= Label(frame2,text="STUDENT NAME  :",bd=5, relief=FLAT, padx=5,font=("cambria", 14))
    label.grid(row =2,column=0)

    student_name = Entry(frame2,textvariable=nameFetch,font=("cambria", 12))
    student_name.grid(row =2 ,column=1)

    labelDiv = Label(frame2,text="DIV :",bd=5, relief=FLAT, padx=5,font=("cambria", 14))
    labelDiv.grid(row =3,column=0)

    division = Entry(frame2, font=("cambria", 12),textvariable=divisionFetch)
    division.grid(row=3, column=1)

    courseLabel = Label(frame2,text="COURSE :",bd=5, relief=FLAT, padx=5,font=("cambria", 14))
    courseLabel.grid(row =4,column=0)

    course = Entry(frame2, font=("cambria", 12),textvariable=courseFetch)
    course.grid(row=4, column=1)

    # Remianing to add in db
    attendanceLabel= Label(frame2, text="MONTHLY ATTENDANCE :", bd=5, relief=FLAT, padx=5, font=("cambria", 14))
    attendanceLabel.grid(row=5, column=0)
    attendance= Entry(frame2, font=("cambria", 12))
    attendance.grid(row=5, column=1)

    uin = Label(frame2, text="UIN NO. :", bd=5, relief=FLAT, padx=5, font=("cambria", 14))
    uin.grid(row=6, column=0)

    uinNo = Entry(frame2, font=("cambria", 12),textvariable=uin_noFetch)
    uinNo.grid(row=6, column=1)

    # Created MySql Database connection to fetch Records using mysql connector module.
    db = mysql.connector.connect(host="localhost", user="root", password="shree@18", database="student_profile")
    cur = db.cursor()

    # Created Function to get details to fetch information and set them by executing queries
    def getDatad():
        global getRollNo,getDiv
        getRollNo = int(roll1.get())
        getDiv = getDivision.get()

        # fetch name from table
        cur.execute(("select name from SYBSC_CS where roll_no={} and division={}".format(getRollNo,getDiv)))
        result = cur.fetchall()
        nameFetch.set(result)
        # fetch division from table
        cur.execute(("select division from SYBSC_CS where roll_no={} and division={}".format(getRollNo,getDiv)))
        result1 = cur.fetchall()
        divisionFetch.set(result1)
        # fetch course from table
        cur.execute(("select course from SYBSC_CS where roll_no={} and division={}".format(getRollNo,getDiv)))
        result2 = cur.fetchall()
        courseFetch.set(result2)
        # fetch uin_no from table
        cur.execute(("select uin_no from SYBSC_CS where roll_no={} and division={}".format(getRollNo,getDiv)))
        result3 = cur.fetchall()
        uin_noFetch.set(result3)



    window1.mainloop()



# Pending to do
def studentAttendance():
    win = tk.Tk()
    win.geometry('800x600')
    win.title("Student profile")
    l = Label(win, text="STUDENT ATTENDANCE", bg="blue", fg="white", bd=5, relief=RAISED, padx=5,
              font=("cambria", 20))
    l.pack()
    f = Frame(win, bg="#487fff")
    f.pack()

def latestUpdates():
    win = tk.Tk()
    win.geometry('500x400')
    win.title("Student profile")
    l = Label(win, text="LATEST UPDATES", bg="blue", fg="white", bd=5, relief=RAISED, padx=5,
              font=("cambria", 20))
    l.pack()
    f = Frame(win, bg="#487fff")
    f.pack()
    t = Text(win,font=("cambria", 20),height=10,width=30)
    t.pack()

def studentTimeTable():
    win = tk.Tk()
    win.geometry('500x400')
    win.title("Student profile")
    l = Label(win, text="TODAY'S SCHEDULE", bg="blue", fg="white", bd=5, relief=RAISED, padx=5,
              font=("cambria", 20))
    l.pack()
    f = Frame(win)
    f.pack()
    courseOptions=['FYBSC-CS','SYBSC-CS','TYBSC-CS']

    var=StringVar(f)
    variable=StringVar(f)
    variable.set("Select Course")
    course = Label(f,text="Course :",font=("cambria",15 ))
    course.grid(row=0,column=0)
    options_menu = OptionMenu(f,variable,*courseOptions)
    options_menu.grid(row=0,column=1)
    division = Label(f, text="DIV :", font=("cambria", 15))
    division.grid(row=0, column=2)
    option_menu_div = OptionMenu(f,var,*('1','2'))
    option_menu_div.grid(row=0,column=3)

    fr=Frame(win)
    fr.pack()
    ls=[("Time","Subject","Teacher","T.Attn"),("7:00-7:45","L.Alg","Preksha dixit",'P'),
        ("7:45-8:25","FOA","Priyanka Sherkhane",'A'),("8:25-9:10",".NET","Pooja Tambe",'P')]

    row=len(ls[0])
    column = len(ls[0])
    for i in range(row):
        for j in range(column):
            e = Entry(fr)
            e.grid(row=i,column=j)
            e.insert(END,ls[i][j])



mainWindow()
