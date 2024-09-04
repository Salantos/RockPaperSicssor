import random

user_action = input("Enter a choice (Rock, Papper or Scissor): ")
possible_actions = ["Rock", "Paper", "Sicssor"]
computer_actions = random.choice(possible_actions)

print(f"\nYou chose {user_action}\nComputer chose {computer_actions}.\n")

if user_action == computer_actions:
    print(f"Both players selected: {user_action}. It's a tie!")
