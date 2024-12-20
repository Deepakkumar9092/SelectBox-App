from tkinter import *

def myfun():
    ch1 = var1.get()
    ch2 = var2.get()
    ch3 = var3.get()

    if ch1==1:
        Label(s,text="You Selected C++",font=("Microsoft yahie Ui Light",14,'bold')).place(x=50,y=210)
    
    elif ch2==1:
        Label(s,text="You Selected Java",font=("Microsoft yahie Ui Light",14,"bold")).place(x=50,y=230)

    elif ch3==1:
        Label(s,text="You Selected Python",font=("Microsoft yahie Ui Light",14,"bold")).place(x=50,y=250)
    
    else:
        Label(s,text="Please Select One ->  C++ or Java or Python", font=("Time New Roman",15,"bold")).place(x=50,y=270)

s = Tk()
s.title("CheckBox")
s.geometry("400x300")
# s.resizable(False,False)
s.config(bg="#C73378")

lab = Label(s,text="Select Language",font=("Time New Roman",14,"bold"))
lab.place(x=110,y=10,height=40, width=150)

var1=IntVar()
var2 = IntVar()
var3=IntVar()

check1 = Checkbutton(s,text="C++",variable=var1,onvalue=1,offvalue=0)
check1.select()
check1.place(x=130,y=60,height=20, width=100)

check2 = Checkbutton(s,text="Java",variable=var2,onvalue=1,offvalue=0)
check2.deselect()
check2.place(x=130,y=80,height=20, width=100)

check3 = Checkbutton(s,text="Python",variable=var3,onvalue=1,offvalue=0)
check3.deselect()
check3.place(x=130,y=100,height=20, width=100)

button = Button(s, text="Submit",bd=3, font=("Time New Roman",12,"bold"),command=myfun)
button.place(x=130,y=130,height=50, width=100)

s.mainloop()