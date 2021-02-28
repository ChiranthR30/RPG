import random
import string as s
from tkinter import *
import pyperclip as p


root=Tk()
root.geometry('750x750')
root.title('Random Password Generator')

createLabel=Label(root,text='PASSWORD LENGTH')
createLabel.pack()



length=IntVar()
dropdown=Spinbox(root,from_=8,to_=12,textvariable=length,width=30,bg='blue',font=25)
dropdown.pack()

v=Label(root,text='')
v.pack()


pass_str=StringVar()


def f1():
    x=s.ascii_letters+s.digits+s.punctuation

    y=random.sample(x,length.get())
    u=''.join(y)
    pass_str.set(u)


i=Button(root,text='Generate Password',command=f1,bg='yellow',font=10)
i.pack()

v=Label(root,text='')
v.pack()

k=Entry(root , textvariable = pass_str,bg='maroon',font=35).pack()


j=Label(root,text='Password length greater than 10 recomended!',fg='dark green')
j.place(x=75,y=380)

def copy():
    p.copy(pass_str.get())
    lab3=Label(root,text='Successfuly copied to clipboard!')
    lab3.pack()



b2=Button(root,text='Copy here',command=copy,font=1,bg='green')
b2.pack()

im=PhotoImage('wm2.gif')
lab5=Label(root,image=im)
lab5.pack()

root.mainloop()


