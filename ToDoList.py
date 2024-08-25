from tkinter import *
from tkinter import messagebox

#create GUI window
root = Tk()
root.title("ToDo list")
root.geometry("550x550")


global i
i=-1
j=-1

#Function for adding tasks
def onclick():
     global i
     if(entry.get() == ''):
          messagebox.showwarning("Warning","Please enter a task")
     else:
          i += 1
          list1.insert(i,entry.get())

#function for adding tasks from to do list to completed tasks list
def completed():
     global j
     global i
     selected_items = list1.curselection()
     if(len(selected_items) == 0):
          messagebox.showwarning("Warning","Please select a task")
     else:
          for item in selected_items:
               j += 1
               list2.insert(j, list1.get(item))
               list1.delete(item)
               i-=1

#function to remove tasks from the list
def remove():
     global i
     global j
     if(i==-1 and j==-1):
          messagebox.showwarning("Warning","Please enter a task")
          return
     selected_items = list1.curselection()
     selected_items1 = list2.curselection()
     if(len(selected_items)==0 and len(selected_items1)==0):
               list1.delete(i)
               i-=1
     for item in selected_items:
          list1.delete(item)
          i-=1
     for item in selected_items1:
          list2.delete(item)
          j-=1

#function to edit the tasks in the list
def update():
     if(entry.get() == ''):
          messagebox.showwarning("Warning","Please enter the task")
          return
     selected_item = list1.curselection()
     if(len(selected_item)==0):
          messagebox.showwarning("Warning","Please select a task to edit")
     for item in selected_item:
          list1.delete(item)
          list1.insert(item,entry.get())

label = Label(root,text = "To-Do-List App",bg="yellow",fg="black",height=2,width=30,font="lucida 10 bold").place(x=155,y=10)
entry = Entry(root)
entry.pack(fill=X,ipadx=2,pady=80,padx=150)

#creating the list box and placing it in the GUI window
list1 = Listbox(root,width=50,height=10)
list1.pack(fill=Y,ipadx=2,pady=1,padx=150)

#labels
tasksToDo = Label(root,text = "Tasks To Do",bg="light green",fg="black",height=2,width=10,font="lucida 10 bold").place(x=45,y=250)
#creating listbox for completed tasks
list2 = Listbox(root,width=50,height=10)
list2.pack(fill=Y,ipadx=2,pady=5,padx=150)
tasksCompleted = Label(root,text = "Tasks Completed",bg="light green",fg="black",height=2,width=15,font="lucida 10 bold").place(x=15,y=380)

#creating buttons and placing it in the GUI window
button = Button(root,text="Add Task",command=onclick)
button.place(x=245,y=110)
button1 = Button(root,text="Mark as completed",command=completed)
button1.place(x=150,y=150)
button2 = Button(root,text="Remove Task",command=remove)
button2.place(x=320,y=150)
button2 = Button(root,text="Edit Task",command=update)
button2.place(x=260,y=150)

#Run the GUI application
root.mainloop()

