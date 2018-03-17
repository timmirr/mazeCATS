from Tkinter import *
import time
 
s = 1
 
def stopit():
    global s
    s = 1
    print "stopped"
 
def callback():
    global s
    s = 0
    if s == 0:
        print "called the callback!"
    root.after(3000, callback)
 
root = Tk()
root.geometry("200x200+200+200")
 
w = Button(root, text="START", command=callback)
s = Button(root, text="STOP", command=stopit)
w.pack()
s.pack()
root.mainloop()
