import tkinter as tk
from tkinter import messagebox
import random
import string

# -------------------- Functions --------------------

def generate_password():
    try:
        length = int(length_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Please enter a valid password length.")
            return

        characters = string.ascii_letters + string.digits + string.punctuation
        password = "".join(random.choice(characters) for _ in range(length))

        password_entry.config(state="normal")
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
        password_entry.config(state="readonly")

    except ValueError:
        messagebox.showerror("Error", "Please enter numbers only.")

def clear_fields():
    length_entry.delete(0, tk.END)
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.config(state="readonly")

def copy_password():
    password = password_entry.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "Generate a password first.")

# -------------------- Main Window --------------------

root = tk.Tk()
root.title("Password Generator")
root.geometry("500x350")
root.resizable(False, False)
root.configure(bg="#1E88E5")

# -------------------- Heading --------------------

title = tk.Label(
    root,
    text="🔐 PASSWORD GENERATOR",
    font=("Arial", 20, "bold"),
    bg="#1E88E5",
    fg="white"
)
title.pack(pady=20)

# -------------------- Length --------------------

length_label = tk.Label(
    root,
    text="Enter Password Length",
    font=("Arial", 12),
    bg="#1E88E5",
    fg="white"
)
length_label.pack()

length_entry = tk.Entry(
    root,
    font=("Arial", 13),
    justify="center",
    width=20
)
length_entry.pack(pady=10)

# -------------------- Buttons --------------------

generate_btn = tk.Button(
    root,
    text="Generate Password",
    font=("Arial", 12, "bold"),
    bg="#0D47A1",
    fg="white",
    width=20,
    command=generate_password
)
generate_btn.pack(pady=10)

password_entry = tk.Entry(
    root,
    font=("Consolas", 12),
    width=35,
    justify="center",
    state="readonly"
)
password_entry.pack(pady=10)

copy_btn = tk.Button(
    root,
    text="Copy Password",
    font=("Arial", 12, "bold"),
    bg="#1565C0",
    fg="white",
    width=20,
    command=copy_password
)
copy_btn.pack(pady=5)

clear_btn = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12, "bold"),
    bg="#1976D2",
    fg="white",
    width=20,
    command=clear_fields
)
clear_btn.pack(pady=10)

# -------------------- Footer --------------------

footer = tk.Label(
    root,
    text="Developed using Python & Tkinter",
    font=("Arial", 10),
    bg="#1E88E5",
    fg="white"
)
footer.pack(side="bottom", pady=10)

root.mainloop()
