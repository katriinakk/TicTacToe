

from tkinter import *
from tkinter import messagebox, font
logs = Tk() #izveido logu
logs.title("TicTacToe")
#logs.geometry("500x350")

playerX = True
count=0

def btnClick(button):
    global playerX,count
    if button["text"]==""and playerX==True:
        button["text"]="X"
        playerX=False
        count+=1
        
    elif button["text"]==""and playerX==False:
        button["text"]="0"
        playerX=True
        count+=1

def checkWinner()
    global winner
    winner=False
if (btn1["text"]=="X" and btn2["text"]=="X" and btn3["text"]=="X" or btn2["text"]=="X" and btn3["text"]=="X" and btn4["text"]=="X" ):

btn1= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn1))
btn2= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn2))
btn3= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn3))
btn4= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn4))
btn5= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn5))
btn6= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn6))
btn7= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn7))
btn8= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn8))
btn9= Button(logs, text="",width=6,height=3,font=('Fixedsys', 24), command=lambda:btnClick(btn9))

btn1.grid(row=0, column=0)
btn2.grid(row=0, column=1)
btn3.grid(row=0, column=2)
btn4.grid(row=1, column=0)
btn5.grid(row=1, column=1)
btn6.grid(row=1, column=2)
btn7.grid(row=2, column=0)
btn8.grid(row=2, column=1)
btn9.grid(row=2, column=2)


logs.mainloop()