import random

# Function for test_game.py
def is_valid_choice(choice):
    return choice.lower() in ['rock', 'paper', 'scissors']

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

# Function to determine the winner
def determine_winner(player_choice, computer_choice):
    print(f"\nYou chose: {player_choice}")
    print(f"Computer chose: {computer_choice}")

    if player_choice == computer_choice:
        print("\nIt's a tie!")
    elif (player_choice == 'Rock' and computer_choice == 'Scissors') or \
         (player_choice == 'Paper' and computer_choice == 'Rock') or \
         (player_choice == 'Scissors' and computer_choice == 'Paper'):
        print("\nCongratulations! You win!")
    else:
        print("\nSorry, Computer wins this time!")

def main():
    print("=========================================")
    print("            Rock, Paper, Scissors")
    print("=========================================")
    print("Enter your choice:")
    print("  Rock")
    print("  Paper")
    print("  Scissors")
    print("=========================================")

    # Get player input
    player_choice = input("Your choice: ").capitalize()

    # Validate input
    if player_choice not in ['Rock', 'Paper', 'Scissors']:
        print("\nInvalid choice. Please enter Rock, Paper, or Scissors.")
        return

    computer_choice = get_computer_choice()
    
    determine_winner(player_choice, computer_choice)

if __name__ == "__main__":
    main()
