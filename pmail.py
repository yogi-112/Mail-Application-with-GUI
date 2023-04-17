from tkinter import *
from tkinter.ttk import *
import smtplib

# main Screen
master = Tk()
master.title("Python Mail")

# functions
def send():
    try:
        username = temp_username.get()
        password = temp_password.get()
        to = temp_receiver.get()
        subject = temp_subject.get()
        body = temp_body.get()
        if username == "" or password == "" or to == "" or subject == "" or body == "":
            notif.config(text="Fill all fields", fg="pink")
            return
        else:
            finalmessage = 'Subject: {}\n\n{}'.format(subject, body)
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(username, password)
            server.sendmail(username, to, finalmessage)
            notif.config(text='Mail sent', fg='green')
    except:
        notif.config(text="Error", fg='red')


def reset():
    usernameEntry.delete(0, 'end')
    passwordEntry.delete(0, 'end')
    receiverEntry.delete(0, 'end')
    subjectEntry.delete(0, 'end')
    subjectbody.delete(0, 'end')


# animations
Label(master, text="Custom Mail", font=('Calibri', 15)).grid(row=0, sticky=N)
Label(master, text="Use below form to send mail", font=('Calibri', 11)).grid(row=1, sticky=W, padx=5)

Label(master, text="Email", font=('Calibri', 11)).grid(row=2, sticky=W, padx=5)
Label(master, text="Password", font=('Calibri', 11)).grid(row=3, sticky=W, padx=5)
Label(master, text="To", font=('Calibri', 11)).grid(row=4, sticky=W, padx=5)
Label(master, text="Subject", font=('Calibri', 11)).grid(row=5, sticky=W, padx=5)
Label(master, text="Body", font=('Calibri', 11)).grid(row=6, sticky=W, padx=5)

notif = Label(master, text="", font=('Calibri', 11))
notif.grid(row=7, sticky=S, padx=5)

# storage
temp_username = StringVar()
temp_password = StringVar()
temp_receiver = StringVar()
temp_subject = StringVar()
temp_body = StringVar()

# entry
usernameEntry = Entry(master, textvariable=temp_username)
usernameEntry.grid(row=2, column=0)
passwordEntry = Entry(master, show="*", textvariable=temp_password)
passwordEntry.grid(row=3, column=0)
receiverEntry = Entry(master, textvariable=temp_receiver)
receiverEntry.grid(row=4, column=0)
subjectEntry = Entry(master, textvariable=temp_subject)
subjectEntry.grid(row=5, column=0)
subjectbody = Entry(master, textvariable=temp_body)
subjectbody.grid(row=6, column=0)

# buttons
Button(master, text="Send", command=send).grid(row=7, sticky=W, pady=15, padx=5)
Button(master, text="Reset", command=reset).grid(row=7, sticky=E, pady=15, padx=5)

master.mainloop()
