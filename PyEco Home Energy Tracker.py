# Module Setup
from tkinter import *
from tkinter.messagebox import *
import plotly.express as px
import cpuinfo
import tkinter.ttk as ttk
import random
import hashlib
import datetime
from datetime import date
import time
import openpyxl
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,NavigationToolbar2Tk)
import seaborn as sns
from tkinter import filedialog as fd
import pandas as pd

pd.set_option('mode.chained_assignment', None)
import os
from os.path import exists
from email_validator import validate_email, EmailNotValidError
import re
from tkcalendar import Calendar
import smtplib

# Email Setup


# Initial Setup
print(
    "Welcome to the PyEco Home Energy Tracker Project Dev Report Terminal. Developer Functions and actions are available here: ")
print("")

# Windows 1 Setup
root1 = Tk()
root1.geometry("750x500")
root1.title("PyEco Home Energy Tracker [Start Page]")
#root1.iconbitmap('/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/energyicon.icns')
iconimg = Image("photo", file="/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/energyicon.png")
root1.call('wm','iconphoto', root1._w, iconimg)
root1.wm_attributes("-transparent", True)
photo1 = PhotoImage(file=r"/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/energybtn.png")
photoimage1 = photo1.subsample(7, 7)
canvas = Canvas(root1, width=1280, height=720)

signupimg = PhotoImage(file=r"/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/signupbgimg.png")


def signup():
    def handle_focus_in(_):
        if entry1.get() == 'Enter your full name here ex.(John Adams)':
            entry1.delete(0, END)
            entry1.config(fg='black')

    def handle_focus_out(_):
        if entry1.get() == '':
            entry1.delete(0, END)
            entry1.config(fg='gray')
            entry1.insert(0, "Enter your full name here ex.(John Adams)")

    def handle_enter(_):
        entry2.focus_set()
        handle_focus_out('dummy')

    def handle_focus_in1(_):
        if entry2.get() == 'Enter your email here ex.(johnadams@gmail.com)':
            entry2.delete(0, END)
            entry2.config(fg='black')

    def handle_focus_out1(_):
        if entry2.get() == '':
            entry2.delete(0, END)
            entry2.config(fg='gray')
            entry2.insert(0, "Enter your email here ex.(johnadams@gmail.com)")

    def handle_enter1(_):
        entry3.focus_set()
        handle_focus_out1('dummy')

    def handle_focus_in2(_):
        if entry3.get() == 'Enter your password here ex.(John12adams)':
            entry3.delete(0, END)
            entry3.config(fg='black', show='*')

    def handle_focus_out2(_):
        if entry3.get() == '':
            entry3.delete(0, END)
            entry3.config(fg='gray', show='')
            entry3.insert(0, "Enter your password here ex.(John12adams)")

    def handle_enter2(_):
        entry4.focus_set()
        handle_focus_out2('dummy')

    def handle_focus_in3(_):
        if entry4.get() == 'Confirm your password here ex.(John12adams)':
            entry4.delete(0, END)
            entry4.config(fg='black', show='*')

    def handle_focus_out3(_):
        if entry4.get() == '':
            entry4.delete(0, END)
            entry4.config(fg='gray', show='')
            entry4.insert(0, "Confirm your password here ex.(John12adams)")

    def handle_enter3(_):
        handle_focus_out3('dummy')
        answer = askyesno(title="Submit Login?", message="Are you sure you want to submit your sign up form?")
        if answer:
            if entry1.get() == 'Enter your full name here ex.(John Adams)' or entry2.get() == 'Enter your email here ex.(johnadams@gmail.com)' or entry3.get() == 'Enter your password here ex.(John12adams)' or entry4.get() == '':
                showinfo(title="Error",
                         message="Sorry, it seems like you haven't entered an input in one of the fields. Please try again.")
                if entry4.get() == 'Confirm your password here ex.(John12adams)':
                    entry4.delete(0, END)
                    entry4.config(fg='black')
                return "Dev Code: sent back to main window2()"
            everything()
        else:
            entry4.delete(0, END)
            entry4.config(fg='black')

    def emailvalidator(ev):
        global email_valid
        global email_problem
        try:
            # validate and get info
            v = validate_email(ev)
            # replace with normalized form
            email_valid = True
        except EmailNotValidError as e:
            # email is not valid, exception message is human-readable
            email_problem = str(e)

    def everything():
        global password
        global confirm_password
        global name
        global email
        confirm_password = entry4.get()
        name = entry1.get()
        email = entry2.get()
        password = entry3.get()
        if confirm_password == password:
            enc = confirm_password.encode()
            final_pwd = hashlib.md5(enc).hexdigest()
            # User encryption
            file = open('/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/authorization/credentials.txt', 'w')
            file.write("\n" + email + "7419b34lx019")
            file.write(final_pwd + "7419b34lx019")
            file.write(name)
            showinfo(title="Congrats!",
                     message="Nice:) Welcome to your new account, " + name + ". Just login again to start!")
            root_signup.withdraw()
        else:
            showinfo(title="Unmatching Passwords",
                     message="Your passwords don't seem to be matching. Please try again. :/")
        check_pwd()
        if password_strong == True:
            showinfo(title="Password Valid!", message="Your password is valid! Click OK to continue.")
        elif password_strong == False:
            showinfo(title="Password Invalid",
                     message="Sorry your password was invalid. Please try entering a password with at least 8 characters.")
            return "DEV CODE: code to return to signup def function"
        else:
            showinfo(title="Internal Error",
                     message="If you see this there is an internal issue on our part. The program will now restart automatically.")
            quit()
        ev = email
        emailvalidator(ev)
        if email_valid == True:
            showinfo(title="Email Valid",
                     message="Your email is valid! Please check your inbox to see if you get a confirmation email in your inbox.")
            # smtp = smtplib.SMTP('localhost')
            # sender = "riddhiman.rana@gmail.com"
            # reciever = email
            # subject = "CONFIRMATION EMAIL: PyEco Home Energy Tracker"
            # body = "Hey there, " + name + ". This is a confirmation email to make sure that you have inputted the correct email address. You will also receive any reports with your home energy information here. Hope you enjoy this program! \n Sincerely, \n The PyEco Program Team"
            # msg = 'subject: ' + subject + '\n\n' + body
            # smtp.sendmail('sender', reciever, msg)
        elif email_valid == False:
            print("Invalid Email")
            showinfo(title="Invalid Email",
                     message="It seems like your email address is invalid. Check your email or try a different email address.")
            return "DEV CODE: invalid email returning back to regular program"
        else:
            showinfo(title="Internal Error",
                     message="Sorry it seems like we had an internal error. The program will now auto-restart.")
            quit()

    def check_pwd():
        l, u, p, d = 0, 0, 0, 0
        s = entry3.get()
        if s == 'Enter your password here ex.(John12Adams)':
            showinfo(title="No password warning",
                     message="Sorry, it seems like you didn't enter a password, please try again.")
            return "DEV Code: returning to main because of no password warning"
        if len(s) >= 8:
            global password_strong
            for i in s:

                # counting lowercase alphabets
                if i.islower():
                    l += 1

                    # counting uppercase alphabets
                if i.isupper():
                    u += 1

                    # counting digits
                if i.isdigit():
                    d += 1

                    # counting the mentioned special characters
            if i == '@' or i == '$' or i == '_' or i == '*' or i == '&' or i == '^':
                p += 1

            if len(s) >= 8:
                pwd_strength.config(text="Weak Password", fg='orange')
                password_strong = True
            if d >= 1 or l >= 2 or u >= 2 or p >= 1:
                pwd_strength.config(text="Medium Password", fg='yellow')
                password_strong = True
            if d >= 1 and l >= 2 and p >= 1 and l >= 1:
                pwd_strength.config(text="Strong Password", fg='green')
                password_strong = True
            if l >= 4 and u >= 2 and p >= 2 and d >= 3 and l + p + u + d == len(s):
                print("Valid Password")
                password_strong = True
                pwd_strength.config(
                    text="That's a really strong password! Make sure it's something you can remember though because you will need this later to login.",
                    fg='#1b7ced')
        else:
            print("Invalid Password")
            pwd_strength.config(text="Invalid Password. You need at least 8 characters for your password.", fg='red')
            password_strong = False

    def toggle_pass():
        if entry3.cget('show') == '':
            if entry3.get() == 'Enter your password here ex.(John12adams)':
                entry3.config(show='')
            elif entry4.get() == 'Confirm your password here ex.(John12adams)':
                entry4.config(show='')
            else:
                entry3.config(show='*')
                entry4.config(show='*')
                print("Password Hidden")
                pwd_button.config(text="Show Password")
                warninglabel.config(text="Password hidden", fg="green")

        elif entry3.cget('show') == '*':
            entry3.config(show='')
            entry4.config(show='')
            print("Password Hidden")
            pwd_button.config(text="Hide Password")
            warninglabel.config(text="WARNING! Your password is being shown right now.", fg="red")
        else:
            print("Sorry there was an internal error. Please restart the program.")
            showinfo(title="ERROR", message="Sorry there was an internal error. Please restart the program.")

    root_signup = Toplevel()
    root_signup.geometry("750x500")
    signupbg = Label(root_signup, image=signupimg)
    signupbg.place(x=0, y=0)
    signuplabel = Label(root_signup, text="Fill out these details to sign up now!", font=('DIN Alternate', 23),
                        compound=RIGHT)
    root_signup.wm_attributes("-transparent", True)
    signuplabel.pack()
    entry1 = Entry(root_signup, width=34, borderwidth=5, fg='gray', bg='white')
    entry1.pack()
    entry1.insert(0, "Enter your full name here ex.(John Adams)")
    entry1.bind("<FocusIn>", handle_focus_in)
    entry1.bind("<FocusOut>", handle_focus_out)
    entry1.bind("<Return>", handle_enter)

    entry2 = Entry(root_signup, width=34, borderwidth=5, fg='gray', bg='white')
    entry2.pack()
    entry2.insert(0, "Enter your email here ex.(johnadams@gmail.com)")
    entry2.bind("<FocusIn>", handle_focus_in1)
    entry2.bind("<FocusOut>", handle_focus_out1)
    entry2.bind("<Return>", handle_enter1)

    entry3 = Entry(root_signup, width=34, borderwidth=5, bg='white', fg='gray')
    entry3.pack()
    entry3.insert(0, "Enter your password here ex.(John12adams)")
    warninglabel = Label(root_signup, text="Password hidden", fg="green")
    warninglabel.pack()
    pwd_button = Button(root_signup, text="Show Password", command=toggle_pass)
    pwd_button.pack()

    entry3.bind("<FocusIn>", handle_focus_in2)
    entry3.bind("<FocusOut>", handle_focus_out2)
    entry3.bind("<Return>", handle_enter2)
    pwd_strength = Label(root_signup,
                         text="Click check password to check your password strength. You need at least than 8 characters for your password.",
                         fg='black')
    pwd_strength.pack()
    entry4 = Entry(root_signup, width=34, borderwidth=5, bg='white', fg='gray')
    entry4.pack()
    entry4.insert(0, "Confirm your password here ex.(John12adams)")
    entry4.bind("<FocusIn>", handle_focus_in3)
    entry4.bind("<FocusOut>", handle_focus_out3)
    entry4.bind("<Return>", handle_enter3)
    checkpwdbtn = Button(root_signup, text="Check Password Strength", command=check_pwd)
    checkpwdbtn.pack()
    saveallbtn = Button(root_signup, text="Save all info", command=everything)
    saveallbtn.pack()


# Window 2 Destroy and Setup and UI
def window2():
    def handle_focus_in1(_):
        if entry1.get() == 'Enter your email here':
            entry1.delete(0, END)
            entry1.config(fg='black')

    def handle_focus_out1(_):
        if entry1.get() == '':
            entry1.delete(0, END)
            entry1.config(fg='gray')
            entry1.insert(0, "Enter your email here")

    def handle_enter1(_):
        entry2.focus_set()
        handle_focus_out1('dummy')

    def handle_focus_in(_):
        if entry2.get() == 'Enter your password here':
            entry2.delete(0, END)
            entry2.config(fg='black', show='*')

    def handle_focus_out(_):
        if entry2.get() == '':
            entry2.delete(0, END)
            entry2.config(fg='gray', show='')
            entry2.insert(0, "Enter your password here")

    def handle_enter(_):
        handle_focus_out('dummy')
        answer = askyesno(title="Submit Login?", message="Are you sure you want to login?")
        if answer:
            if entry2.get() == '' or entry1.get() == '':
                showinfo(title="Error",
                         message="Sorry, it seems like you haven't entered an input in one of the fields. Please try again.")
                return "Dev Code: sent back to main window2()"
            login()

    print("Window 1 Closed. Windows 2 Opened. UI2 Built. Developer Signal = [root2]")
    global root2
    global introlabel2
    global exitbutton1
    global entry1
    global btnwait
    global bgimg2
    global bglabel2
    global profilelabel

    def toggle_pass():
        if entry2.cget('show') == '':
            if entry2.get() == 'Enter your password here':
                entry2.config(show='')
            else:
                entry2.config(show='*')
                print("Password Hidden")
                pwdbtn.config(text="Show Password")
                warninglabel.config(text="Password hidden", fg="green")

        elif entry2.cget('show') == '*':
            entry2.config(show='')
            print("Password Shown")
            pwdbtn.config(text="Hide Password")
            warninglabel.config(text="WARNING! Your password is being shown right now.", fg="red")
        else:
            print("Sorry there was an internal error. Please restart the program.")
            showinfo(title="ERROR", message="Sorry there was an internal error. Please restart the program.")

    def login():
        email = entry1.get()
        password = entry2.get()
        auth = password.encode()
        auth_hash = hashlib.md5(auth).hexdigest()
        f = open("/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/authorization/credentials.txt", "r")
        file_content = f.read()
        users = file_content.split("\n")
        while "" in users:
            users.remove("")
        var = 0
        for user in users:
            global stored_name
            global stored_email
            global stored_pwd

            user_array = user.split("7419b34lx019")
            stored_email = str(user_array[0])
            stored_pwd = str(user_array[1])
            stored_name = str(user_array[2])
            f.close()
            var += 1

        if email == stored_email and auth_hash == stored_pwd:
            print("Logged in Successfully!")
            firstname = stored_name.split()
            greetings = ['Whats up, ', 'How are you doing, ', 'Hey there, ', "How's your day going, "]
            greetingsrandom = str(random.sample(greetings, 1))
            showinfo(title="Success!",
                     message=greetingsrandom[2:-2] + firstname[0] + "! You'll be redirected to your dashboard soon.")
            dashboard()
        else:
            print("Login failed! \n")
            showinfo(title="Failed!",
                     message="Sorry, it seems like either your email or password is wrong. Please try again.")

    root2 = Toplevel()
    root1.withdraw()
    root2.geometry("750x500")
    #root2.iconbitmap('/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/energyicon.icns')
    root2.title("PyEco Home Energy Tracker [Login Page]")
    root2.wm_attributes("-transparent", True)
    bgimg2 = PhotoImage(file="/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/loginbgimg.png")
    bglabel2 = Label(root2, image=bgimg2)
    bglabel2.place(x=0, y=0)
    startlabel1 = Label(root2, text="Please enter your login email, and password.",
                        font=('DIN Alternate', 23), compound=RIGHT)
    startlabel1.pack(pady=20)
    entry1 = Entry(root2, width=25, borderwidth=5, bg='white', fg='gray')
    entry1.pack()
    entry1.insert(0, "Enter your email here")
    entry1.bind("<FocusIn>", handle_focus_in1)
    entry1.bind("<FocusOut>", handle_focus_out1)
    entry1.bind("<Return>", handle_enter1)

    entry2 = Entry(root2, width=25, borderwidth=5, bg='white', fg='gray')
    entry2.pack()
    entry2.insert(0, "Enter your password here")
    entry2.bind("<FocusIn>", handle_focus_in)
    entry2.bind("<FocusOut>", handle_focus_out)
    entry2.bind("<Return>", handle_enter)
    warninglabel = Label(root2, text="Password Hidden", fg='green')
    warninglabel.pack()
    pwdbtn = Button(root2, text="Show Password", command=toggle_pass)
    pwdbtn.pack()
    label = Label(root2, text="Dont have an account?", font=('SF Pro Semibold', 15))
    label.pack(pady=7)
    signupbtn = Button(root2, text="Sign up today!", command=signup)
    signupbtn.pack()
    loginbtn = Button(root2, text="Login", compound=LEFT, cursor='hand2', command=login)
    loginbtn.pack()


bg1 = PhotoImage(file='/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/sunrise.png')
bg2 = PhotoImage(file='/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/noon.png')
bg3 = PhotoImage(file='/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/sunset.png')


def dashboard():
    root_dashboard = Toplevel()
    root2.withdraw()

    root_dashboard.geometry("1280x720")
    root_dashboard.wm_attributes("-transparent", True)
    now = datetime.datetime.now()
    hour = now.hour
    global greeting
    if 12 > hour >= 5:

        bgimagedash = bg1
        # root_dashboard['bg'] = '#f1c581'
        greeting = "Good morning, "
    elif 12 <= hour < 19:

        bgimagedash = bg2
        # root_dashboard['bg'] = '#dbedff'
        greeting = "Good afternoon, "
    else:
        bgimagedash = bg3
        # root_dashboard['bg'] = '#d58cc7'
        greeting = "Good evening, "
    print(hour)
    bglabel = Label(root_dashboard, image=bgimagedash)
    bglabel.place(x=0, y=0)
    welcomelabel = Label(root_dashboard, text=greeting + stored_name + ".", font=("SF Pro Semibold", 40))
    welcomelabel.pack()
    welcomelabel2 = Label(root_dashboard, text="Create a New report, or view past reports.")
    welcomelabel2.pack()
    createnew = Button(root_dashboard, text="Create New Energy Report", command=window3)
    createnew.pack()
    pastlabel = Label(root_dashboard, text="Past Energy Reports: ")
    pastlabel.pack()
    scrollbar = Scrollbar(root_dashboard)
    scrollbar.pack(side=LEFT, fill=Y)
    pastreports = os.listdir('/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/energyreports')
    reportbox = Listbox(root_dashboard, yscrollcommand=scrollbar.set)

    reportbox.pack(side="left", fill=BOTH, expand=0)

    def insertfiles():
        for item in pastreports:
            reportbox.insert(END, item)

    def showcontent(event):
        global folder
        folder = '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/energyreports'
        x = reportbox.curselection()[0]
        filename2 = os.path.join(folder, reportbox.get(x))
        print(filename2)
        if filename2.endswith('.txt'):
            with open(filename2, 'r') as file:
                filename2 = file.read()
            text.config(state=NORMAL)
            text.delete('1.0', END)
            text.insert(END, filename2)
            text.config(state=DISABLED)
        elif filename2.endswith('.png'):
            img = PhotoImage(file=filename2)
            imgcanvas.image = img
            imgcanvas.config(width=570, height=449)
            imgcanvas.create_image(0, 0, image=img, anchor=NW)
        else:
            showinfo(title="Error: Unidentified File type", message="Sorry this filetype can not be opened.")

    imgcanvas = Canvas(root_dashboard)
    imgcanvas.pack(side=LEFT)
    text = Text(root_dashboard, bg='#f4faff')
    text.pack(side=LEFT, fill=BOTH, expand=1)
    scrollbar.config(command=reportbox.yview)
    reportbox.bind("<<ListboxSelect>>", showcontent)
    insertfiles()


cloudup = PhotoImage(file=r'/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/cloudupload.png')
cloudupimg = cloudup.subsample(4, 4)

csvbgimg = PhotoImage(file='/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/csvuploadbg.png')

def window3():

    global root3
    print("Window 2 close. Window 3 Opened. UI3 Built. Developer Signal = [root3]")
    root2.withdraw()
    root3 = Toplevel()
    root3.geometry("1280x720")
    root3.title("PyEco Home Energy Tracker [Import Data Page] v1.0")
    #root3.iconbitmap('/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/energyicon.icns')
    root3.wm_attributes("-transparent", True)
    root3.attributes('-alpha', 0.997)
    bgimg = Label(root3, image=csvbgimg)
    bgimg.place(x=-7, y=-5)

    welcomelabel = Label(root3,
                         text="Welcome to the File Upload Page. Upload your .csv energy report that your energy provider gave you here!",
                         font=('DIN Alternate', 23), compound=RIGHT)
    welcomelabel.pack(side=TOP, pady=50)
    csvuploadbtn = Button(root3, text='Import Data from CSV File', image=cloudupimg, compound=TOP, command=window4, font = ('SF Pro Semibold', 22), cursor="openhand")
    csvuploadbtn.config(background='#C8EE90', foreground='black', width=450, height=350)
    csvuploadbtn.place(relx=0.5, rely=0.5, anchor=CENTER)



def window5check():
    if verified == True:
        window5()
    else:
        showinfo(title='No file uploaded', message="You have not uploaded a file yet.")
        print("Waiting for file to be uploaded")


def select_files():
    global verified
    global filetype
    global filename
    filetype = (('CSV Files', '*.csv'),)
    filename = fd.askopenfilename(title='Open your .csv energy report file', initialdir='/', filetypes=filetype)
    showinfo(title='Selected File', message="You selected file at directory: " + filename)
    if os.path.exists(filename) == True:
        verified = True
    else:
        verified = False


energybgimg = PhotoImage(file='/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/csvicon.png')
energybgimg = energybgimg.subsample(10, 10)
energyuploadbgimg = PhotoImage(file='/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/bgimg3.png')


def window4():
    global verified
    verified = False
    print("Window 3 Closed. Window 4 Opened. UI4 Built. Developer Signal = [root4]")
    global root4
    global filebtn
    root3.withdraw()
    root4 = Toplevel()
    root4.geometry("768x477")
    root4.wm_attributes("-transparent", True)
    root4.title("PyEco Home Energy Tracker [CSV File Import Page]")
    #root4.iconbitmap('/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/energyicon.icns')
    filebtn = Button(root4, text="Choose Energy Report File", fg='black', compound=LEFT, command=select_files,
                     width=240, height=90, image=energybgimg,
                     cursor="openhand")
    filebtn.pack(expand=True)
    global data
    # cal = Calendar(root4, selectmode='year', year=2022, month=8, day=14)
    # cal.pack(pady = 20)
    # enteryear1 = Button(root4, text = "Input Year 1",command = calaccept1)
    # enteryear1.pack(pady = 100)
    # enteryear2 = Button(root4, text="Input Year 2", command = calaccept2)
    # enteryear2.pack(pady=150)
    contbtn2 = Button(root4, text="Continue to Energy Report", font=('Segoe UI Semibold', 11), fg='black', width=30,
                      height=1, command=window5check, cursor="openhand")
    contbtn2.pack(side=BOTTOM, pady=100)


energydatabase = '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/PyEco Home Energy Tracker Appliances Energy Consumption.xlsx'

addeditems = {}
powerconsumption = []
dateadded = []
timeused = []
appliancename = []

def home_appliances():
    # Create the basic dataframe from the user copy dataset
    ha_usercopy = '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/fileusercopyha.xlsx'
    df_ha = pd.read_excel(ha_usercopy)

    def ha_process():
        for index, row in df_ha.iterrows():
            df_ha['Minutes/Day(Moderately Used)'] = pd.to_numeric(df_ha['Minutes/Day(Moderately Used)'], errors='ignore')
            df_ha['Minutes/Week(Rarely Used)'] = pd.to_numeric(df_ha['Minutes/Week(Rarely Used)'],
                                                                  errors='ignore')
            df_ha['Hours/Day(Heavy Use)'] = pd.to_numeric(df_ha['Hours/Day(Heavy Use)'],
                                                                  errors='ignore')
            df_ha['Hours/Week(Not Used Much)'] = pd.to_numeric(df_ha['Hours/Week(Not Used Much)'],
                                                                  errors='ignore')
            df_ha['Weekly kwh'] = pd.to_numeric(df_ha['Weekly kwh'],
                                                                  errors='ignore')
            df_ha['Daily kwh'] = pd.to_numeric(df_ha['Daily kwh'],
                                                                  errors='ignore')
            if int(row['Minutes/Day(Moderately Used)']) > 0:
                df_ha.iloc[index]['Daily kwh'] = int(row['Minutes/Day(Moderately Used)']) / 60000 * int(
                    row['Power Consumption(Watts)'])
                print(df_ha.iloc[index]['Daily kwh'])
                df_ha.iloc[index]['Daily kwh'] = df_ha.iloc[index]['Daily kwh'].astype(int)
                df_ha.to_excel(ha_usercopy, sheet_name="Electronics", index=False)
            elif int(row['Hours/Day(Heavy Use)']) > 0:
                df_ha.iloc[index]['Daily kwh'] = int(row['Minutes/Day(Moderately Used)']) / 1000 * int(
                    row['Power Consumption(Watts)'])
                df_ha.iloc[index]['Daily kwh'] = df_ha.iloc[index]['Daily kwh'].astype(int)
                df_ha.to_excel(ha_usercopy, sheet_name="Electronics", index=False)
            elif int(row['Minutes/Week(Rarely Used)']) > 0:
                df_ha.iloc[index]['Weekly kwh'] = int(row['Minutes/Week(Rarely Used)']) / 60000 * int(
                    row['Power Consumption(Watts)'])
                df_ha.iloc[index]['Weekly kwh'] = df_ha.iloc[index]['Weekly kwh'].astype(int)
                df_ha.to_excel(ha_usercopy, sheet_name="Electronics", index=False)
            elif int(row['Hours/Week(Not Used Much)']) > 0:
                df_ha.iloc[index]['Weekly kwh'] = int(row['Minutes/Week(Rarely Used)']) / 1000 * int(
                    row['Power Consumption(Watts)'])
                df_ha.iloc[index]['Weekly kwh'] = df_ha.iloc[index]['Weekly kwh'].astype(int)
                df_ha.to_excel(ha_usercopy, sheet_name="Electronics", index=False)
            df_ha['Minutes/Day(Moderately Used)'] = pd.to_numeric(df_ha['Minutes/Day(Moderately Used)'],
                                                                  errors='ignore')
            df_ha['Minutes/Day(Moderately Used)'] = df_ha['Minutes/Day(Moderately Used)'].astype(int)
            df_ha['Minutes/Week(Rarely Used)'] = pd.to_numeric(df_ha['Minutes/Week(Rarely Used)'],
                                                               errors='ignore')
            df_ha['Minutes/Week(Rarely Used)'] = df_ha['Minutes/Week(Rarely Used)'].astype(int)
            df_ha['Hours/Day(Heavy Use)'] = pd.to_numeric(df_ha['Hours/Day(Heavy Use)'],
                                                          errors='ignore')
            df_ha['Hours/Day(Heavy Use)'] = df_ha['Hours/Day(Heavy Use)'].astype(int)
            df_ha['Hours/Week(Not Used Much)'] = pd.to_numeric(df_ha['Hours/Week(Not Used Much)'],
                                                               errors='ignore')
            df_ha['Hours/Week(Not Used Much)'] = df_ha['Hours/Week(Not Used Much)'].astype(int)
            df_ha['Weekly kwh'] = pd.to_numeric(df_ha['Weekly kwh'],
                                                errors='ignore')
            df_ha['Weekly kwh'] = df_ha['Weekly kwh'].astype(int)
            df_ha['Daily kwh'] = pd.to_numeric(df_ha['Daily kwh'],
                                               errors='ignore')
            df_ha['Daily kwh'] = df_ha['Daily kwh'].astype(int)

    # Show Item saved in UI
    def item_show():
        global text_ha
        text_ha = clicked.get()
        item_label = Label(root_ha, text="")
        item_label.config(text="You chose: " + text_ha)
        item_label.pack()

    # Show date saved in UI
    def date_show():
        date_label = Label(root_ha, text="")
        date_label.config(text="Selected Date is: " + cal.get_date())
        date_label.pack()

    # Save the time the device is used
    def savetimexlsx():
        time_ha = savetime.get()
        global text_he
        text_he = clicked.get()
        row = df_ha["Appliance Name"] == text_he
        row1 = df_ha.index[row][0]
        df_ha.at[row1, clicked2.get()] = time_ha
        df_ha.to_excel(ha_usercopy, sheet_name="Home Appliances", index=False)

    # Save the Date an appliance is added
    def savedatexlsx():
        global text_he
        print(text_he)
        date_ha = cal.get_date()
        row = df_ha["Appliance Name"] == text_he
        row1 = df_ha.index[row][0]
        df_ha.at[row1, "Date Added"] = date_ha
        df_ha.to_excel(ha_usercopy, sheet_name="Home Appliances", index=False)


    def savetolist():
        global  timeunit
        date_ha = cal.get_date()
        text_he = clicked.get()
        time_ha = int(savetime.get())
        row2 = df_ha["Appliance Name"] == text_he
        row3 = df_ha.index[row2][0]
        power_ha = int(df_ha.at[row3, "Power Consumption(Watts)"])
        if clicked2.get() == "Minutes/Day(Moderately Used)":
            powerconsumption.append((((time_ha/60)*power_ha)/60000)*7)
            timeunit = " minutes per day"
        elif clicked2.get() == "Hours/Day(Heavy Use)":
            powerconsumption.append(((time_ha*power_ha)/60000)*7)
            timeunit = " hours per day"
        elif clicked2.get() == "Minutes/Week(Rarely Used)":
            powerconsumption.append(((time_ha / 60) * power_ha) / 60000)
            timeunit = " minutes per week"
        elif clicked2.get() == "Hours/Week(Not Used Much)":
            powerconsumption.append((time_ha * power_ha) / 60000)
            timeunit = " hours per week"
        else:
            print("error occureed in this part.")
        dateadded.append(date_ha)
        timeused.append(time_ha)
        appliancename.append(text_he)
        #addeditems.append([text_he, power_ha, date_ha, time_ha])

    # Save everything
    def saveall():
        savetolist()
        item_show()
        date_show()
        savetimexlsx()
        savedatexlsx()
        root_ha.withdraw()
        ha_process()

    row_all_ha = []

    # Append Home appliances to dropdown
    appliance_data = pd.read_excel(energydatabase, sheet_name='Home Appliances', skiprows=1)
    for index, row in appliance_data.iterrows():
        row_ha = row['Appliance Name']
        row_all_ha.append(row_ha)

    # Creating UI
    root_ha = Toplevel()
    root_ha.geometry("1280x720")
    root_ha.wm_attributes("-transparent", True)
    today = str(datetime.date.today())
    curr_year = int(today[:4])
    curr_month = int(today[5:7])
    curr_day = int(today[8:10])
    cal = Calendar(root_ha, selectmode='day',
                   year=curr_year, month=curr_month,
                   day=curr_day)
    cal.pack(pady=20)
    clicked = StringVar()
    clicked.set(row_all_ha[0])
    clicked2 = StringVar()
    drop = OptionMenu(root_ha, clicked, *row_all_ha)
    drop.pack()

    # Time Used UI part
    timeoptions = ['Minutes/Day(Moderately Used)', 'Hours/Day(Heavy Use)', 'Minutes/Week(Rarely Used)',
                   'Hours/Week(Not Used Much)']
    dropdown2 = OptionMenu(root_ha, clicked2, *timeoptions)
    clicked2.set(timeoptions[0])
    dropdown2.pack()
    savetimelabel = Label(root_ha,
                          text="How much time do you use this device for?(Click the dropdown to choose your preferred measurement of time)")
    savetimelabel.pack()
    savetime = Entry(root_ha, width=25, borderwidth=5, bg='white')
    savetime.insert(0, "Type your consumption time here: ")
    savetime.pack()

    # Save everything
    finishbtn = Button(root_ha, text="Save & Finish", command=saveall)
    finishbtn.pack()


def electronics():
    # Create the basic dataframe from the user copy dataset
    e_usercopy = '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/fileusercopye.xlsx'
    df_e = pd.read_excel(e_usercopy, sheet_name='Electronics')

    def e_process():
        for index, row in df_e.iterrows():
            if int(row['Minutes/Day(Moderately Used)']) > 0:
                df_e.iloc[index]['Daily kwh'] = int(row['Minutes/Day(Moderately Used)']) / 60000 * int(
                    row['Power Consumption(Watts)'])
                df_e.to_excel(e_usercopy, sheet_name="Electronics", index=False)
            elif int(row['Hours/Day(Heavy Use)']) > 0:
                df_e.iloc[index]['Daily kwh'] = int(row['Minutes/Day(Moderately Used)']) / 1000 * int(
                    row['Power Consumption(Watts)'])
                df_e.to_excel(e_usercopy, sheet_name="Electronics", index=False)
            elif int(row['Minutes/Week(Rarely Used)']) > 0:
                df_e.iloc[index]['Weekly kwh'] = int(row['Minutes/Week(Rarely Used)']) / 60000 * int(
                    row['Power Consumption(Watts)'])
                df_e.to_excel(e_usercopy, sheet_name="Electronics", index=False)
            elif int(row['Hours/Week(Not Used Much)']) > 0:
                df_e.iloc[index]['Weekly kwh'] = int(row['Minutes/Week(Rarely Used)']) / 1000 * int(
                    row['Power Consumption(Watts)'])
                df_e.to_excel(e_usercopy, sheet_name="Electronics", index=False)

    # Show Item saved in UI
    def item_show():
        global text_e
        text_e = clicked.get()
        item_label = Label(root_e, text="")
        item_label.config(text="You chose: " + text_e)
        item_label.pack()

    # Show date saved in UI
    def date_show():
        date_label = Label(root_e, text="")
        date_label.config(text="Selected Date is: " + cal.get_date())
        date_label.pack()

    # Save the time the device is used
    def savetimexlsx():
        time_e = savetime.get()
        global text_he
        text_e = clicked.get()
        row = df_e["Electronics Name"] == text_e
        row1 = df_e.index[row][0]
        df_e.at[row1, clicked2.get()] = time_e
        df_e.to_excel(e_usercopy, sheet_name="Electronics", index=False)

    # Save the Date an appliance is added
    def savedatexlsx():
        global text_e
        print(text_e)
        date_e = cal.get_date()
        row = df_e["Electronics Name"] == text_e
        row1 = df_e.index[row][0]
        df_e.at[row1, "Date Added"] = date_e
        df_e.to_excel(e_usercopy, sheet_name="Electronics", index=False)

    def savetolist():
        global timeunit
        date_e = cal.get_date()
        text_e = clicked.get()
        time_e = int(savetime.get())
        row2 = df_e["Electronics Name"] == text_e
        row3 = df_e.index[row2][0]
        power_e = int(df_e.at[row3, "Power Consumption(Watts)"])
        if clicked2.get() == "Minutes/Day(Moderately Used)":
            powerconsumption.append((((time_e / 60) * power_e) / 60000) * 7)
            timeunit = " minutes per week"
        elif clicked2.get() == "Hours/Day(Heavy Use)":
            powerconsumption.append(((time_e * power_e) / 60000) * 7)
            timeunit = " hours per day"
        elif clicked2.get() == "Minutes/Week(Rarely Used)":
            powerconsumption.append(((time_e / 60) * power_e) / 60000)
            timeunit = " minutes per week"
        elif clicked2.get() == "Hours/Week(Not Used Much)":
            powerconsumption.append((time_e * power_e) / 60000)
            timeunit = " hours per week"
        else:
            print("error occureed in this part.")
        dateadded.append(date_e)
        timeused.append(time_e)
        appliancename.append(text_e)
        # addeditems.append([text_he, power_ha, date_ha, time_ha])

        #addeditems.append([text_he, power_ha, date_ha, time_ha])
    # Save everything
    def saveall():
        savetolist()
        item_show()
        date_show()
        savetimexlsx()
        savedatexlsx()
        e_process()
        root_e.withdraw()

    row_all_e = []

    # Append Home appliances to dropdown
    appliance_data = pd.read_excel(energydatabase, sheet_name='Electronics', skiprows=1)
    for index, row in appliance_data.iterrows():
        row_ha = row['Electronics Name']
        row_all_e.append(row_ha)

    # Creating UI
    root_e = Toplevel()
    root_e.geometry("1280x720")
    root_e.wm_attributes("-transparent", True)
    today = str(datetime.date.today())
    curr_year = int(today[:4])
    curr_month = int(today[5:7])
    curr_day = int(today[8:10])
    cal = Calendar(root_e, selectmode='day',
                   year=curr_year, month=curr_month,
                   day=curr_day)
    cal.pack(pady=20)
    clicked = StringVar()
    clicked.set(row_all_e[0])
    clicked2 = StringVar()
    drop = OptionMenu(root_e, clicked, *row_all_e)
    drop.pack()

    # Time Used UI part
    timeoptions = ['Minutes/Day(Moderately Used)', 'Hours/Day(Heavy Use)', 'Minutes/Week(Rarely Used)',
                   'Hours/Week(Not Used Much)']
    dropdown2 = OptionMenu(root_e, clicked2, *timeoptions)
    clicked2.set(timeoptions[0])
    dropdown2.pack()
    savetimelabel = Label(root_e,
                          text="How much time do you use this device for?(Click the dropdown to choose your preferred measurement of time)")
    savetimelabel.pack()
    savetime = Entry(root_e, width=25, borderwidth=5, bg='white')
    savetime.insert(0, "Type your consumption time here: ")
    savetime.pack()

    # Save everything
    finishbtn = Button(root_e, text="Save & Finish", command=saveall)
    finishbtn.pack()


def home_energy():
    # Create the basic dataframe from the user copy dataset
    he_usercopy = '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/fileusercopyhe.xlsx'
    df_he = pd.read_excel(he_usercopy)

    def he_process():
        for index, row in df_he.iterrows():
            if int(row['Minutes/Day(Moderately Used)']) > 0:
                df_he.iloc[index]['Daily kwh'] = int(row['Minutes/Day(Moderately Used)']) / 60000 * int(
                    row['Power Consumption(Watts)'])
                df_he.to_excel(he_usercopy, sheet_name="Home Energy", index=False)
            elif int(row['Hours/Day(Heavy Use)']) > 0:
                df_he.iloc[index]['Daily kwh'] = int(row['Minutes/Day(Moderately Used)']) / 1000 * int(
                    row['Power Consumption(Watts)'])
                df_he.to_excel(he_usercopy, sheet_name="Home Energy", index=False)
            elif int(row['Minutes/Week(Rarely Used)']) > 0:
                df_he.iloc[index]['Weekly kwh'] = int(row['Minutes/Week(Rarely Used)']) / 60000 * int(
                    row['Power Consumption(Watts)'])
                df_he.to_excel(he_usercopy, sheet_name="Home Energy", index=False)
            elif int(row['Hours/Week(Not Used Much)']) > 0:
                df_he.iloc[index]['Weekly kwh'] = int(row['Minutes/Week(Rarely Used)']) / 1000 * int(
                    row['Power Consumption(Watts)'])
                df_he.to_excel(he_usercopy, sheet_name="Home Energy", index=False)

    # Show Item saved in UI
    def item_show():
        global text_he
        text_he = clicked.get()
        item_label = Label(root_he, text="")
        item_label.config(text="You chose: " + text_he)
        item_label.pack()

    # Show date saved in UI
    def date_show():
        date_label = Label(root_he, text="")
        date_label.config(text="Selected Date is: " + cal.get_date())
        date_label.pack()

    # Save the time the device is used
    def savetimexlsx():
        time_he = savetime.get()
        global text_he
        text_he = clicked.get()
        row = df_he["Home Energy Name"] == text_he
        row1 = df_he.index[row][0]
        df_he.at[row1, clicked2.get()] = time_he
        df_he.to_excel(he_usercopy, sheet_name="Home Energy", index=False)

    # Save the Date an appliance is added
    def savedatexlsx():
        global text_he
        print(text_he)
        date_ha = cal.get_date()
        row = df_he["Home Energy Name"] == text_he
        row1 = df_he.index[row][0]
        df_he.at[row1, "Date Added"] = date_ha
        df_he.to_excel(he_usercopy, sheet_name="Home Energy", index=False)

    def savetolist():
        global timeunit
        date_he = cal.get_date()
        text_he = clicked.get()
        time_he = int(savetime.get())
        row2 = df_he["Home Energy Name"] == text_he
        row3 = df_he.index[row2][0]
        power_he = int(df_he.at[row3, "Power Consumption(Watts)"])
        if clicked2.get() == "Minutes/Day(Moderately Used)":
            powerconsumption.append((((time_he / 60) * power_he) / 60000) * 7)
            timeunit = " minutes per day"
        elif clicked2.get() == "Hours/Day(Heavy Use)":
            powerconsumption.append(((time_he * power_he) / 60000) * 7)
            timeunit = " hours per day"
        elif clicked2.get() == "Minutes/Week(Rarely Used)":
            powerconsumption.append(((time_he / 60) * power_he) / 60000)
            timeunit = " minutes per week"
        elif clicked2.get() == "Hours/Week(Not Used Much)":
            powerconsumption.append((time_he * power_he) / 60000)
            timeunit = " hours per week"
        else:
            print("error occureed in this part.")
        dateadded.append(date_he)
        timeused.append(time_he)
        appliancename.append(text_he)
        # addeditems.append([text_he, power_ha, date_ha, time_ha])
    # Save everything
    def saveall():
        savetolist()
        item_show()
        date_show()
        savetimexlsx()
        savedatexlsx()
        he_process()

        root_he.withdraw()

    row_all_he = []

    # Append Home appliances to dropdown
    appliance_data = pd.read_excel(energydatabase, sheet_name='Home Energy', skiprows=1)
    for index, row in appliance_data.iterrows():
        row_he = row['Home Energy Name']
        row_all_he.append(row_he)

    # Creating UI
    today = str(datetime.date.today())
    curr_year = int(today[:4])
    curr_month = int(today[5:7])
    curr_day = int(today[8:10])
    root_he = Toplevel()
    root_he.geometry("1280x720")
    root_he.wm_attributes("-transparent", True)
    cal = Calendar(root_he, selectmode='day',
                   year=curr_year, month=curr_month,
                   day=curr_day)
    cal.pack(pady=20)
    clicked = StringVar()
    clicked.set(row_all_he[0])
    clicked2 = StringVar()
    drop = OptionMenu(root_he, clicked, *row_all_he)
    drop.pack()

    # Time Used UI part
    timeoptions = ['Minutes/Day(Moderately Used)', 'Hours/Day(Heavy Use)', 'Minutes/Week(Rarely Used)',
                   'Hours/Week(Not Used Much)']
    dropdown2 = OptionMenu(root_he, clicked2, *timeoptions)
    clicked2.set(timeoptions[0])
    dropdown2.pack()
    savetimelabel = Label(root_he,
                          text="How much time do you use this device for?(Click the dropdown to choose your preferred measurement of time)")
    savetimelabel.pack()
    savetime = Entry(root_he, width=25, borderwidth=5, bg='white')
    savetime.insert(0, "Type your consumption time here: ")
    savetime.pack()

    # Save everything
    finishbtn = Button(root_he, text="Save & Finish", command=saveall)
    finishbtn.pack()


def window5():
    global root5
    root4.withdraw()
    root5 = Toplevel()
    root5.geometry("1280x720")
    root5.wm_attributes("-transparent", True)
    Grid.rowconfigure(root5, 0, weight=0)
    Grid.columnconfigure(root5, 0, weight=1)
    root5['bg'] = '#e5f5f9'
    global datetimeformat
    csv_data = pd.read_csv(filename, skiprows=5)
    print("Data Recieved:\n")
    csv_data['COST'] = csv_data['COST'].str[1:]
    csv_data['COST'] = csv_data['COST'].astype(float)
    csv_data['END DATE'] = pd.to_datetime(csv_data['END DATE'], infer_datetime_format=True)
    fig = px.scatter(csv_data, x='END DATE', y='USAGE', title="Energy Usage Trend", trendline="lowess")
    fig.show()
    titletext = Label(root5, text="Add your Home Devices", font=('DIN Alternate', 40), compound=CENTER)
    titletext.grid(row=0, column=0, sticky="NSEW")
    addhomebtn = Button(root5, text="Add Home Appliance", font=('Segoe UI Semibold', 13), fg='black', width=17,
                        height=2, cursor="openhand", command=home_appliances)
    addhomebtn.grid(row=1, column=0, sticky="NSEW")
    addhomeenergybtn = Button(root5, text="Add Home Energy Item", font=('Segoe UI Semibold', 13), fg='black', width=17,
                              height=2, cursor="openhand", command=home_energy)
    addhomeenergybtn.grid(row=2, column=0, sticky="NSEW")
    addelectronicsbtn = Button(root5, text="Add Electronics Appliance", font=('Segoe UI Semibold', 13), fg='black',
                               width=17,
                               height=2, cursor="openhand", command=electronics)
    addelectronicsbtn.grid(row=3, column=0, sticky="NSEW")
    finishbtn = Button(root5, text="Finish and Continue", font=('Franklin Gothic Medium', 16), fg='black',
                       command=window6)
    finishbtn.grid()


# processingbgimg = PhotoImage(file='/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/bgimg3.png')
# bglabel = Label(root6, image=processingbgimg)
# bglabel.place(x=0, y=0)
def percent_change(num_a, num_b):
    global answer
    global phrase
    answer = (num_a / num_b) * 100
    if num_a > num_b:
        phrase = "decreased"
    elif num_b > num_a:
        phrase = "increased"
    elif num_a == num_b:
        phrase = "didn't change"
    else:
        print("Internal Error in code. Please restart program")
def processing():
    global root6
    global percent0
    global percent1
    global lbl1
    global csv_data
    global processbtn
    percent0 = 100
    percent1 = 0
    for x in range(23):
        prgrs['value'] += 1
        root5.update_idletasks()
        time.sleep(0.01)
    for x in range(2):
        time.sleep(1)
        prgrs['value'] += 8.5
        root5.update_idletasks()
        time.sleep(0.5)
    for x in range(120):
        prgrs['value'] += 0.5
        root5.update_idletasks()
        time.sleep(0.00125)
    prgrs.pack_forget()

    lbl1 = Label(root6, text="Finished Processing...Displaying Summary", font=('SF Pro Semibold', 14))
    print("Processing Completed. Displaying Graph.")
    print("Thank you for using Py Eco Home Energy Tracker")
    time.sleep(1)
    lbl1.pack(pady=20)
    processbtn.pack_forget()
    csv_data = pd.read_csv(filename, skiprows=4)
    global totalenergyinfo
    totalenergyinfo = {}
    first_last = {}
    for index, row in csv_data.iterrows():
        row_startdate = str(row['START DATE'])
        cost = str(row['COST'])
        cost = int(round(float(cost[1:])))
        usage = int(round(float(row['USAGE'])))
        year = int(row_startdate[:-6])
        month_day = row_startdate[-5:]
        month = int(row_startdate[-5:-3])
        day = row_startdate[8:]
        if year in first_last:
            if month < first_last[year][0]:
                first_last[year][0] = month
            if month > first_last[year][1]:
                first_last[year][1] = month
        else:
            first_last[year] = [month, month]
    global years
    global kwhyear
    global costyear
    global ecoyear
    awesomevar = 0
    month2 = 0
    for index, row in csv_data.iterrows():
        row_startdate = str(row['START DATE'])
        cost = str(row['COST'])
        cost = int(round(float(cost[1:])))
        usage = int(round(float(row['USAGE'])))
        year = int(row_startdate[:-6])
        month_day = row_startdate[-5:]
        month = int(row_startdate[-5:-3])
        day = row_startdate[8:]

        if year in totalenergyinfo:
            #     if int(day) >= 15:
            #         print("old monthday: " + month_day)
            #         oldmonth = month
            #         if month == "12":
            #             month = 0  # subtracting -1 at the end so this answer must be -1 of the value. the actual wanted value is 1
            #         elif str.startswith(month, "0"):
            #             month = int(month[1:])
            #         elif month == "10" or month == "11":
            #             print("monthcheck: " + month)
            #         else:
            #             showinfo(title="File Error",
            #                      message="Sorry, it seems like your uploaded file was not formatted correctly. The program will now auto-restart to solve this problem. Just click OK to continue.")
            #             quit()
            #         month = int(month)
            #         month += 1
            #     elif int(day) < 15:
            #         print("old monthday: " + month_day)
            #         oldmonth = month
            #         if month == "01":
            #             month = 13  # adding +1 at the end so this answer must be +1 of the value. the actual wanted value is 11
            #         elif str.startswith(month, "0"):
            #             month = int(month[1:])
            #         elif month == "10" or month == "11" or month == "12":
            #             print("monthcheck: " + month)
            #         else:
            #             showinfo(title="File Error",
            #                      message="Sorry, it seems like your uploaded file was not formatted correctly. The program will now auto-restart to solve this problem. Just click OK to continue.")
            #             quit()
            #
            #         month = int(month)
            #         month -= 1
            #
            #     month2 = 0
            #     print(month)

            # print(first_last)
            # if month == first_last[year][0]:
            #     print(month)
            #     month2 = month
            #     usage2 = usage
            #     cost2 = cost
            #
            #     month2 += 1
            #
            #
            # elif month2 < first_last[year][0] and month2 > first_last[year][0]:
            #     print(month)
            #     usage2 = usage
            #     cost2 = cost
            #
            #     month2 += 1
            #
            # elif month2 == first_last[year][1]:
            #     month2 = month
            #     usage2 = usage
            #     cost2 = cost
            #
            #
            # elif month2 < first_last[year][0] or month2 > first_last[year][1]:
            #     print(month)
            #     usage = 0
            #     cost = 0
            #     month2 += 1
            #     print("monthy: " + str(month2))

            # else:
            #     print(
            #         "Sorry there's an internal problem and we need to restart our program. Please excuse the inconvenience.")
            #     showinfo(title="INTERNAL PROBLEM",
            #              message="Sorry there's an internal problem and we need to restart our program. Please excuse the inconvenience.")
            #     quit()
            # print(first_last)
            # if month in totalenergyinfo:
            #     print("exception made...")
            #     month = oldmonth
            #     print("ok..." + month)
            print("the month: " + str(month))

            print(month2)

            if month == first_last[year][1]:
                usage2 = usage
                cost2 = cost
                eco2 = round(usage2 * 0.818, 2)
                totalenergyinfo[year][month2] = [usage2, cost2, eco2]
            elif first_last[year][0] < month2 < first_last[year][1]:
                usage2 = usage
                cost2 = cost
                eco2 = round(usage2 * 0.818, 2)
                totalenergyinfo[year][month2] = [usage2, cost2, eco2]
                month2 += 1
                print("after: " + str(month2))
            else:
                month2 += 1
                print("deex")

            print("firstlast:" + str(first_last))
            print(totalenergyinfo)

        else:
            totalenergyinfo[year] = {}
            month2 = 0
            for i in range(1, 13):
                month2 += 1
                usage2 = 0
                cost2 = 0
                eco2 = 0
                totalenergyinfo[year][month2] = [usage2, cost2, eco2]
            awesomevar = 0

            if month == first_last[year][0]:
                month2 = month
                usage2 = usage
                cost2 = cost
                eco2 = round(usage2 * 0.818,2)
                totalenergyinfo[year][month2] = [usage2, cost2, eco2]
                month2 += 1
                print("after: " + str(month2))

    # Get the years
    years = []
    ecoyear = []
    for year in totalenergyinfo:
        years.append(year)
    kwhyear = []
    costyear = []
    # Getting Usage and Cost iterating
    for yearcounter in range(len(years)):
        # Get all the months in the year
        months = []

        for month in totalenergyinfo[int(years[yearcounter])]:
            months.append(month)

        # Use the months to iterate and find the usages/costs
        usages = []
        costs = []
        for monthcounter in range(len(months)):
            for cost_usage in totalenergyinfo[int(years[yearcounter])][int(months[monthcounter])]:
                usages.append(cost_usage)
                costs.append(cost_usage)

        # Format the iterated results and produce a final result
        del usages[1::2]
        del costs[::2]
        year_kwh_sum = sum([usage for usage in usages])
        year_cost_sum = sum([cost for cost in costs])
        kwhyear.append(year_kwh_sum)
        costyear.append(year_cost_sum)
        ecoyear.append(round(year_kwh_sum * 0.818, 2))
        snstotalenergy = totalenergyinfo
        #csv_data['COST'] = csv_data['COST'].str[1:]
        #csv_data['COST'] = csv_data['COST'].astype(float)
        #csv_data['END DATE'] = pd.to_datetime(csv_data['END DATE'], infer_datetime_format=True)


    # Final Result
    global kwh_all
    global cost_all
    global co2_all

    print("Kwh/Year: " + str(kwhyear))
    print("Cost/Year: " + str(costyear))
    print(totalenergyinfo)
    kwh_all = sum([kwh for kwh in kwhyear])
    cost_all = sum([cost for cost in costyear])
    co2_all = sum([co2 for co2 in ecoyear])
    print("Total Kwh all in all: " + str(kwh_all))
    print("Total Cost all in all: " + str(cost_all))



    print(totalenergyinfo)
    try1 = totalenergyinfo[2018][6]
    print("hmm.. " + str(try1))
    print("2018: " + str(try1[0]))
    try2 = totalenergyinfo[2019][6]
    print(try2)
    print("2019: " + str(try2[0]))
    num_a1 = try1[0]
    num_b2 = try2[0]
    percent_change(num_a1, num_b2)

    comparisons = 0
    global percentkwh
    global percentcost
    global percentcarbon
    global summary
    percentkwh = []
    percentcost = []
    percentcarbon = []
    summary = []
    for k in range(len(years)):
        try:
            if comparisons == 0:
                kwhphrase = ". Your total energy consumption in " + str(years[k]) + " was " + str(kwhyear[k]) + "kWh."
                ecophrase = "."

            elif comparisons > 0:
                percent_change(ecoyear[k], ecoyear[k - 1])
                kwhphrase = " compared to " + str(years[k - 1]) + ". Your total energy consumption in " + str(
                    years[k]) + " was " + str(kwhyear[k]) + "kWh."
                ecophrase = " which is " + str(round(answer, 2)) + "% higher than " + str(years[k - 1]) + "."
            percent_change(kwhyear[k], kwhyear[k - 1])
            text_summarykwh = "In " + str(years[k]) + " your energy consumption " + phrase + " by " + str(
                round(answer)) + "%" + kwhphrase
            summary.append(text_summarykwh)
            percentkwh.append(round(answer))
            text_summaryco2 = "Your total Carbon Footprint in " + str(years[k]) + " was " + str(ecoyear[k]) + " pounds of CO2" + ecophrase
            summary.append(text_summaryco2)
            print(text_summaryco2)
            percentcarbon.append(round(answer, 2))
            percent_change(costyear[k], costyear[k - 1])
            text_summarycost = "In " + str(years[k]) + " your total energy cost was $" + str(round(costyear[k],2)) + " which is " + str(round(answer))+ "% higher than " +  str(years[k-1]) + "."
            summary.append(text_summarycost)
            print(text_summarycost)
            percentcost.append(round(answer, 2))
            comparisons += 1
        except IndexError:
            if comparisons > 0:
                text_summarykwh = "In " + str(years[k]) + " your energy consumption was " + str(kwhyear[k]) + "kWh."
                summary.append(text_summarykwh)
                text_summaryco2 = "Your total Carbon Footprint in " + str(years[k]) + " was " + str(
                    ecoyear[k]) + " pounds of CO2."
                summary.append(text_summaryco2)
                print(text_summaryco2)
                text_summarycost = "In " + str(years[k]) + ", your total energy cost was $" + str(format(costyear[k])) + "."
                summary.append(text_summarycost)
                print(text_summaryco2)
            else:
                print("An internal error has occurred please try again later.")
            break

    # Suggestions

    # Total

    # Ending


    window7()


bgimagesdata = ['/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/finalscreenbg1.png',
                '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/finalscreenbg2.png',
                '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/finalscreenbg3.png',
                '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/finalscreenbg4.png']
bgimages1 = str(random.sample(bgimagesdata, 1))
bgimages = PhotoImage(file=bgimages1[2:-2])


def window7():
    global totalenergyinfo
    root7 = Toplevel()
    root7.geometry("1280x720")
    root7.wm_attributes("-transparent", True)
    bglabel3 = Label(root7, image=bgimages)
    bglabel3.place(x=0, y=0)
    print("FINAL Window!! Initializing 7...")
    biglabel = Label(root7, text="Your Home Energy Report Summary", font=('SF Pro Semibold', 40), compound=CENTER)
    biglabel.pack()
    ecolabel = Label(root7, text="From the data you gave us, here's what we analyzed", font=('SF Pro Text', 13))
    ecolabel.pack()
    # Eco Emissions Finder
    print("the summary: " + str(summary))
    fig = Figure(figsize=(6, 4.74), dpi=95)
    sns.color_palette("bright")
    sns.set_style("darkgrid")
    graph = fig.add_subplot(111)
    fig.subplots_adjust(left=0.12, bottom=0.112, right=0.971, top=0.907, wspace=0.2, hspace=0.2)
    graph.plot(years, kwhyear, label="kWh")
    graph.plot(years, costyear, label="Cost")
    graph.plot(years, ecoyear, label="Carbon Footprint")
    graph.set_xlabel("Years", fontdict={'fontsize': 14, 'fontname': 'DIN Alternate'})
    graph.set_ylabel("Units", fontdict={'fontsize': 14, 'fontname': 'DIN Alternate'})
    graph.set_title("Home Energy Comparison from " + str(years[0]) + " - " + str(years[len(years) - 1]), fontdict={'fontsize': 16, 'fontname': 'DIN Alternate'})
    graph.legend(loc="upper left")
    frame1 = Frame(root7, highlightbackground="#1aa7ec", highlightthickness=4)
    frame1.pack(side=LEFT, anchor = NW, padx=15, pady=20)
    canvas = FigureCanvasTkAgg(fig, master=frame1)
    canvas.draw()
    canvas.get_tk_widget().pack()
    toolbar = NavigationToolbar2Tk(canvas, frame1)
    toolbar.update()
    canvas.get_tk_widget().pack()
    percentkwh_1 = round(sum(percentkwh) / len(percentkwh), 2)
    percentcost_1 = round(sum(percentcost) / len(percentcost), 2)
    percentcarbon_1 = round(sum(percentcarbon)/ len(percentcarbon), 2)
    left_frame = Frame(root7)
    left_frame.pack(side=LEFT, pady = 40, ipady=10, anchor =N)

    folder2 = '/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/energyreports/'
    today = date.today()
    format_today = today.strftime('%m-%d-%Y')
    figurepath = folder2 + 'Energy Report Graph-' + format_today + '.png'
    textpath = folder2 + 'Energy Report Text-' + format_today + '.txt'
    filecheck = exists(figurepath)
    filecheck2 = exists(textpath)
    print(powerconsumption)
    suggestpower = max(powerconsumption)
    suggestpower_index = powerconsumption.index(suggestpower)
    suggestdevice = appliancename[suggestpower_index]
    suggesttime = timeused[suggestpower_index]
    suggestdate = dateadded[suggestpower_index]
    reclabel = Label(left_frame, text = "Recommendations:",font=('SF Pro Semibold', 28), fg='green')
    suggestlabel = Label(left_frame, font = ('SF Pro Semibold', 20), text="⓵ Your highest consumption device is " + suggestdevice + " \nwhich has a power consumption of " + str(round(suggestpower, 2)*52) +"kWH per year.", anchor = W)
    suggestlabel2 = Label(left_frame, font = ('SF Pro Semibold', 20),text = "⓶ This device was added on " + str(suggestdate) + "\nand is currently used " + str(suggesttime) + timeunit + ".\n", anchor=W)
    suggestlabels = Label(left_frame, font = ('SF Pro Semibold', 22), text= "⓷ Suggestion: Try reducing the useage of this device\n to lower your energy.", fg='#2AAA8A', anchor=W)
    averagekwh = Label(left_frame, text="\n Overall, every year your energy consumption " + phrase + " by " + str(percentkwh_1) + "%.",anchor=W,
                       font=('SF Pro Semibold', 20))
# averagecost = Label(left_frame, text="Average year over year cost " + phrase + " " + str(percentcost_1) + "%.",
#                     font=('SF Pro Semibold', 20))
# averagearbon = Label(left_frame,
#                      text="Average year over year carbon footprint " + phrase + " " + str(percentcarbon_1) + "%.",
#                      font=('Segoe UI Variable', 20))

    suggestlabel3 = Label(root7, font = ('SF Pro Semibold', 23), text = "Total Home Energy Stats from " + str(years[0]) + " - " +  str(years[len(years)-1]) + ":")
    suggestlabel4 = Label(root7, font = ('SF Pro Semibold', 26), text = "Energy Consumption(kWh): " + str(format(int(round(kwh_all)), ",d")) + "kWh", fg='#2A78B1')
    suggestlabel5 = Label(root7, font = ('SF Pro Semibold', 26), text = "Energy Cost: $" + str(format(int(round(cost_all, 2)),",d")), fg='#F4812E')
    suggestlabel6 = Label(root7, font = ('SF Pro Semibold', 26), text = "Carbon Footprint: " + str(format(int(round(co2_all, 2)), ",d")) + " pounds of CO2", fg='#39A039')
    reclabel.pack()
    suggestlabel.pack()
    suggestlabel2.pack()
    suggestlabels.pack()
    averagekwh.pack()
    # averagecost.pack()
    # averagearbon.pack()
    suggestlabel3.place(x=460, y=600)
    suggestlabel4.place(x=10, y=670)
    suggestlabel5.place(x=505, y=670)
    suggestlabel6.place(x=790, y=670)


    #reclabel.place(x=20, y=550)
    #suggestlabel.place(x=20, y=600)
    #suggestlabel2.place(x=20, y=625)
    #finallabel = Label(root7, font=('Segoe UI Variable', 17), text = "Total Home Energy over " + str(years[len(years)-1] - years[0]) + " years -> Energy Consumption(kWh): " + str(round(kwh_all))+  " -> Energy Cost: " + str(cost_all) + "$ -> Carbon Footprint: " + str(co2_all) + " pounds of CO2")
    #finallabel.place(x=20, y=650)
    if filecheck == True:
        format_today = today.strftime("%m-%d-%Y %H:%M")
        figurepath = folder2 + 'Energy Graph Report- ' + format_today + '.png'
        graph.figure.savefig(figurepath)
    elif filecheck == False:
        graph.figure.savefig(figurepath)
    else:
        print("There was an error uploading your graph")

    if filecheck2 == True:
        format_today = today.strftime("%m-%d-%Y %H:%M")
        textpath = folder2 + 'Energy Text Report- ' + format_today + '.txt'
        with open(textpath, 'x') as f:
            f.write("Hey there! These are all of the energy consumption, carbon footprint, and cost analysis we got from the data you uploaded, check it out! ↓↓\n")
            f.write("\n")
            for i in range(len(years)):
                f.write('Summary for ' + str(years[i]) + ': \n')
                f.write(summary[i])
                f.write('\n')
                f.write(summary[i+1])
                f.write('\n')
                f.write(summary[i+2])
                f.write('\n')
            f.close()
    elif filecheck2 == False:
        with open(textpath, 'x') as f:
            f.write(
                "Hey there! These are all of the energy consumption, carbon footprint, and cost analysis we got from the data you uploaded, check it out! ↓↓ \n")
            f.write("\n")
            for i in range(len(years)):
                f.write('Summary for ' + str(years[i]) + ':\n')
                f.write(summary[i])
                f.write('\n')
                f.write(summary[i])
                f.write('\n')
                f.write(summary[i])
                f.write('\n')
            f.close()
    else:
        print("There was an error uploading your textfile")


def window6():
    global root6
    global root5
    root6 = Toplevel()
    root5.withdraw()
    root6.geometry("1366x768")
    root6.wm_attributes("-transparent", True)
    print("Window 4 Closed. UI5 Built. Developer Signal = [root5]")
    global cpu
    global prgrs
    global processbtn
    global cpulbl
    root6.geometry("700x500")
    root6.title("Py Eco Home Energy Tracker - [Processing Page]")
    #root6.iconbitmap('/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/energyicon.icns')
    cpu = cpuinfo.get_cpu_info()['brand_raw']
    prgrs = ttk.Progressbar(root6, orient=HORIZONTAL, length=300, mode='determinate')
    prgrs.pack(pady=20)
    processbtn = Button(root6, text="Start Processing", command=processing, cursor="openhand")
    processbtn.pack(pady=20)
    cpulbl = Label(root6, text="Your Processor: " + cpu, font=('SF Pro Semibold', 16), width = 22, height = 2)
    cpulbl.pack(pady=40)
    cpulbl.config(background='#2D46B9', foreground='#F5F5F5')


# Windows 1 UI
bgimg1 = PhotoImage(file="/Users/riddhiman.rana/Documents/PyEcoHome Energy Tracker/images/bgimg1.png")
bglabel1 = Label(root1, image=bgimg1)
bglabel1.place(x=0, y=0)
introlabel = Label(root1, text="Welcome to the PyEco Home Energy Tracker. Press Start to Continue.",
                   font=('SF Compact Semibold', 20), compound=RIGHT)
introlabel.pack(side=TOP, pady=50)
contbtn = Button(root1, text="Start", image=photoimage1, compound=LEFT, command=window2, cursor='openhand')
contbtn.config(background='#C8EE90', foreground='black', width=175, height=40)
contbtn.pack(side=TOP, padx=10, pady=30)
print("Windows 1 has opened. UI1 built. Developer Signal = [root1]")

root1.mainloop()
