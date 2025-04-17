import random

options = ("rock", "paper", "scissors")
running = True

while running:
    player = None
    comp = random.choice(options)

    while player not in options:
        player = input("Enter a choice(rock,paper,scissors):")

    print(f"Player:{player}")
    print(f"Computer:{comp}")

    if player == comp:
        print("It's a tie. No one won...")
    elif player == "rock" and comp == "scissors":
        print("Congratulations!!!You won")
    elif player == "paper" and comp == "rock":
        print("Congratulations!!!You won")
    elif player == "scissors" and comp == "paper":
        print("Congratulations!!!You won")
    else:
        print("Oh no... You lost")
    
    if not input("Play again? (y/n):").lower() == "y":
        print("Thanks for playing?!")
