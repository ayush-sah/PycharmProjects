from tkinter import *
import os


def run_pong():
    os.system('python Pong/pong.py')


def run_snake():
    os.system('python Snake/snake.py')


def run_si():
    os.system('python SpaceInvader/SpaceInvader.py')


def run_c4():
    os.system('python ConnectFour/connect4.py')


window = Tk()
window.title("Retro Gaming Station")

Label(window, text="Choose game to play.", fg="white", bg="dark blue", font="Helvetica 60 bold italic").place(relx=0.5, rely=0.1, anchor=CENTER)

Label(window, text="PONG", fg="black", font="Helvetica 30 bold").place(relx=0.13, rely=0.40, anchor=S)
pong = PhotoImage(file="pong.gif")
Button(window, text='Pong', image=pong, command=run_pong).place(relx=0.13, rely=0.40, anchor=N)

Label(window, text="CONNECT FOUR", fg="blue", font="Helvetica 30 bold").place(relx=0.38, rely=0.40, anchor=S)
c4 = PhotoImage(file="c4.png")
Button(window, text='Connect Four', image=c4, command=run_c4).place(relx=0.38, rely=0.40, anchor=N)

Label(window, text="SNAKE", fg="red", font="Helvetica 30 bold").place(relx=0.63, rely=0.40, anchor=S)
snake = PhotoImage(file="snake.png")
Button(window, text='Snake', image=snake, command=run_snake).place(relx=0.63, rely=0.40, anchor=N)

Label(window, text="SPACE INVADER", fg="purple", font="Helvetica 30 bold").place(relx=0.87, rely=0.40, anchor=S)
si = PhotoImage(file="si.png")
Button(window, text='Space Invader', image=si, command=run_si).place(relx=0.87, rely=0.40, anchor=N)

exit_image = PhotoImage(file="exit.png")
Button(window, text='Exit', image=exit_image, command=window.destroy).place(relx=0.5, rely=0.9, anchor=CENTER)
window.attributes("-fullscreen", True)

window.mainloop()
