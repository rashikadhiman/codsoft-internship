import tkinter as tk
import random

# -------------------- Main Window --------------------

root = tk.Tk()
root.title("🌸 Rock Paper Scissors Game")
root.geometry("520x620")
root.configure(bg="#FFC0CB")
root.resizable(False, False)

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

# -------------------- Game Function --------------------

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    user_label.config(text=f"👩 You: {user_choice}")
    computer_label.config(text=f"💻 Computer: {computer_choice}")

    if user_choice == computer_choice:
        result = "🤝 It's a Tie!"
        color = "#FF1493"

    elif (user_choice == "Rock" and computer_choice == "Scissors") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissors" and computer_choice == "Paper"):

        result = "🎉 You Win!"
        color = "green"
        user_score += 1

    else:
        result = "😔 Computer Wins!"
        color = "red"
        computer_score += 1

    result_label.config(text=result, fg=color)
    score_label.config(
        text=f"Score : 👩 {user_score}   |   💻 {computer_score}"
    )

# -------------------- Reset --------------------

def reset_game():
    global user_score, computer_score

    user_score = 0
    computer_score = 0

    user_label.config(text="👩 You:")
    computer_label.config(text="💻 Computer:")
    result_label.config(text="", fg="#FF1493")
    score_label.config(text="Score : 👩 0   |   💻 0")

# -------------------- Heading --------------------

title = tk.Label(
    root,
    text="🌸 Rock Paper Scissors 🌸",
    font=("Comic Sans MS", 22, "bold"),
    bg="#FFC0CB",
    fg="#C71585"
)
title.pack(pady=20)

subtitle = tk.Label(
    root,
    text="Choose Your Move!",
    font=("Arial", 14),
    bg="#FFC0CB",
    fg="#8B008B"
)
subtitle.pack()

# -------------------- Buttons --------------------

frame = tk.Frame(root, bg="#FFC0CB")
frame.pack(pady=25)

button_style = {
    "font": ("Arial", 12, "bold"),
    "width": 12,
    "bg": "#FF69B4",
    "fg": "white",
    "activebackground": "#FF1493",
    "activeforeground": "white"
}

tk.Button(frame, text="🪨 Rock",
          command=lambda: play("Rock"),
          **button_style).grid(row=0, column=0, padx=6)

tk.Button(frame, text="📄 Paper",
          command=lambda: play("Paper"),
          **button_style).grid(row=0, column=1, padx=6)

tk.Button(frame, text="✂️ Scissors",
          command=lambda: play("Scissors"),
          **button_style).grid(row=0, column=2, padx=6)

# -------------------- Output --------------------

user_label = tk.Label(
    root,
    text="👩 You:",
    font=("Arial", 14),
    bg="#FFC0CB",
    fg="#8B008B"
)
user_label.pack(pady=8)

computer_label = tk.Label(
    root,
    text="💻 Computer:",
    font=("Arial", 14),
    bg="#FFC0CB",
    fg="#8B008B"
)
computer_label.pack(pady=8)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 18, "bold"),
    bg="#FFC0CB",
    fg="#FF1493"
)
result_label.pack(pady=20)

score_label = tk.Label(
    root,
    text="Score : 👩 0   |   💻 0",
    font=("Arial", 16, "bold"),
    bg="#FFC0CB",
    fg="#C71585"
)
score_label.pack(pady=10)

# -------------------- Reset Button --------------------

reset_btn = tk.Button(
    root,
    text="🔄 Reset Game",
    font=("Arial", 13, "bold"),
    bg="#FF1493",
    fg="white",
    width=20,
    activebackground="#C71585",
    activeforeground="white",
    command=reset_game
)
reset_btn.pack(pady=20)

# -------------------- Footer --------------------

footer = tk.Label(
    root,
    text="💖 Developed using Python & Tkinter 💖",
    font=("Arial", 10),
    bg="#FFC0CB",
    fg="#C71585"
)
footer.pack(side="bottom", pady=15)

root.mainloop()
