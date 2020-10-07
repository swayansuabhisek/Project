from tkinter import *

def submit():
    getf = first.get()
    getl = last.get()
    geta=age.get()


    file = open('database.txt','a')
    file.write(getf+","+getl+","+str(geta)+"\n")
    file.close()
    
    print("USER REGISTERED SUCCESFUL")

win = Tk()
win . title("REGISTRATION FORM")
win.geometry("350x350")

l1 = Label(win , text="REGISTER NOW", bg="black",fg="white",font="times 12")
l1.pack()

first= StringVar()
last = StringVar()
age = IntVar()

Label(win,text="FIRST NAME :",bg="black",fg="white") .place(x=50,y=60)
entry_first = Entry(win,textvariable=first)
entry_first.place (x=150,y=60)

Label(win,text="LAST NAME :",bg="black",fg="white") .place(x=50,y=120)
entry_last = Entry(win,textvariable=last)
entry_last.place (x=150,y=120)

Label(win,text="AGE :",bg="black",fg="white") .place(x=50,y=180)
entry_age = Entry(win,textvariable=age)
entry_age.place (x=150,y=180)

Button(win,text="SUBMIT",bg="black",fg="white",font="times 12",command =  submit) .place(x=100,y=240)
