from tkinter import messagebox
from tkinter import*
top_div  = Tk()
top_div.withdraw()
top_div.geometry("300x300")
top_div.title("Divide")
top_div['bg']="#FFFF00"
def div():
    try:
        f = firstNum.get()
        s = secondNum.get()
        messagebox.showinfo("Divide",f/s)
    except Exception as e:
        messagebox.showerror("Error",e)
    

	
firstNum=IntVar()
secondNum=IntVar()
def hide_window():
    top_div.withdraw()
Label(top_div,text="First number",width="13").place(x=50,y=50)
Label(top_div,text="Second number",width="13").place(x=50,y=90)
Entry(top_div,textvariable=firstNum).place(x=150,y=50)
Entry(top_div,textvariable=secondNum).place(x=150,y=90)
Button(top_div,text="Divide",width="6",bg="orange",command=div).place(x=100,y=120)
Button(top_div,text="Hide window",command=hide_window).place(x=100,y=220)
