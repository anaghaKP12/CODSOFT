import tkinter as tk
from tkinter import messagebox
from tkinter import font
import re
import json
import os

# Initialize tkinter
root = tk.Tk()
root.title("Contact Management App")

# Create a list to store contacts
contacts = []

# File path for saving/loading contacts
contact_file = "contacts.json"

# Function to load contacts from file
def load_contacts():
    global contacts
    if os.path.exists(contact_file):
        with open(contact_file, 'r') as f:
            contacts = json.load(f)
            update_contact_list()

# Function to save contacts to file
def save_contacts():
    with open(contact_file, 'w') as f:
        json.dump(contacts, f)

# Function to add a contact
def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name and phone.isdigit() and len(phone) == 10 and is_valid_email(email):
        # Check for duplicates based on phone or email
        if any(contact['Phone'] == phone or contact['Email'] == email for contact in contacts):
            messagebox.showwarning("Warning", "Contact with this phone or email already exists!")
            return

        contact = {"Name": name, "Phone": phone, "Email": email, "Address": address}
        contacts.append(contact)
        save_contacts()  # Save to file
        clear_entries()
        update_contact_list()
    else:
        messagebox.showerror("Error", "Please enter valid Name, Phone (10 digits), and Email!")

# Function to validate email format
def is_valid_email(email):
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

# Function to view all contacts
def update_contact_list():
    contact_listbox.delete(0, tk.END)
    for contact in contacts:
        contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to search for a contact
def search_contact():
    search_term = search_entry.get().lower()
    found_contacts = [contact for contact in contacts if search_term in contact['Name'].lower() or search_term in contact['Phone']]
    
    contact_listbox.delete(0, tk.END)
    for contact in found_contacts:
        contact_listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")

# Function to clear search results
def clear_search():
    search_entry.delete(0, tk.END)
    update_contact_list()

# Function to update a contact
def update_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        new_name = name_entry.get()
        new_phone = phone_entry.get()
        new_email = email_entry.get()
        new_address = address_entry.get()

        if new_name and new_phone.isdigit() and len(new_phone) == 10 and is_valid_email(new_email):
            contacts[selected_index] = {"Name": new_name, "Phone": new_phone, "Email": new_email, "Address": new_address}
            save_contacts()  # Save to file
            clear_entries()
            update_contact_list()
        else:
            messagebox.showerror("Error", "Please enter valid Name, Phone (10 digits), and Email!")
    else:
        messagebox.showerror("Error", "Please select a contact to update!")

# Function to delete a contact
def delete_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        del contacts[selected_index]
        save_contacts()  # Save to file
        update_contact_list()
        clear_entries()
    else:
        messagebox.showerror("Error", "Please select a contact to delete!")

# Function to clear entry fields
def clear_entries():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)
    search_entry.delete(0, tk.END)

# Create and configure UI elements
name_label = tk.Label(root, text="Name:")
phone_label = tk.Label(root, text="Phone:")
email_label = tk.Label(root, text="Email:")
address_label = tk.Label(root, text="Address:")

name_entry = tk.Entry(root)
phone_entry = tk.Entry(root)
email_entry = tk.Entry(root)
address_entry = tk.Entry(root)

add_button = tk.Button(root, text="Add Contact", command=add_contact)
update_button = tk.Button(root, text="Update Contact", command=update_selected_contact)
delete_button = tk.Button(root, text="Delete Contact", command=delete_selected_contact)
search_button = tk.Button(root, text="Search", command=search_contact)
# clear_search_button = tk.Button(root, text="Clear Search", command=clear_search)

search_label = tk.Label(root, text="Search:")
search_entry = tk.Entry(root)

contact_listbox = tk.Listbox(root, selectmode=tk.SINGLE)
contact_listbox.bind("<<ListboxSelect>>", lambda event: load_selected_contact())

# Place UI elements on the grid
name_label.grid(row=0, column=0)
phone_label.grid(row=1, column=0)
email_label.grid(row=2, column=0)
address_label.grid(row=3, column=0)

name_entry.grid(row=0, column=1, padx=10, pady=5)
phone_entry.grid(row=1, column=1, padx=10, pady=5)
email_entry.grid(row=2, column=1, padx=10, pady=5)
address_entry.grid(row=3, column=1, padx=10, pady=5)

add_button.grid(row=4, column=0, columnspan=2, pady=10)
update_button.grid(row=5, column=0, columnspan=2, pady=10)
delete_button.grid(row=6, column=0, columnspan=2, pady=10)

search_label.grid(row=7, column=0)
search_entry.grid(row=7, column=1, padx=10, pady=5)
search_button.grid(row=8, column=0, columnspan=2, pady=5)
# clear_search_button.grid(row=8, column=1, pady=5)

contact_listbox.grid(row=0, column=2, rowspan=10, padx=10, pady=10, sticky="nsew")

# Configure grid columns and rows to expand with the window size
root.columnconfigure(2, weight=1)
root.rowconfigure(9, weight=1)

# Function to load the selected contact for updating
def load_selected_contact():
    selected_index = contact_listbox.curselection()
    if selected_index:
        selected_index = int(selected_index[0])
        contact = contacts[selected_index]
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        address_entry.delete(0, tk.END)
        name_entry.insert(0, contact["Name"])
        phone_entry.insert(0, contact["Phone"])
        email_entry.insert(0, contact["Email"])
        address_entry.insert(0, contact["Address"])

# Run the application
font_size = font.nametofont("TkDefaultFont")
font_size.configure(size=14)

# Apply the larger font size to UI elements
name_label["font"] = font_size
phone_label["font"] = font_size
email_label["font"] = font_size
address_label["font"] = font_size
name_entry["font"] = font_size
phone_entry["font"] = font_size
email_entry["font"] = font_size
address_entry["font"] = font_size
add_button["font"] = font_size
update_button["font"] = font_size
delete_button["font"] = font_size
search_label["font"] = font_size
search_entry["font"] = font_size
search_button["font"] = font_size
contact_listbox["font"] = font_size

# Set the window size
root.geometry("800x600")

# Load contacts and run the application
load_contacts()
update_contact_list()
root.mainloop()
