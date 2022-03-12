import random
player = input("Enter a choice (rock, paper, scissors): ")
actions = ["rock", "paper", "scissors"]
computer = random.choice(actions)
print(f"\nYou chose {player}, computer chose {computer}.\n")

if player == computer:
    print(f"Both players selected {player}. It's a tie!")
elif player == "rock":
    if computer== "scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif player == "paper":
    if computer == "rock":
        print("Paper will cover rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif player == "scissors":
    if computer == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
  
