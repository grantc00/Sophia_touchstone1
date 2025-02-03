# Import libraries
import random

def play_game():
    choices = ['rock', 'paper', 'scissors']
    user_wins = 0
    computer_wins = 0
    ties = 0

    while True:
        # Ask user for input
        user_choice = input("Enter Rock, Paper, or Scissors (or 'quit' to stop): ").lower()

        # Check for exit condition
        if user_choice == 'quit':
            break

        # Check input
        if user_choice not in choices:
            print("Invalid choice, try again.")
            continue

        # Computer makes a random choice
        computer_choice = random.choice(choices)
        print(f"Computer chose {computer_choice}")

        # The result
        if user_choice == computer_choice:
            print("It's a tie!")
            ties += 1
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'scissors' and computer_choice == 'paper') or \
             (user_choice == 'paper' and computer_choice == 'rock'):
            print("You win!")
            user_wins += 1
        else:
            print("Computer wins!")
            computer_wins += 1

    print("Game over! Final score:")
    print(f"Wins: {user_wins}, Losses: {computer_wins}, Ties: {ties}")

# Run the game
play_game()
