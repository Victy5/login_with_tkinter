from tkinter import *
import os
from tkinter import messagebox
import re

from future.backports import email

entbd = 4
entbg = "black"
but1height = 2
butt1width = 30
btnWidth = 12
btnHeight = 2
bg1 = "#8c0c08"
fg1 = "white"
font1 = ("castellar", 15, "bold")
enterfont = ("calibre", 13, "bold")
smallfont = ("Times new roman", 13, "bold")

#funtion
def register():
    global register_screen
    register_screen = Toplevel(login_screen)
    register_screen.title("register")
    register_screen.configure(bg=bg1)

    global username
    global password
    global Email
    global phonenumber
    global user_enter
    global user_enter2

    Email = StringVar()
    var = StringVar(register_screen, "1")
    phonenumber = StringVar()
    # conv = str(phonenumber)
    username = StringVar()
    password = StringVar()
    confirm_password = StringVar()

    register_top1 = Label(register_screen, text="Register", font=font1, bg=bg1, fg=fg1, justify=LEFT)
    register_top1.grid(row=0, column=0, columnspan=31)

    user_label = Label(register_screen, text="Username", bg=bg1, fg=fg1, font=smallfont)
    user_label.grid(row=1, column=0)
    user_enter = Entry(register_screen, width=butt1width, font=enterfont, textvariable=username, bd=entbd)
    user_enter.grid(row=1, column=1, columnspan=2)
    space_user = Label(register_screen, text="", bg=bg1, fg=fg1, font=smallfont).grid(row=2, column=0)


    user_label2 = Label(register_screen, text="Email", bg=bg1, fg=fg1, font=smallfont)
    user_label2.grid(row=3, column=0)
    user_enter2 = Entry(register_screen, width=butt1width, font=enterfont,textvariable=Email, bd=entbd)
    user_enter2.grid(row=3, column=1, columnspan=2)
    space_password = Label(register_screen, text="", bg=bg1, fg=fg1, font=smallfont).grid(row=4, column=0)

    user_label3 = Label(register_screen, text="Phone number", bg=bg1, fg=fg1, font=smallfont)
    user_label3.grid(row=5, column=0)
    user_enter3 = Entry(register_screen, width=butt1width, font=enterfont, textvariable=phonenumber, bd=entbd)
    user_enter3.grid(row=5, column=1, columnspan=2)
    space_password = Label(register_screen, text="", bg=bg1, fg=fg1, font=smallfont).grid(row=6, column=0)

    user_label4 = Label(register_screen, text="Select Gender", bg=bg1, fg=fg1, font=smallfont )
    user_label4.grid(row=7, column=0)
    def sel():
        selection = "You selected "+ var.get()
        print(selection)
    bt1 = Radiobutton(register_screen, text="Male",variable=var, value="Male", command=sel, font=smallfont, bd=entbd).grid(row=7, column=1)
    bt2 = Radiobutton(register_screen, text="Female",variable=var, value="Female", command=sel, font=smallfont, bd=entbd).grid(row=7, column=2)
    space_password = Label(register_screen, text="", bg=bg1, fg=fg1, font=smallfont).grid(row=8, column=0)

    user_label5 = Label(register_screen, text="Password", bg=bg1, fg=fg1, font=smallfont )
    user_label5.grid(row=9, column=0)
    user_enter5 = Entry(register_screen, width=butt1width, font=enterfont, textvariable=password, bd=entbd)
    user_enter5.grid(row=9, column=1, columnspan=2)
    space_password = Label(register_screen, text="", bg=bg1, fg=fg1, font=smallfont).grid(row=10, column=0)

    def show1():
        user_enter5.configure(show="*")
        check1.configure(command=hide1)

    def hide1():
        user_enter5.configure(show="")
        check1.configure(command=show1)

    check1 = Checkbutton(register_screen, text=' ', bg=bg1, command=show1, cursor="hand2")
    check1.grid(row=9, column=3)

    user_label6 = Label(register_screen, text="Confirm Password", bg=bg1, fg=fg1, font=smallfont)
    user_label6.grid(row=11, column=0)
    user_enter6 = Entry(register_screen, width=butt1width, font=enterfont, textvariable=confirm_password, bd=entbd)
    user_enter6.grid(row=11, column=1, columnspan=2)
    space_password = Label(register_screen, text="", bg=bg1, fg=fg1, font=smallfont).grid(row=12, column=0)

    def show2():
        user_enter6.configure(show="*")
        check2.configure(command=hide2)
    def hide2():
        user_enter6.configure(show="")
        check2.configure(command=show2)
    check2 = Checkbutton(register_screen, text=' ', bg=bg1, command=show2, cursor="hand2")
    check2.grid(row=11, column=3)

    def confirm_password():
        rule = r'\b[A-Za_z0-9._%]+@[A-Za-z0-9]+\.[A-Z|a-z]{2,}\b'
        email

        pwd = user_enter5.get()
        conpwd = user_enter6.get()
        if conpwd== pwd :
            register_user()
            # if (re.fullmatch(rule, Email)):
            #     print("valid email")
            #
            # else:
            #     messagebox.showerror("invalid", 'invalid email')
        else:
            messagebox.showerror('register', 'pls confirm your password')
    register_button = Button(register_screen, text="Register", borderwidth=5, command=confirm_password,  width=btnWidth, height=btnHeight, bg=bg1, fg=fg1, font=smallfont)
    register_button.grid(row=14, column=1)

    def reset_register():
        user_enter.delete(0, END)
        user_enter2.delete(0, END)
        user_enter3.delete(0, END)
        user_enter5.delete(0, END)
        var.set(0)
        user_enter.focus()
    register_reset = Button(register_screen, text="Reset", borderwidth=5, width=btnWidth, height=btnHeight, command=reset_register, bg=bg1, fg=fg1, font=smallfont)
    register_reset.grid(row=14, column=2, columnspan=2)

    def back():
        register_screen.withdraw()
        login()
    back = Button(register_screen, text="\u20ea", width=8, height=1, bg=bg1, fg=fg1, command=back, borderwidth=5)
    back.grid(row=14, column=0)

def register_user():
    username_info = username.get()
    password_info = password.get()
    email_info = Email.get()
    phone_info = phonenumber.get()

    file = open("myfile.txt", "w")
    file.write("username = "+username_info + "\n")
    file.write("password = "+password_info+ "\n")
    file.write("email = "+email_info+ "\n")
    file.write("phone Number = "+ str(phone_info))
    file.close()

    succed = Label(register_screen, text="Registration Success", fg="#fbb021", font=font1, bg=bg1)
    succed.grid(row=13, column=0, columnspan=8)
    register_screen.withdraw()
    login()

def login():
    global login_screen
    login_screen = Tk()
    login_screen.title("login")
    login_screen.configure(bg=bg1)

    global username_login_entry1
    global password_login_entry1
    global username_verify
    global password_verify

    username_verify = StringVar()
    password_verify = StringVar()

    top = Label(login_screen, text="Login form", font=font1, fg=fg1, bg=bg1)
    top.grid(row=0,column=0,columnspan=5)

    loglbl = Label(login_screen, text="Username", bg=bg1, fg=fg1, font=smallfont)
    loglbl.grid(row=1, column=0)
    username_login_entry1 = Entry(login_screen, textvariable=username_verify, font=enterfont, bd=entbd)
    username_login_entry1.grid(row=1, column=1, columnspan=2)
    space = Label(login_screen, text=" ", bg=bg1, fg=fg1, font=smallfont).grid(row=2,column=0)

    loglbl1 = Label(login_screen, text="Password", bg=bg1, fg=fg1, font=smallfont)
    loglbl1.grid(row=3, column=0)
    password_login_entry1 = Entry(login_screen, textvariable=password_verify, font=enterfont, show="*", bd=entbd)
    password_login_entry1.grid(row=3, column=1, columnspan=2)
    space = Label(login_screen, text="", bg=bg1, fg=fg1, font=smallfont)
    space.grid(row=4, column=0)

    def show1():
        password_login_entry1.configure(show="")
        check1.configure(command=hide1)

    def hide1():
        password_login_entry1.configure(show="*")
        check1.configure(command=show1)

    check1 = Checkbutton(login_screen, text=' ', bg=bg1, command=show1)
    check1.grid(row=3, column=3)
    tton = Button(login_screen, text="Login", width=btnWidth, height=btnHeight, command=login_verification, bg=bg1, fg=fg1, font=smallfont, borderwidth=5, bd=1).grid(row=6, column=1)

    fra = Frame(login_screen,width=80, height=10, bg=bg1)
    fra.grid(row=6, column=0)
    lbb = Label(fra, text="Don't have an account", height=1, fg=fg1, bg=bg1,)
    lbb.grid(row=0, column=0)
    but = Button(fra, text="Register", width=8, height=1, command=loggo, fg=fg1, bg=bg1, bd=1, justify=LEFT, borderwidth=5)
    but.grid(row=1, column=0)

    login_screen.mainloop()
def loggo():
    login_screen.withdraw()
    register()
def login_verification():
    login_verify()

def login_verify():
    global password1
    global username1
    username1 = username_verify.get()
    password1 = password_verify.get()

    username_login_entry1.delete(0, END)
    password_login_entry1.delete(0, END)
    print("working....")

    list_the_files = os.listdir()
    # if username1 in list_the_files:
    file1 = open("myfile.txt", "r")
    verify = file1.read()
    def check():
        if not username1 and not password1:
            messagebox.showwarning("clear", "input something")
            login_screen.withdraw()
            login()
        else:
            messagebox.showinfo("u are free")

    check()
    if username1 in verify and password1 in verify:
        print(username1 + "\n" + password1)
        login_sucess()
        # new()
    elif username1 not in verify and password1 not in verify:
        messagebox.showerror("validation", "please enter ur correct profile")
    elif password1 in verify:
        messagebox.showwarning("incorrect", "Username incorrect")
        print(username1)
    elif username1 in verify:
        messagebox.showwarning("incorrect", "password incorrect")
        print(password1)
    elif username1=="" and password1 == "":
        messagebox.showerror("invalid", "invalid")
    else:
        messagebox.showerror("not available", "user not found")

def login_sucess():
    global username1
    work = Label(login_screen, text="loading..", font=font1, fg="orange", bg=bg1)
    work.grid(row=5, column=1)
    name = username_verify.get()+ ","
    messagebox.showinfo("completed", f"{name} you have logged successfully")
    new()

def new():
    nw = Toplevel(login_screen)
    nw.title("Web page")
    scrwidth = nw.winfo_screenwidth()
    scrheight = nw.winfo_screenheight()
    nw.geometry(f"{scrwidth}x{scrheight}")

    tlbl = Label(nw, text=" welcome",).pack()



# lb1 = Label(a,text="Choose a process of entering this webpage",  font=font1, fg=fg1, bg=bg1)
# lb1.grid(row=0, column=0,)
#
# but1 = Button(a, text="Register", height=but1height, width=butt1width, command=register, bg=bg1, fg=fg1, font=smallfont)
# space1 = Label(a, text="", bg=bg1, fg=fg1, font=smallfont).grid(row=2, column=0)
# but1.grid(row=1,column=0)
#
# but1 = Button(a, text="Login", height=but1height, width=butt1width, command=login, bg=bg1, fg=fg1, font=smallfont)
# but1.grid(row=3,column=0)


login()
# a.mainloop()