from tkinter import *
import string
import random
from tkinter import messagebox

# Create the GUI window
root = Tk()
root.geometry("600x600")
root.title("Password Generator")

# Function for generating the password
def onclick():
    if entry.get() == "":
        messagebox.showwarning("Warning", "Please enter the length of the password")
        return
    length = int(entry.get())
    if length <= 0:
        lb1.config(text="Invalid length")
        return
    s1 = string.ascii_letters
    s2 = string.digits
    s3 = string.punctuation
    s = []
    s.extend(list(s1))
    s.extend(list(s2))
    s.extend(list(s3))
    password = "".join(random.sample(s, length))
    lb1.config(text="Generated Password:")
    lb2.config(text=password)

# Function to copy password to clipboard
def copy_to_clipboard():
    password = lb2.cget("text")  # Get the generated password
    if password:  # Check if there is a password to copy
        root.clipboard_clear()  # Clear the clipboard
        root.clipboard_append(password)  # Append the password to the clipboard
        messagebox.showinfo("Info", "Password copied to clipboard!")  # Notify user
    else:
        messagebox.showwarning("Warning", "No password to copy!")

# Create UI elements
header_label = Label(root, text="Password Generator", bg="yellow", fg="black", height=2, width=30, font="lucida 14 bold")
header_label.pack(pady=10)

instruction_label = Label(root, text="Enter the length of the password:", fg="black", height=2, width=30, font="lucida 12 bold")
instruction_label.pack(pady=10)

# Entry widget for specifying the length of the password
entry = Entry(root, font="lucida 12")
entry.pack(fill=X, ipadx=2, pady=10, padx=150)

# Button for generating password
button = Button(root, text="Generate Password", command=onclick, font="lucida 12 bold")
button.pack(pady=10)

# Label to indicate generated password
lb1 = Label(root, text="", fg="black", height=2, width=30, font="lucida 12 bold")
lb1.pack(pady=10)

# Label for displaying the generated password
lb2 = Label(root, width=40, height=2, text="", font="Helvetica 24 bold")
lb2.pack(pady=20)

# Button to copy password to clipboard
copy_button = Button(root, text="Copy to Clipboard", command=copy_to_clipboard, font="lucida 12 bold")
copy_button.pack(pady=10)

# Run the GUI application
root.mainloop()
