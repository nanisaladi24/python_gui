#part 1 - checkbox

from tkinter import *

root = Tk()

l1 = Label(root,text="label 1",fg="black")

l1.pack()

def trial():
    if var.get()==1:
        print ("hello")
    else:
        print ("bla bla")

var=IntVar()
cb = Checkbutton(root,text="please check", command=trial,variable=var)

cb.pack()

#root.mainloop()

#part 2 - button

#def butCom():
#    print ("clicked")


def butCom(event):
    print ("clicked based on event")

#but1= Button(root,text="click here",command=butCom) #works for any button

but1= Button(root,text="click here")
but1.bind("<Button-1>",butCom) #specific to left click

but1.pack()

root.mainloop()