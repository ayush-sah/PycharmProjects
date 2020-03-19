from tkinter import *

window = Tk()

window.title("Create your Google Account")
window.geometry('748x500')

window.configure(background="white")
canvas = Canvas(window, width=748, height=1024, bd=2, bg="#fff")
canvas.pack(anchor=CENTER)

# Google logo
logo = PhotoImage(file="logo.png")
canvas.create_image(60, 50, anchor=NW, image=logo)

# Start text
canvas.create_text(235, 100, fill="black", font="arial 18", text="Create your own Google Account")

# Input first name
fname = Entry(window)
fname.insert(0, 'First name')
fname.configure(state=DISABLED)
canvas.create_window(150, 160, window=fname, height=36, width=176)

# Input last name
lname = Entry(window)
lname.insert(0, 'Last name')
lname.configure(state=DISABLED)
canvas.create_window(350, 160, window=lname, height=36, width=176)

# Input Username
uname = Entry(window)
uname.insert(0, 'Username')
uname.configure(state=DISABLED)
canvas.create_window(225, 240, window=uname, height=36, width=330)

mail = Label(window, text="@gmail.com", bg="white").place(x=390, y=238)

options = Label(window, text="You can use letters, numbers & periods", bg="white").place(x=58, y=265)

# Input Password
passwd = Entry(window)
passwd.insert(0, 'Password')
passwd.configure(state=DISABLED)
canvas.create_window(150, 330, window=passwd, height=36, width=176)

# Input Confirm Password
confirm = Entry(window)
confirm.insert(0, 'Confirm')
confirm.configure(state=DISABLED)
canvas.create_window(350, 330, window=confirm, height=36, width=176)

options = Label(window, text="Use 8 or more characters with a mix of letters, numbers & symbols", bg="white").place(
    x=60, y=360)

nextButton = Button(window, text="Next", bg="#1a73e8", fg="white", width=10, height=2).place(x=325, y=400)

account = PhotoImage(file="account.png")
canvas.create_image(500, 120, anchor=NW, image=account)


label1 = Label(window, text="One account. All of Google", bg="white").place(x=540, y=350)

label2 = Label(window, text="working for you.", bg="white").place(x=570, y=370)


def on_click(event):
    fname.configure(state=NORMAL)
    fname.delete(0, END)
    fname.unbind('<Button-1>', on_click_id)


on_click_id = fname.bind('<Button-1>', on_click)


def on_click1(event):
    lname.configure(state=NORMAL)
    lname.delete(0, END)
    lname.unbind('<Button-1>', on_click_id1)


on_click_id1 = lname.bind('<Button-1>', on_click1)


def on_click2(event):
    uname.configure(state=NORMAL)
    uname.delete(0, END)
    uname.unbind('<Button-1>', on_click_id2)


on_click_id2 = uname.bind('<Button-1>', on_click2)


def on_click3(event):
    passwd.configure(state=NORMAL)
    passwd.delete(0, END)
    passwd.unbind('<Button-1>', on_click_id3)


on_click_id3 = passwd.bind('<Button-1>', on_click3)


def on_click4(event):
    confirm.configure(state=NORMAL)
    confirm.delete(0, END)
    confirm.unbind('<Button-1>', on_click_id4)


on_click_id4 = confirm.bind('<Button-1>', on_click4)

window.mainloop()
