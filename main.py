print("I love Python!")

#Imported Modules --> tkinter, Open cv and mysql connector
import tkinter as tk
from tkinter import *
import mysql.connector
import cv2 as cv

#created MySQL database  STUDENT_PROFILE connection
db = mysql.connector.connect(host="localhost", user="root", password="shree@18", database="student_profile")

#The main Window from where we can select multiple options for required services
def mainWindow():
    window = tk.Tk()
    window.geometry('420x290')
    window.title("Student Manager")
    title = Label(window,text="STUDENT MANAGEMENT SYSTEM",bg="blue",fg="white",bd=5,relief=RAISED,padx=5,font=("cambria",20))
    title.pack()

    #Main Frame with options to select
    frame = Frame(window,bg="#4d0099",width=400,height=400)
    frame.pack()
    studentProfileOption = Label(frame,text="STUDENT PROFILE",font=("cambria",24),bg="#ccffcc")
    studentProfileOption.grid(row=0,column=0)

    btn1= Button(frame,text="GO",font=("cambria",22),relief=RAISED,command=lambda:profileDetails(),bg="#99ff22")
    btn1.grid(row=0,column=2)

    attendanceOption = Label(frame, text="STUDENT ATTENDANCE", font=("cambria", 24), bg="#ccffcc")
    attendanceOption.grid(row=1, column=0)

    btn2 = Button(frame, text="GO", font=("cambria", 22), relief=RAISED,command=lambda:studentAttendance(),bg="#99ff22")
    btn2.grid(row=1, column=2)

    updatesOption = Label(frame, text="LATEST UPDATES", font=("cambria", 24), bg="#ccffcc")
    updatesOption.grid(row=2, column=0)

    btn3 = Button(frame, text="GO", font=("cambria", 22), relief=RAISED,command=lambda:latestUpdates(),bg="#99ff22")
    btn3.grid(row=2, column=2)

    scheduleOption = Label(frame, text="TODAY'S SCHEDULE", font=("cambria", 24), bg="#ccffcc")
    scheduleOption.grid(row=3, column=0)

    btn4 = Button(frame, text="GO", font=("cambria", 22), relief=RAISED, command=lambda:studentTimeTable(),bg="#99ff22")
    btn4.grid(row=3, column=2)

    window.mainloop()

# Profile Details Window
def profileDetails():
    global sn
    window1 = tk.Tk()
    window1.geometry('750x400')
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

    """addbtn = Button(frame1,text="ADD",font=("cambria", 12))
    addbtn.grid(row=2,column=3)"""

    # Created MySql Database connection to fetch Records using mysql connector module.
    cur = db.cursor()

    """def addDetails():
        a = StringVar(frame1)
        b = StringVar(frame1)
        c = StringVar(frame1)
        d = StringVar(frame1)
        e = StringVar(frame1)
        
        
        cur.execute("Insert into tybsc_cs values({},{},{},{},{})".format(a,b,c,d,e))"""


    # Next Frame to show all Student Details.
    frame2 = Frame(window1,width = 200, height = 200)
    frame2.pack(side = LEFT)

    # Declared Variables to set values in the entry section
    nameFetch = StringVar(frame2)
    divisionFetch = StringVar(frame2)
    courseFetch = StringVar(frame2)
    uin_noFetch = StringVar(frame2)
    attenFetch = StringVar(frame2)

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


    attendanceLabel= Label(frame2, text="MONTHLY ATTENDANCE :", bd=5, relief=FLAT, padx=5, font=("cambria", 14))
    attendanceLabel.grid(row=5, column=0)

    attendance= Entry(frame2, font=("cambria", 12),textvariable=attenFetch)
    attendance.grid(row=5, column=1)

    uin = Label(frame2, text="UIN NO. :", bd=5, relief=FLAT, padx=5, font=("cambria", 14))
    uin.grid(row=6, column=0)

    uinNo = Entry(frame2, font=("cambria", 12),textvariable=uin_noFetch)
    uinNo.grid(row=6, column=1)

    student_details = Label(frame2, text="Other Details :", bd=5, relief=FLAT, padx=5, font=("cambria", 14))
    student_details.grid(row = 2, column = 4)

    stud = Entry(frame2, font=("cambria", 12))
    stud.grid(row=2, column=5)

    # Created Function to get details to fetch information and set them by executing queries
    def getDatad():
        global getRollNo,getDiv
        getRollNo = int(roll1.get())
        getDiv = getDivision.get()

        # fetch name from table
        cur.execute(("select name from TYBSC_CS where rollno={} and division={}".format(getRollNo,getDiv)))
        result = cur.fetchall()
        nameFetch.set(result)
        # fetch division from table
        cur.execute(("select division from TYBSC_CS where rollno={} and division={}".format(getRollNo,getDiv)))
        result1 = cur.fetchall()
        divisionFetch.set(result1)
        # fetch course from table
        cur.execute(("select course from TYBSC_CS where rollno={} and division={}".format(getRollNo,getDiv)))
        result2 = cur.fetchall()
        courseFetch.set(result2)
        # fetch uin_no from table
        cur.execute(("select uin_no from TYBSC_CS where rollno={} and division={}".format(getRollNo,getDiv)))
        result3 = cur.fetchall()
        uin_noFetch.set(result3)
        # fetch Monthly Attendance from table
        cur.execute(("select Monthly_Attendance from TYBSC_CS where rollno={} and division={}".format(getRollNo, getDiv)))
        result4 = cur.fetchall()
        attenFetch.set(result4)
        cur.close()


    window1.mainloop()



# Capture pic for attendance and add daily attendance to students database.
# Use OpenCV capture image of user and store present for each valid face detection.
# Store the image into database BLOB
def studentAttendance():
    win = tk.Tk()
    win.geometry('900x250')
    win.title("Student profile")
    l = Label(win, text="STUDENT ATTENDANCE", bg="blue", fg="white", bd=5, relief=RAISED, padx=5,
              font=("cambria", 20))
    l.pack()

    # Give Attendance Frame
    f = Frame(win)

    f.pack()
    def click():
        getr = StringVar(f)
        lroll = Label(f,text="Enter Roll No:- ",font=("Cambria",15))
        lroll.grid(row=0,column=0)
        e1roll = Entry(f,font=("Cambria",15),textvariable=getr)
        e1roll.grid(row=0,column=1)

        im = cv.VideoCapture(0, cv.CAP_DSHOW)
        count = 0
        while True:
            ret, img = im.read()
            cv.imshow("Test", img)
            if not ret:
                break
            k = cv.waitKey(1)
            if k % 256 == 27:
                print("Close")
                break
            elif k % 256 == 32:
                print("Image" + str(count) + "saved")
                file = "C://Users//HP//Desktop//imagecv" + str(count) + ".jpg"
                cv.imwrite(file, img)
                count += 1

        im.release()
        cv.destroyAllWindows()

    # Two options (Buttons) 1. To Give Attendance 2. Attendance Details of Student accor. to Roll-No
    giveAttn = Button(f, text="Give Attendance", font=("cambria", 14),fg="#fff", bg="#544725",relief=RAISED,command=lambda: click())
    giveAttn.grid(row=2, column=0)

    checkattn = Button(f,text="Attendance Details",font=("cambria", 14),bg="#9600c4",fg="#fff",relief=RAISED,command= lambda :attnDetails())
    checkattn.grid(row=2,column=1)

    attnD = db.cursor()     # MySQL connection on top!
        
    # Attendance details
    def attnDetails():
        f1 = Frame(win)
        f1.pack()

        getroll = StringVar(f1)

        # For Attendace Details Enter Roll No and Click on OK!
        lroll = Label(f1,text="Enter Roll No:- ",font=("Cambria",15))
        lroll.grid(row=0,column=0)
        e1roll = Entry(f1,font=("Cambria",15),textvariable=getroll)
        e1roll.grid(row=0,column=1)
        btn = Button(f1,text="OK",font=("Cambria",15),bg="#1f4a29",fg="#fff",command=lambda :showAttnDetails())
        btn.grid(row=0,column=2)

        # After clicking OK fetch details of a students from Attn_details database and display it on the frame
        def showAttnDetails():
            # Labels to show details
            l1 = Label(f1, text="Roll No: ", font=("Cambria", 15))
            l1.grid(row=1, column=0)
            l2 = Label(f1, text="Month: ", font=("Cambria", 15))
            l2.grid(row=1, column=1)
            l3 = Label(f1, text="Total Working Days: ", font=("Cambria", 15))
            l3.grid(row=1, column=2)
            l4 = Label(f1, text="Present Days: ", font=("Cambria", 15))
            l4.grid(row=1, column=3)
            l5 = Label(f1, text="Average Attendance: ", font=("Cambria", 15))
            l5.grid(row=1, column=4)

            # Details displaying after user input roll no
            k = int(getroll.get())
            attnD.execute(("SELECT * FROM ATTN_DETAILS WHERE ROLLNO={}".format(k)))
            i = 3
            for attn_details in attnD:
                for j in range(len(attn_details)):
                    e = Text(f1, width=15, height=1, fg='#01114d', bg='#d9ffd4', font=("cambria", 12))
                    e.grid(row=i, column=j)
                    e.insert(END, attn_details[j])
                i = i + 1


# Updates or important notices if any can be shown in latest updates.
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


# Student time table created according to teachers schedule and availability.
def studentTimeTable():
    win = tk.Tk()
    win.geometry('700x260')
    win.title("Student profile")
    l = Label(win, text="TODAY'S SCHEDULE", bg="blue", fg="white", bd=5, relief=RAISED, padx=5,font=("cambria", 20))
    l.pack()

    # Created 3 course options to see TimeTable.
    f = Frame(win)
    f.pack()
    # From BSC Course three years 1st 2nd and 3rd.
    courseOptions=['FYBSC-CS','SYBSC-CS','TYBSC-CS']

    # Created variables for options menu to select and default value is set.
    var = StringVar(f)
    variable = StringVar(f)
    variable.set("Select Course")
    var.set("Select Division")

    course = Label(f,text="Course :",font=("cambria",15 ))
    course.grid(row=0,column=0)
    # Select Courses from given options OPTIONS MENU.
    options_menu = OptionMenu(f,variable,*courseOptions,command=lambda y:sel())
    options_menu.config(bg="#efba00",fg="#fff",font=("cambria", 15))
    options_menu.grid(row=0,column=1)

    division = Label(f, text="DIV :", font=("cambria", 15))
    division.grid(row=0, column=2)
    # Select Division from given OPTIONS MENU
    option_menu_div = OptionMenu(f,var,*('1','2'),command=lambda x:sel())
    option_menu_div.config(bg="#efba00",fg="#fff",font=("cambria", 15))
    option_menu_div.grid(row=0,column=3)

    # Created new frame to display schedule / Time table
    fr = Frame(win)
    fr.pack()

    """ Defined function to get the values from options menu by using get()
    Also Created connection for MySQL database to fetch the values/ whole schedule table from Tschedule and 
    Tschedulei Tables from Student_profile database. 
    Topics:
    ---------------------------------------------------------------------------------------------------------------
    buffered - MysqlCursorBuffered() is used where multiple queries with small result sets needs to be combined or
    computed with each other. It fetches the entire result set (all the rows) from the server and buffers the rows.
    .cursor(buffered = True Argument) : Only the current cursor will buffer the results.
    ---------------------------------------------------------------------------------------------------------------
    """

    def sel():
        k = variable.get()
        m = var.get()
        tcur = db.cursor(buffered=True)

        if k == "TYBSC-CS" and m == "1":
            tcur.execute("SELECT * FROM TSCHEDULE")
            i = 0
            for tschedule in tcur:
                for j in range(len(tschedule)):
                    e = Text(fr, width=20, height=1, fg='blue', bg='Yellow',font=("cambria", 12))
                    e.grid(row=i, column=j)
                    e.insert(END, tschedule[j])
                i = i + 1

        elif k == "TYBSC-CS" and m == "2":
            tcur.execute(("SELECT * FROM TSCHEDULEI"))
            i = 0
            for tschedulei in tcur:
                for j in range(len(tschedulei)):
                    e = Text(fr,width=20,height=1,fg='RED', bg='Yellow',font=("cambria", 12))
                    e.grid(row=i, column=j)
                    e.insert(END, tschedulei[j])
                i = i + 1

        tcur.close()


mainWindow()


"""
   Topics : 
   ------------------------------------------------------------------------------------------------------------
   To Create a MYSQL connection. 
   mysql.connector.connect() ->  The connect() constructor creates a connection to MySql server and returns
   MySQLConnection object
   ============================================================================================================ 
   .cursor() -> create Cursor object using cursor() method.
   Using the methods of it can execute SQL statements, fetch data from the result sets, call procedures.
   ------------------------------------------------------------------------------------------------------------
   open cv -->  Open source Library for Computer Vision, Machine Learning and Image Processing

"""
