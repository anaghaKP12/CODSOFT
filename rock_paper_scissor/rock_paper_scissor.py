import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# Function to get computer's choice
def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return "You win!"
    else:
        return "You lose!"

# Function to handle animations
def animate_result(result):
    if result == "You win!":
        for _ in range(2):
            result_label.config(fg="green")
            window.update()
            window.after(150)
            result_label.config(fg="black")
            window.update()
            window.after(150)
    elif result == "You lose!":
        for _ in range(2):
            result_label.config(fg="red")
            window.update()
            window.after(150)
            result_label.config(fg="black")
            window.update()
            window.after(150)
    else:
        result_label.config(fg="orange")

# Function to handle user choice and update the game
def play_round(user_choice):
    computer_choice = get_computer_choice()

    result = determine_winner(user_choice, computer_choice)

    # Update labels with choices and result
    user_choice_label.config(image=image_dict[user_choice], text=user_choice.capitalize(), compound="top")
    computer_choice_label.config(image=image_dict[computer_choice], text=computer_choice.capitalize(), compound="top")
    result_label.config(text=result, font=("Arial", 16))

    # Animate result
    animate_result(result)

    # Update scores
    global user_score, computer_score
    if result == "You win!":
        user_score += 1
    elif result == "You lose!":
        computer_score += 1

    # Update score labels
    user_score_label.config(text=f"Your Score: {user_score}")
    computer_score_label.config(text=f"Computer's Score: {computer_score}")

    # Ask if the user wants to play again
    # play_again = messagebox.askyesno("Play Again", "Do you want to play another round?")
    # if not play_again:
    #     window.quit()

# Function to handle score reset
def reset_scores():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    user_score_label.config(text="Your Score: 0")
    computer_score_label.config(text="Computer's Score: 0")
    result_label.config(text="", fg="black")
    user_choice_label.config(image="", text="")
    computer_choice_label.config(image="", text="")

# Function to handle quit button
def quit_game():
    window.quit()

# Initialize the scores
user_score = 0
computer_score = 0

# Create the main window
window = tk.Tk()
window.title("Rock-Paper-Scissors with Images & Animation")
window.geometry("500x500")
window.config(bg="#f0f8ff")

# Load images for rock, paper, and scissors
rock_img = ImageTk.PhotoImage(Image.open("rock.png").resize((100, 100)))
paper_img = ImageTk.PhotoImage(Image.open("paper.png").resize((100, 100)))
scissors_img = ImageTk.PhotoImage(Image.open("scissor.jpg").resize((100, 100)))

# Dictionary to map choices to images
image_dict = {
    "rock": rock_img,
    "paper": paper_img,
    "scissors": scissors_img
}

# Instructions label
instructions_label = tk.Label(window, text="Choose Rock, Paper, or Scissors", font=("Arial", 16), bg="#e6f7ff")
instructions_label.pack(pady=15)

# Labels for user and computer choices
user_choice_label = tk.Label(window, text="", bg="#f0f8ff", font=("Arial", 14))
user_choice_label.pack(pady=5)
computer_choice_label = tk.Label(window, text="", bg="#f0f8ff", font=("Arial", 14))
computer_choice_label.pack(pady=5)

# Label to show the result
result_label = tk.Label(window, text="", font=("Arial", 18, "bold"), bg="#f0f8ff")
result_label.pack(pady=10)

# Score labels
user_score_label = tk.Label(window, text="Your Score: 0", font=("Arial", 14), bg="#d9f0ff")
user_score_label.pack(pady=5)
computer_score_label = tk.Label(window, text="Computer's Score: 0", font=("Arial", 14), bg="#d9f0ff")
computer_score_label.pack(pady=5)

# Buttons for Rock, Paper, and Scissors with images
button_frame = tk.Frame(window, bg="#f0f8ff")
button_frame.pack(pady=15)

rock_button = tk.Button(button_frame, image=rock_img, bg="#b3d9ff", command=lambda: play_round("rock"))
rock_button.grid(row=0, column=0, padx=10)

paper_button = tk.Button(button_frame, image=paper_img, bg="#b3d9ff", command=lambda: play_round("paper"))
paper_button.grid(row=0, column=1, padx=10)

scissors_button = tk.Button(button_frame, image=scissors_img, bg="#b3d9ff", command=lambda: play_round("scissors"))
scissors_button.grid(row=0, column=2, padx=10)

# Reset score button with background color
reset_button = tk.Button(window, text="Reset Scores", width=15, font=("Arial", 12), bg="#ffd966", command=reset_scores)
reset_button.pack(pady=10)

# Quit button with background color
quit_button = tk.Button(window, text="Quit", width=15, font=("Arial", 12), bg="#ff9999", command=quit_game)
quit_button.pack(pady=10)

# Run the application
window.mainloop()
