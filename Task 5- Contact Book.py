import tkinter as tk
from tkinter import messagebox

contacts = []

# ---------------- Functions ---------------- #

def clear_fields():
    name_entry.delete(0, tk.END)
    phone_entry.delete(0, tk.END)
    email_entry.delete(0, tk.END)
    address_entry.delete(0, tk.END)


def refresh_list():
    listbox.delete(0, tk.END)
    for contact in contacts:
        listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")


def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    address = address_entry.get()

    if name == "" or phone == "":
        messagebox.showwarning("Warning", "Name and Phone are required!")
        return

    contacts.append({
        "Name": name,
        "Phone": phone,
        "Email": email,
        "Address": address
    })

    refresh_list()
    clear_fields()
    messagebox.showinfo("Success", "Contact Added Successfully!")


def search_contact():
    keyword = name_entry.get().lower()

    listbox.delete(0, tk.END)

    found = False
    for contact in contacts:
        if keyword in contact["Name"].lower() or keyword in contact["Phone"]:
            listbox.insert(tk.END, f"{contact['Name']} - {contact['Phone']}")
            found = True

    if not found:
        messagebox.showinfo("Search", "No Contact Found")


def load_contact(event):
    selected = listbox.curselection()

    if selected:
        index = selected[0]
        item = listbox.get(index)
        phone = item.split(" - ")[1]

        for contact in contacts:
            if contact["Phone"] == phone:
                clear_fields()
                name_entry.insert(0, contact["Name"])
                phone_entry.insert(0, contact["Phone"])
                email_entry.insert(0, contact["Email"])
                address_entry.insert(0, contact["Address"])
                break


def update_contact():
    phone = phone_entry.get()

    for contact in contacts:
        if contact["Phone"] == phone:
            contact["Name"] = name_entry.get()
            contact["Email"] = email_entry.get()
            contact["Address"] = address_entry.get()

            refresh_list()
            clear_fields()
            messagebox.showinfo("Updated", "Contact Updated Successfully!")
            return

    messagebox.showerror("Error", "Contact Not Found")


def delete_contact():
    phone = phone_entry.get()

    for contact in contacts:
        if contact["Phone"] == phone:
            contacts.remove(contact)
            refresh_list()
            clear_fields()
            messagebox.showinfo("Deleted", "Contact Deleted Successfully!")
            return

    messagebox.showerror("Error", "Contact Not Found")


# ---------------- GUI ---------------- #

root = tk.Tk()
root.title("Contact Book")
root.geometry("700x600")
root.configure(bg="#E6E6FA")

title = tk.Label(
    root,
    text="📒 Contact Book",
    font=("Arial", 22, "bold"),
    bg="#E6E6FA",
    fg="#4B0082"
)
title.pack(pady=15)

frame = tk.Frame(root, bg="#E6E6FA")
frame.pack()

# Labels and Entries

tk.Label(frame, text="Name", font=("Arial", 12, "bold"),
         bg="#E6E6FA", fg="#4B0082").grid(row=0, column=0, pady=8, padx=10)

name_entry = tk.Entry(frame, width=35, font=("Arial", 11))
name_entry.grid(row=0, column=1)

tk.Label(frame, text="Phone", font=("Arial", 12, "bold"),
         bg="#E6E6FA", fg="#4B0082").grid(row=1, column=0, pady=8)

phone_entry = tk.Entry(frame, width=35, font=("Arial", 11))
phone_entry.grid(row=1, column=1)

tk.Label(frame, text="Email", font=("Arial", 12, "bold"),
         bg="#E6E6FA", fg="#4B0082").grid(row=2, column=0, pady=8)

email_entry = tk.Entry(frame, width=35, font=("Arial", 11))
email_entry.grid(row=2, column=1)

tk.Label(frame, text="Address", font=("Arial", 12, "bold"),
         bg="#E6E6FA", fg="#4B0082").grid(row=3, column=0, pady=8)

address_entry = tk.Entry(frame, width=35, font=("Arial", 11))
address_entry.grid(row=3, column=1)

# Buttons

button_frame = tk.Frame(root, bg="#E6E6FA")
button_frame.pack(pady=20)

button_color = "#9370DB"

tk.Button(button_frame, text="Add Contact",
          bg=button_color, fg="white",
          width=14, font=("Arial", 10, "bold"),
          command=add_contact).grid(row=0, column=0, padx=5)

tk.Button(button_frame, text="Search",
          bg=button_color, fg="white",
          width=14, font=("Arial", 10, "bold"),
          command=search_contact).grid(row=0, column=1, padx=5)

tk.Button(button_frame, text="Update",
          bg=button_color, fg="white",
          width=14, font=("Arial", 10, "bold"),
          command=update_contact).grid(row=0, column=2, padx=5)

tk.Button(button_frame, text="Delete",
          bg=button_color, fg="white",
          width=14, font=("Arial", 10, "bold"),
          command=delete_contact).grid(row=0, column=3, padx=5)

tk.Button(button_frame, text="View All",
          bg=button_color, fg="white",
          width=14, font=("Arial", 10, "bold"),
          command=refresh_list).grid(row=1, column=1, pady=10)

tk.Button(button_frame, text="Clear",
          bg="#BA55D3", fg="white",
          width=14, font=("Arial", 10, "bold"),
          command=clear_fields).grid(row=1, column=2, pady=10)

# Listbox

listbox = tk.Listbox(
    root,
    width=70,
    height=12,
    font=("Arial", 11),
    bg="white",
    fg="#4B0082",
    selectbackground="#9370DB",
    selectforeground="white"
)

listbox.pack(pady=10)
listbox.bind("<<ListboxSelect>>", load_contact)

root.mainloop()
