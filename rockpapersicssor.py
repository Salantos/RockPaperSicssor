import random

while True:
    user_action = input("Enter a choice (Rock, Paper or Scissors): ").lower().capitalize()
    possible_actions = ["Rock", "Paper", "Scissors"]
    computer_actions = random.choice(possible_actions)

    print(f"\nYou chose {user_action}.\nComputer chose {computer_actions}.\n")

    if user_action == computer_actions:
        print(f"Both players selected: {user_action}. It's a tie!")
    elif user_action == "Rock":
        if computer_actions == "Scissors":
            print("Rock smashes Scissors! You win")
        else:
            print("Paper covers Rock! You lose.")
    elif user_action == "Paper":
        if computer_actions == "Rock":
            print("Paper covers Rock! You win.")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action == "Scissors":
        if computer_actions == "Paper":
            print("Scissors cuts paper! You win.")
        else:
            print("Rock smashes Scissors! You lose.")

    play_again = input("Would you like to play again? (y/n): ").lower()
    if play_again in ["yes", "y"]:
        continue
    elif play_again in ["no", "n"]:
        print("Thanks for playing! Goodbye.")
        break