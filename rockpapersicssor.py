import random

possible_actions = ["Rock", "Paper", "Scissors"]

def create_player():
    player_name = input("Enter your name: ")
    return player_name

def get_user_selection():
    while True:
        user_action = input("Enter a choice (Rock, Paper or Scissors):\n").lower().capitalize()
        if user_action in possible_actions:
            return user_action
        else:
            print(f"{user_action} is not a valid option. You can chose between Rock, Paper or Scissors.")

def get_computer_selection():
    return random.choice(possible_actions)


def determine_winner(user_action, computer_action):
    if user_action == computer_action:
        return(f"Both players selected: {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_action == "Scissors":
            return("Rock smashes Scissors! You win")
        else:
            return("Paper covers Rock! You lose.")
    elif user_action == "Paper":
        if computer_action == "Rock":
            return("Paper covers Rock! You win.")
        else:
            return("Scissors cuts paper! You lose.")
    elif user_action == "Scissors":
        if computer_action == "Paper":
            return("Scissors cuts paper! You win.")
        else:
            return("Rock smashes Scissors! You lose.")

def play_again():
    while True:
            play_again_input = input("Would you like to play again? (y/n): ").lower()
            if play_again_input in ["yes", "y"]:
                return True
            elif play_again_input in ["no", "n"]:
                return False
            else:
                print("Please enter 'yes', 'y' or 'no', 'n'")



def main_game(player_name):
    while True:
        user_action = get_user_selection()
        computer_action = get_computer_selection()

        print(f"\nYou chose {user_action}.\nComputer chose {computer_action}.\n")

        result = determine_winner(user_action, computer_action)
        print(result)

        if not play_again():
            print(f"Thanks for playing {player_name}! Goodbye.\n")
            break

def menu():
    while True:
        print("Welcome to a game of Rock, Paper, Sicssor!\n1. Start game\n2. End game")
        
        choice = input("Select your option between 1 and 2.\n")

        if choice == "1":
            player_name = create_player()
            main_game(player_name)
        elif choice == "2":
            print("Thanks for playing! Exiting game.")
            exit()
        else:
            print("Invalid choice. Please select either 1 or 2.")

menu()