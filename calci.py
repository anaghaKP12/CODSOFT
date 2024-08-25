from tkinter import *
root = Tk()

scValue = ""
def reset():
    global scValue
    scValue = ""
    screen.config(text=scValue)
def display(value):
    global scValue
    scValue+=value
    screen.config(text=scValue)
def compute():
    global scValue
    answer = ""
    if scValue!="":
        try:
            answer = eval(scValue)
        except:
            answer = "error"
            scValue = ""
    screen.config(text=answer)
root.geometry("570x600+100+200")
root.title("Calculator")
root.configure(bg="light green")
root.resizable(False,False)
screen = Label(root,width=25,height=1,text="",font="lucida 40 bold")
screen.pack()
Button(root,width=5,height=1,text="C",font="lucida 30 bold",bd=1,command=lambda: reset()).place(x=10,y=100)
Button(root,width=5,height=1,text="/",font="lucida 30 bold",bd=1,command=lambda: display("/")).place(x=150,y=100)
Button(root,width=5,height=1,text="%",font="lucida 30 bold",bd=1,command=lambda: display("%")).place(x=290,y=100)
Button(root,width=5,height=1,text="*",font="lucida 30 bold",bd=1,bg="white",command=lambda: display("*")).place(x=430,y=100)

Button(root,width=5,height=1,text="7",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("7")).place(x=10,y=200)
Button(root,width=5,height=1,text="8",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("8")).place(x=150,y=200)
Button(root,width=5,height=1,text="9",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("9")).place(x=290,y=200)
Button(root,width=5,height=1,text="-",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("-")).place(x=430,y=200)

Button(root,width=5,height=1,text="4",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("4")).place(x=10,y=300)
Button(root,width=5,height=1,text="5",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("5")).place(x=150,y=300)
Button(root,width=5,height=1,text="6",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("6")).place(x=290,y=300)
Button(root,width=5,height=1,text="+",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("+")).place(x=430,y=300)

Button(root,width=5,height=1,text="1",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("1")).place(x=10,y=400)
Button(root,width=5,height=1,text="2",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("2")).place(x=150,y=400)
Button(root,width=5,height=1,text="3",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("3")).place(x=290,y=400)
Button(root,width=11,height=1,text="0",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display("0")).place(x=10,y=500)

Button(root,width=5,height=1,text=".",font="lucida 30 bold",bd=1,fg="black",bg="white",command=lambda: display(".")).place(x=290,y=500)
Button(root,width=5,height=3,text="=",font="lucida 30 bold",bd=1,fg="black",bg="#fe9037",command=lambda: compute()).place(x=430,y=400)
root.mainloop()