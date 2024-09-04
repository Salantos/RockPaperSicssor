import random

user_action = input("Enter a choice (Rock, Papper or Scissor): ")
possible_actions = ["Rock", "Paper", "Sicssor"]
computer_actions = random.choice(possible_actions)

print(f"\nYou chose {user_action}\nComputer chose {computer_actions}.\n")

if user_action == computer_actions:
    print(f"Both players selected: {user_action}. It's a tie!")
elif user_action == "Rock":
    if computer_actions == "Sicssor":
        print("Rock smashes Sicssor! You win")
    else:
        print("Paper covers Rock! You lose.")
elif user_action == "Paper":
    if computer_actions == "Rock":
        print("Paper covers Rock! You win.")
    else:
        print("Sicssor cuts paper! You lose.")
elif user_action == "Sicssor":
    if computer_actions == "Paper":
        print("Sicssor cuts paper! You win.")
    else:
        print("Rock smashes Sicssor! You lose.")