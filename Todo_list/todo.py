from tkinter import *
from tkinter import messagebox
import json
import os

# Create GUI window
root = Tk()
root.title("To-Do List")
root.geometry("600x600")

# Global variables
task_file = 'tasks.json'

# Load existing tasks from file
def load_tasks():
    if os.path.exists(task_file):
        with open(task_file, 'r') as f:
            tasks = json.load(f)
            for task in tasks['todo']:
                list1.insert(END, task)
            for task in tasks['completed']:
                list2.insert(END, task)

# Save tasks to file
def save_tasks():
    tasks = {
        'todo': list1.get(0, END),
        'completed': list2.get(0, END)
    }
    with open(task_file, 'w') as f:
        json.dump(tasks, f)

# Function for adding tasks
def onclick():
    if entry.get() == '':
        messagebox.showwarning("Warning", "Please enter a task")
    else:
        list1.insert(END, entry.get())
        entry.delete(0, END)  # Clear input field
        save_tasks()

# Function for adding tasks from To-Do list to Completed tasks list
def completed():
    selected_items = list1.curselection()
    if len(selected_items) == 0:
        messagebox.showwarning("Warning", "Please select a task")
    else:
        for item in selected_items[::-1]:  # Reverse to avoid index errors
            list2.insert(END, list1.get(item))
            list1.delete(item)
        save_tasks()

# Function to remove tasks from the list
def remove():
    selected_items = list1.curselection()
    selected_items1 = list2.curselection()
    if len(selected_items) == 0 and len(selected_items1) == 0:
        messagebox.showwarning("Warning", "Please select a task")
        return
    for item in selected_items[::-1]:
        list1.delete(item)
    for item in selected_items1[::-1]:
        list2.delete(item)
    save_tasks()

# Function to edit the tasks in the list
def update():
    selected_item = list1.curselection()
    if entry.get() == '':
        messagebox.showwarning("Warning", "Please enter the task")
        return
    if len(selected_item) == 0:
        messagebox.showwarning("Warning", "Please select a task to edit")
    else:
        for item in selected_item:
            list1.delete(item)
            list1.insert(item, entry.get())
        entry.delete(0, END)  # Clear input field
        save_tasks()

# Function to populate the input field when clicking a task
def populate_entry(event):
    selected_index = list1.curselection()
    if selected_index:
        entry.delete(0, END)  # Clear the entry field first
        entry.insert(0, list1.get(selected_index))  # Insert the selected task

# Create UI elements
label = Label(root, text="To-Do List App", bg="yellow", fg="black", height=2, width=30, font="lucida 14 bold")
label.pack(pady=10)

entry = Entry(root, font="lucida 12")
entry.pack(fill=X, ipadx=2, pady=10, padx=150)

# Create the list box for tasks
list1 = Listbox(root, width=50, height=10, font="lucida 12")
list1.pack(fill=Y, ipadx=2, pady=5, padx=150)
list1.bind('<ButtonRelease-1>', populate_entry)  # Bind click event

# Labels
tasksToDo = Label(root, text="Tasks To Do", bg="light green", fg="black", height=2, width=10, font="lucida 12 bold")
tasksToDo.pack()

# Create listbox for completed tasks
list2 = Listbox(root, width=50, height=10, font="lucida 12")
list2.pack(fill=Y, ipadx=2, pady=5, padx=150)

tasksCompleted = Label(root, text="Tasks Completed", bg="light green", fg="black", height=2, width=15, font="lucida 12 bold")
tasksCompleted.pack()

# Create buttons
button_frame = Frame(root)
button_frame.pack(pady=20)

button = Button(button_frame, text="Add Task", command=onclick, font="lucida 12")
button.grid(row=0, column=0, padx=5)

button1 = Button(button_frame, text="Mark as Completed", command=completed, font="lucida 12")
button1.grid(row=0, column=1, padx=5)

button2 = Button(button_frame, text="Remove Task", command=remove, font="lucida 12")
button2.grid(row=0, column=2, padx=5)

button3 = Button(button_frame, text="Edit Task", command=update, font="lucida 12")
button3.grid(row=0, column=3, padx=5)

# Load tasks on startup
load_tasks()

# Run the GUI application
root.mainloop()
