from tkinter import *
import string
import random
from tkinter import messagebox

#Create the GUI window
root = Tk()
root.geometry("550x550")
root.title("Password_generator")

#function for generating the password
def onclick():
    if(entry.get()==""):
        messagebox.showwarning("Warning", "Please enter the length of the password")
        return
    len = int(entry.get())
    if(len<=0):
        lb1.config(text="Invalid length")
        return
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    password = "".join(random.sample(s,len))
    lb1.config(text="Generated password")
    lb2.config(text=password)

label = Label(root,text = "Password Generator",bg="yellow",fg="black",height=2,width=30,font="lucida 10 bold").place(x=155,y=10)

label = Label(root,text = "Enter the length of the password",fg="black",height=2,width=30,font="lucida 10 bold").place(x=155,y=50)

#entry widget for specifying the length of the password
entry = Entry(root)
entry.pack(fill=X,ipadx=2,pady=90,padx=150)

#button for generate password
button = Button(root,text="Generate password",command=onclick)
button.place(x=215,y=120)


lb1 = Label(root,text = "",fg="black",height=2,width=30,font="lucida 10 bold")
lb1.place(x=155,y=150)
#label for displaying the generated password
lb2 = Label(root,width=25,height=1,text="",font="Helvetica 40 bold")
lb2.pack()
root.mainloop()