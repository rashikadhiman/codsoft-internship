import tkinter as tk
from tkinter import messagebox

# ---------------- Main Window ----------------
root = tk.Tk()
root.title("To-Do List")
root.geometry("450x550")
root.config(bg="#DFFFD6")   # Light Green Background

tasks = []

# ---------------- Functions ----------------
def add_task():
    task = entry.get().strip()
    if task == "":
        messagebox.showwarning("Warning", "Please enter a task!")
    else:
        tasks.append(task)
        update_listbox()
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()[0]
        tasks.pop(index)
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task.")

def complete_task():
    try:
        index = listbox.curselection()[0]
        if not tasks[index].startswith("✔ "):
            tasks[index] = "✔ " + tasks[index]
        update_listbox()
    except:
        messagebox.showwarning("Warning", "Please select a task.")

def clear_tasks():
    if messagebox.askyesno("Confirm", "Delete all tasks?"):
        tasks.clear()
        update_listbox()

def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# ---------------- Heading ----------------
title = tk.Label(
    root,
    text="🌿 TO-DO LIST 🌿",
    font=("Arial", 20, "bold"),
    bg="#DFFFD6",
    fg="#2E7D32"
)
title.pack(pady=15)

# ---------------- Entry ----------------
entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=25,
    bd=3
)
entry.pack(pady=10)

# ---------------- Buttons ----------------
button_frame = tk.Frame(root, bg="#DFFFD6")
button_frame.pack(pady=10)

add_btn = tk.Button(
    button_frame,
    text="Add",
    bg="#81C784",
    fg="white",
    font=("Arial", 11, "bold"),
    width=10,
    command=add_task
)
add_btn.grid(row=0, column=0, padx=5, pady=5)

delete_btn = tk.Button(
    button_frame,
    text="Delete",
    bg="#66BB6A",
    fg="white",
    font=("Arial", 11, "bold"),
    width=10,
    command=delete_task
)
delete_btn.grid(row=0, column=1, padx=5, pady=5)

complete_btn = tk.Button(
    button_frame,
    text="Complete",
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=10,
    command=complete_task
)
complete_btn.grid(row=1, column=0, padx=5, pady=5)

clear_btn = tk.Button(
    button_frame,
    text="Clear All",
    bg="#388E3C",
    fg="white",
    font=("Arial", 11, "bold"),
    width=10,
    command=clear_tasks
)
clear_btn.grid(row=1, column=1, padx=5, pady=5)

# ---------------- Listbox ----------------
listbox = tk.Listbox(
    root,
    font=("Arial", 13),
    width=35,
    height=15,
    bg="white",
    fg="#1B5E20",
    selectbackground="#A5D6A7",
    bd=3
)
listbox.pack(pady=20)

# ---------------- Run ----------------
root.mainloop()

