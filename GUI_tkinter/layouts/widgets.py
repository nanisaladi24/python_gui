from tkinter import *

root = Tk()

one = Label(root,text="one",fg="black",bg="red")
one.pack()
two = Label(root,text="two",fg="blue",bg="yellow")
two.pack(fill=X)
three = Label(root,text="three",fg="red",bg="green")
three.pack(side=LEFT,fill=Y)
four = Label(root,text="four",fg="green",bg="black")
four.pack(side=LEFT,fill=BOTH) #no idea how BOTH exactly works. Mostly it requires "expand=True".
five = Label(root,text="five",fg="blue",bg="green")
five.pack(expand=True)
six = Label(root,text="six",fg="green",bg="orange")
six.pack(expand=True,fill=BOTH)
root.mainloop()


