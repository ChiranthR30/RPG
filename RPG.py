import random
import string as s
from tkinter import *


root=Tk()
root.geometry('400x400')
root.title('rpg')

createLabel=Label(root,text='PASS LENGTH')
createLabel.pack()

length=IntVar()
dropdown=Spinbox(root,from_=8,to_=12,textvariable=length,width=20)
dropdown.pack()



pass_str=StringVar()


def f1():
    x=s.ascii_letters+s.digits+s.punctuation

    y=random.sample(x,8)
    u=''.join(y)
    pass_str.set(u)

i=Button(root,text='generate pass',command=f1)
i.pack()
k=Entry(root , textvariable = pass_str).pack()

root.mainloop()


