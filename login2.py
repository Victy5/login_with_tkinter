
from tkinter import *
a = Tk()
a.configure(bg='black')
a.title(text='login interface')

fc = "aqua"
en = "black"
li = "white"

def login():
    from tkinter import messagebox
    global enter1
    global enter2
    global menu
    username = "vik3"
    password = "12345"

    if enter1.get() == username and enter2.get() == password:
        messagebox.showinfo("logged-in", username + ", you have successfully logged-in")
        open()
        a.withdraw()
    elif enter1.get() == username and enter2.get() != password:
        messagebox.showwarning("Error", "wrong password")
    elif enter1.get() != username and enter2.get() == password:
        messagebox.showwarning("Error", "wrong username")
    else:
        messagebox.showerror("no syntax", "invalid syntax")



def open():
    new = Toplevel(a)
    high = new.winfo_screenheight()
    wid = new.winfo_screenwidth()
    print(str(high) + "\n" + str(wid))
    new.geometry(f"{wid}x{high}")
    new.title("New Window")
    new.configure(bg="beige")
    new.iconphoto(False, photo)
    fr = Frame(new, width=10,  bg="blue")
    fr.grid(row=0, column=0, columnspan=5)
    txt = Label(fr, text="welcome to  Freelancer club", font=('Helvetica 17 bold'), justify="center", width=55)
    txt.grid(row=0, column=0,)
    Label(new, text="You have successfully logged in ", width=55, justify="center", font=("bold",10)).grid(row=1, column=0)


    from tkinter import Menu
    from tkinter import filedialog
    import turtle
    menu = Menu()
    new_item = Menu(menu, tearoff=0)
    new_item.add_command(label='New')
    new_item.add_separator()
    new_item.add_command(label='Edit', font=())

    def click():
        Menu()
        turtle.shape("turtle")
        turtle.color("yellow","red")
        turtle.begin_fill()
        for i in range(1, 60):
            turtle.forward(50)
            turtle.right(140)
        turtle.right(-60)
        turtle.forward(2)
        for i in range(0, 200):
            turtle.forward(1)
            turtle.right(1)
        turtle.forward(120)
        turtle.right(90)
        turtle.forward(120)
        for i in range(0, 100):
            turtle.forward(1)
            turtle.right(1)
        turtle.end_fill()
        turtle.exitonclick()
    new_item.add_command(label='show a design',command=click)
    menu.add_cascade(label='File', menu=new_item)
    insert = Menu()
    def wide():
        filedialog.askopenfilename(filetypes=(("Python file","*.py"),("all files", "*.*")))

    insert.add_command(label='object', command=wide)
    menu.add_cascade(label="insert", menu=insert)
    new.config(menu=menu)

def fmenu():
    head = Label(a, text="Login",font=("Calisto MT bold", 26), justify="center", fg=fc, width=30, bg=en)
    head.grid(row=0, column=0, columnspan=5)

    lbl1 = Label(a, text="Username", fg=fc, bg=en, font=("Calisto MT", 20), height=3)
    lbl1.grid(row=1, column=1)
    enter1 = Entry(a, width=30, font=("Areal capitalize", 20), bg=li, fg=en)
    enter1.grid(row=1,column=2, columnspan=2)
    enter1.focus()

    lbl2 = Label(a, text="Password", fg=fc, bg=en, font=("Calisto MT", 20), height=2)
    lbl2.grid(row=2, column=1)
    enter2 = Entry(a, width=30, font=("Areal bold", 20), bg=li, fg=en, show="*", validate="all")
    enter2.grid(row=2,column=2, columnspan=2)

    def clicked():
        enter1.delete(0, END)
        enter2.delete(0, END)
        enter1.focus()

    btn1 = Button(a, text="Login", width=20, bg=fc, font=("impact", 12), fg=en, command=login)
    btn1.grid(row=3, column=2)
    btn2 = Button(a, text="reset", width=20, bg=en, font=("impact", 12), fg=li, command=clicked)
    btn2.grid(row=3, column=3)



head = Label(a, text="Login",font=("Calisto MT bold", 26), justify="center", fg=fc, width=30, bg=en)
head.grid(row=0, column=0, columnspan=5)

lbl1 = Label(a, text="Username", fg=fc, bg=en, font=("Calisto MT", 20), height=3)
lbl1.grid(row=1, column=1)
enter1 = Entry(a, width=30, font=("Areal capitalize", 20), bg=li, fg=en)
enter1.grid(row=1,column=2, columnspan=2)
enter1.focus()

lbl2 = Label(a, text="Password", fg=fc, bg=en, font=("Calisto MT", 20), height=2)
lbl2.grid(row=2, column=1)
enter2 = Entry(a, width=30, font=("Areal bold", 20), bg=li, fg=en, show="*", validate="all")
enter2.grid(row=2,column=2, columnspan=2)

def clicked():
    enter1.delete(0, END)
    enter2.delete(0, END)
    enter1.focus()

btn1 = Button(a, text="Login", width=20, bg=fc, font=("impact", 12), fg=en, command=login)
btn1.grid(row=3, column=2)
btn2 = Button(a, text="reset", width=20, bg=en, font=("impact", 12), fg=li, command=clicked)
btn2.grid(row=3, column=3)

a.mainloop()
