import os
from tkinter import *

file = open("password.txt", "w")

root = Tk()
root.title("Lock App")
root.configure(bg="black")

#guide
info = Label(root, text="Create a password or login", fg="white", bg="black", font=100)
info.grid(row=0, column=0)

def create():
    new = Tk()
    new.title("Create a Password")
    new.configure(bg="black")
    newp = Label(new, text="Type in Passoword", fg="white", bg="black")
    rep = Label(new, text="Retype Passoword", fg="white", bg="black")

    pass1 = Entry(new, text="", fg="white", bg="black")
    pass2 = Entry(new, text="", fg="white", bg="black")

    def check(pass1=pass1):
        if pass1.get() and pass2.get() == "0":
            reset = ""
            file = open("password.txt", "w")
            file.write(reset)
            help = Label(root, text="Password reset", fg="green", bg="black")
            help.grid(row=0, column=1)

            if pass2.get() == pass1.get():
                file = open("password.txt", "w")
                file.write(pass2.get())
                file.close()
                os.startfile("C:/Users/orhan/AppData/Roaming/uTorrent/uTorrent.exe")
            else:
                print("Not matching")

        if pass2.get() == pass1.get():
            file = open("password.txt", "w")
            file.write(pass2.get())
            file.close()
            os.startfile("C:/Users/orhan/AppData/Roaming/uTorrent/uTorrent.exe")
        else:
            print("Not matching")

    pass1.grid(row=1, column=1)
    pass2.grid(row=2, column=1)
    newp.grid(row=1, column=0)
    rep.grid(row=2, column=0)

    cre = Button(new, text="Create", command=check,fg="green", bg="white", width=16)
    cre.grid(row=3, column=1)


    new.mainloop()


def log():
    logs = Tk()
    logs.title("Login")
    logs.configure(bg="black")

    lo = Label(logs, text="Type in password", fg="white", bg="black")

    value = Entry(logs, text="", fg="white", bg="black")
    value.grid(row=0, column=1)
    lo.grid(row=0, column=0)

    def check1():
        file = open("password.txt", "r")
        if value.get() == file.read():
            os.startfile("C:/Users/orhan/AppData/Roaming/uTorrent/uTorrent.exe")

    logins = Button(logs, text="Login", command=check1, fg="green", bg="white")
    logins.grid(row=1, column=1)


one = Button(root, text="Create a password", command=create, fg="green", bg="white")
two = Button(root, text="Login",command=log, fg="green", bg="white")

one.grid(row=2, column=0)
two.grid(row=3, column=0)
root.mainloop()