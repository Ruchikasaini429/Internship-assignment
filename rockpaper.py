# Rock, Paper, Scissors Game - 5 Rounds

import random

def play_game():

    choices = ["rock", "paper", "scissors"]

    user_score = 0
    computer_score = 0

    # Loop runs 5 times
    for round in range(1, 6):

        print(f"\n--- Round {round} ---")

        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        # Check valid input
        if user_choice not in choices:
            print("Invalid choice! Round skipped.")
            continue

        # Computer choice
        computer_choice = random.choice(choices)

        print(f"Computer chose: {computer_choice}")

        # Check result
        if user_choice == computer_choice:
            print("It's a tie!")

        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):

            print("You win this round!")
            user_score += 1

        else:
            print("Computer wins this round!")
            computer_score += 1

    # Final Scores
    print("\n----- Final Score -----")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    # Final Winner
    if user_score > computer_score:
        print("Congratulations! You are the overall winner!")

    elif computer_score > user_score:
        print("Computer is the overall winner!")

    else:
        print("The game is a tie!")

# Function Call
play_game()