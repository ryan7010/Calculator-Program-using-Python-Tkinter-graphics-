from tkinter import messagebox
from tkinter import*
top_mul  = Tk()
top_mul.withdraw()
top_mul.geometry("300x300")
top_mul.title("Multiply")
top_mul['bg']="#00DC00"
def mul():
    try:
        f = firstNum.get()
        s = secondNum.get()
        messagebox.showinfo("Multiply",f*s)
    except Exception as e:
        messagebox.showerror("Error",e)
    

	
firstNum=IntVar()
secondNum=IntVar()
def hide_window():
    top_mul.withdraw()
Label(top_mul,text="First number",width="13").place(x=50,y=50)
Label(top_mul,text="Second number",width="13").place(x=50,y=90)
Entry(top_mul,textvariable=firstNum).place(x=150,y=50)
Entry(top_mul,textvariable=secondNum).place(x=150,y=90)
Button(top_mul,text="Multiply",width="6",bg="red",fg="white",command=mul).place(x=100,y=120)
Button(top_mul,text="Hide window",command=hide_window).place(x=100,y=220)

