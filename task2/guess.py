import tkinter as tk
from tkinter import messagebox
import random

# Function to handle the guessing logic
def check_guess():
    global attempts
    try:
        guess = int(entry_guess.get())
        attempts += 1
        if guess < number_to_guess:
            result_label.config(text="Too low! Try again.", fg="#ffcc00")
        elif guess > number_to_guess:
            result_label.config(text="Too high! Try again.", fg="#ffcc00")
        else:
            result_label.config(text=f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.", fg="#00e676")
            messagebox.showinfo("Success!", f"You've guessed the number {number_to_guess} in {attempts} attempts!")
            reset_game()
    except ValueError:
        messagebox.showerror("Invalid Input", "Please enter a valid number.")

# Function to reset the game
def reset_game():
    global number_to_guess, attempts
    number_to_guess = random.randint(1, 100)
    attempts = 0
    entry_guess.delete(0, tk.END)
    result_label.config(text="Guess a number between 1 and 100", fg="#cccccc")

# Initialize the main window
root = tk.Tk()
root.title("Guessing Game")
root.geometry("450x300")
root.configure(bg="#1e1e2e")  # Dark theme
root.resizable(False, False)

# Initialize game variables
number_to_guess = random.randint(1, 100)
attempts = 0

# Styles
label_style = {'font': ('Helvetica', 13), 'bg': '#1e1e2e', 'fg': '#cccccc'}
entry_style = {'font': ('Helvetica', 14), 'width': 10, 'bg': '#33334d', 'fg': 'white', 'insertbackground': 'white', 'bd': 1}
button_style = {'font': ('Helvetica', 12), 'width': 15, 'bg': '#007acc', 'fg': 'white', 'activebackground': '#005999', 'bd': 0}
result_style = {'font': ('Helvetica', 12), 'fg': '#cccccc', 'bg': '#1e1e2e'}

# Create GUI components
title_label = tk.Label(root, text="Welcome to the Guessing Game!", font=("Helvetica", 16, "bold"), bg="#1e1e2e", fg="#00e676", pady=15)
title_label.pack()

instruction_label = tk.Label(root, text="Guess a number between 1 and 100:", **label_style)
instruction_label.pack()

entry_guess = tk.Entry(root, **entry_style)
entry_guess.pack(pady=10)

guess_button = tk.Button(root, text="Submit Guess", **button_style, command=check_guess)
guess_button.pack(pady=10)

reset_button = tk.Button(root, text="Reset Game", **button_style, command=reset_game)
reset_button.pack(pady=5)

result_label = tk.Label(root, text="Guess a number between 1 and 100", **result_style)
result_label.pack(pady=10)

# Hover effects for buttons
def on_enter(e):
    e.widget.config(bg="#005999")

def on_leave(e):
    e.widget.config(bg="#007acc")

guess_button.bind("<Enter>", on_enter)
guess_button.bind("<Leave>", on_leave)
reset_button.bind("<Enter>", on_enter)
reset_button.bind("<Leave>", on_leave)

# Start the Tkinter event loop
root.mainloop()
