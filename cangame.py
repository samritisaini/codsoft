import tkinter as tk
import random

def play_game():
    user_choice = user_choice_var.get().lower()
    
    if user_choice not in ['rock', 'paper', 'scissors']:
        result_var.set("Invalid choice. Please enter rock, paper, or scissors.")
        return
    
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    
    user_choice_label.config(text=f"Your choice:\n{get_ascii_art(user_choice)}")
    computer_choice_label.config(text=f"Computer's choice:\n{get_ascii_art(computer_choice)}")
    
    if user_choice == computer_choice:
        result_var.set("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        result_var.set("You win!")
    else:
        result_var.set("You lose!")

def get_ascii_art(choice):
    if choice == 'rock':
        return """
        _______
    ---'   ____)
          (_)
          (_)
          ()
    ---.(_)
     Rock
        """
    elif choice == 'paper':
        return """
         _______
    ---'    ___)___
               ______)
              _______)
             _______)
    ---.)
    Paper
        """
    elif choice == 'scissors':
        return """
        _______
    ---'   ___)___
              ______)
           __________)
          ()
    ---.(_)
    scissors
        """
    else:
        return "Invalid choice"

# Create Tkinter GUI
root = tk.Tk()
root.title("Rock, Paper, Scissors Game")

# User choice entry
user_choice_var = tk.StringVar()
user_choice_entry = tk.Entry(root, textvariable=user_choice_var, width=20)
user_choice_entry.grid(row=0, column=0, padx=10, pady=10)

# Play button
play_button = tk.Button(root, text="Play", command=play_game)
play_button.grid(row=0, column=1, padx=10, pady=10)

# Labels to display choices and result
user_choice_label = tk.Label(root, text="Your choice:", justify="left")
user_choice_label.grid(row=1, column=0, padx=10, pady=10)

computer_choice_label = tk.Label(root, text="Computer's choice:", justify="left")
computer_choice_label.grid(row=1, column=1, padx=10, pady=10)

result_var = tk.StringVar()
result_label = tk.Label(root, textvariable=result_var, font=("Arial", 14))
result_label.grid(row=2, columnspan=2, padx=10, pady=10)

root.mainloop()
