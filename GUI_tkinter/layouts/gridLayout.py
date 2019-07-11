from tkinter import *

root = Tk()

l1 = Label(root,text="f1",fg="black",bg="yellow")
#l1.pack()
l2 = Label(root,text="Field2",fg="green")

e1 = Entry(root)
e2 = Entry(root)

l1.pack(fill=BOTH,expand=True)

l1.grid(row=0,column=0,sticky=E)
l2.grid(row=1,column=0,sticky=E)
e1.grid(row=0,column=1)
e2.grid(row=1,column=1)

b1 = Checkbutton(root,text="check check!",fg="Black")

b1.grid(row=2,columnspan=2)

root.anchor("center") #Super Feature. must be n, ne, e, se, s, sw, w, nw, or center

root2=root

root2.mainloop()

print ("hello")

root.mainloop()