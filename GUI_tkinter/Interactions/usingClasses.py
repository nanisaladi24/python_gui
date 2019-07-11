from tkinter import *

class prac:

    def __init__(self,myMaster):

        frame = Frame(myMaster)
        frame.pack()

        printButton = Button(myMaster,text="Print",command=self.printMsg) #please remember "()" are not needed for functions
        quitButton = Button(myMaster,text="Quit",command=myMaster.quit)

        printButton.pack(side=LEFT)
        quitButton.pack(side=RIGHT)

    def printMsg(self):
        print ("Hello .. I'm print here")
    

root = Tk()

prac(root)

root.mainloop()