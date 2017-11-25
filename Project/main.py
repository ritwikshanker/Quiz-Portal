from Tkinter import *
import os
root=Tk()
root.title("Student Details")
Label(root,text="Name: Ritwik Shanker",font="Arial 20 italic").grid(row=2,column=0,sticky=W)
Label(root,text="Enroll. no.: 161B180",font="Arial 20 italic").grid(row=4,column=0,sticky=W)
Label(root,text="Mobile no: 8604605757",font="Arial 20 italic").grid(row=6,column=0,sticky=W)
Label(root,text="E-mail: ritwikshanker@yahoo.in",font="Arial 20 italic").grid(row=8,column=0,sticky=W)
Label(root,text="Project: Quiz Portal",font="Arial 20 italic").grid(row=9,column=0,sticky=W)
lb=Label(root,text="Batch: B6(BY)",font="Arial 20 italic")
lb.grid(row=11,column=0,sticky=W)
def func():
    root.destroy()
    os.startfile('portal.py')
lb.after(6000,func)
root.mainloop()
