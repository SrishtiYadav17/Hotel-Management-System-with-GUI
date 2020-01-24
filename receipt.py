from __main__ import *
import sys

from tkinter import *

fo1=open("recipt.txt","r")
list1=fo1.readlines()

del list1[1]
del list1[2]
del list1[3]
del list1[4]
del list1[5]
list1[0]=list1[0][:-1]
list1[1]=list1[1][:-1]
list1[2]=list1[2][:-1]
list1[3]=list1[3][:-1]
list1[4]=list1[4][:-1]

p='''
----------------------------------------------
********  MARIGOLD HOTEL AND RESORTS ****
**********SHILLONG, MEGHALAYA*********
*******SERVING GUESTS SINCE 1990*********
-----------------------------------------------
NAME-%s
ADDRESS-%s
MOBILE NO.-%s
YOUR TOTAL BILL IS Rs.-%s
YOUR ROOM NUMBER IS %s    
     
     
     
'''%(list1[0],list1[1],list1[2],list1[4],list1[3])

        





class recipt:
    def __init__(self):
        root=Tk()
        _bgcolor = '#d9d9d9'  
        _fgcolor = '#000000'  
        _compcolor = '#d9d9d9' 
        _ana1color = '#d9d9d9' 
        _ana2color = '#d9d9d9' 

        root.geometry("800x800")
        root.title("recipt")
        root.configure(background="#d9d9d9")



        self.Label1 = Label(root)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.place(relx=0, rely=0, height=800, width=800)
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text=p)
        self.Label1.configure(anchor=N)

        self.Label1.configure(wraplength=1000)
        self.Label1.configure(justify =LEFT)

        self.Label1.configure(width=582)
        root.mainloop()


if __name__ == '__main__':
    recipt1=recipt()