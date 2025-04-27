import random

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

    while True:
        print("\nEnter your choice:")
        print("  Rock")
        print("  Paper")
        print("  Scissors")
        print("=========================================")

        # Get player input
        player_choice = input("Your choice: ").capitalize()

        # Validate input
        if player_choice not in ['Rock', 'Paper', 'Scissors']:
            print("\nInvalid choice. Please enter Rock, Paper, or Scissors.")
            continue  # 如果输入无效，重新开始本轮

        computer_choice = get_computer_choice()
        determine_winner(player_choice, computer_choice)

        # Ask if want to play again
        play_again = input("\nPlay again? (y/n): ").strip().lower()
        if play_again != 'y':
            print("\nThanks for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()
