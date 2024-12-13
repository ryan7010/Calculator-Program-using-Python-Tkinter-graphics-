#A calculator python program (with graphics)
#Used to add, subtract, multiply or divide
#So let's start our program
#-------------------------------------------------------------
#Getting ready with the materials
from tkinter import messagebox
from tkinter import*
from sumc import*
from difc import*
from proc import*
from divc import*

#------------Making the main window---------------------
top_main = Tk()
top_main.geometry("300x300")
top_main.title("Calculator")
def add_b():
    top_add.deiconify()
def sub_b():
    top_sub.deiconify()
def mul_b():
    top_mul.deiconify()
def div_b():
    top_div.deiconify()
lb_main = Label(top_main,text="What do you want to do?",bg="yellow",fg="purple",width=40,height=5).place(x=583,y=89)
btn_add = Button(top_main,text="Add",bg="orange",fg="black",width=5,height=3,command=add_b).place(x=383,y=250)
btn_sub = Button(top_main,text="Subtract",bg="purple",fg="pink",width=7,height=3,command=sub_b).place(x=583,y=250)
btn_mul = Button(top_main,text="Multiply",bg="green",fg="light blue",width=7,height=3,command=mul_b).place(x=783,y=250)
btn_div = Button(top_main,text="Divide",bg="white",fg="black",width=5,height=3,command=div_b).place(x=983,y=250)
#------------Finished the main window------------
#-------------------------------------
#To run the program:
#Click on Run > Run module to see the program in action.
#--------------------------
#Made by: Ryan Rodrigues
#Used the app: Python (3.8.7)


