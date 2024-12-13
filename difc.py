from tkinter import messagebox
from tkinter import*
top_sub  = Tk()
top_sub.withdraw()
top_sub.title("Subtract")
top_sub.geometry("300x300")
top_sub['bg']="#FF0000"
def sub():
    try:
        f = firstNum.get()
        s = secondNum.get()
        messagebox.showinfo("Subtract",f-s)
    except Exception as e:
        messagebox.showerror("Error",e)
    

	
firstNum=IntVar()
secondNum=IntVar()
def hide_window():
    top_sub.withdraw()
Label(top_sub,text="First number",width="13").place(x=50,y=50)
Label(top_sub,text="Second number",width="13").place(x=50,y=90)
Entry(top_sub,textvariable=firstNum).place(x=150,y=50)
Entry(top_sub,textvariable=secondNum).place(x=150,y=90)
Button(top_sub,text="Subtract",width="6",bg="yellow",command=sub).place(x=100,y=120)
Button(top_sub,text="Hide window",command=hide_window).place(x=100,y=220)
