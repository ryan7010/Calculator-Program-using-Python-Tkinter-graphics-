from tkinter import messagebox
from tkinter import*
top_add  = Tk()
top_add.withdraw()
top_add.geometry("300x300")
top_add.title("Add")
top_add['bg']="#51E1DC"
def add():
    try:
        f = firstNum.get()
        s = secondNum.get()
        messagebox.showinfo("Add",f+s)
    except Exception as e:
        messagebox.showerror("Error",e)
    

	
firstNum=IntVar()
secondNum=IntVar()
def hide_window():
    top_add.withdraw()
Label(top_add,text="First number",width="13").place(x=50,y=50)
Label(top_add,text="Second number",width="13").place(x=50,y=90)
Entry(top_add,textvariable=firstNum).place(x=150,y=50)
Entry(top_add,textvariable=secondNum).place(x=150,y=90)
Button(top_add,text="Add",width="5",bg="orange",command=add).place(x=100,y=120)
Button(top_add,text="Hide window",command=hide_window).place(x=100,y=220)

