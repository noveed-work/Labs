# CODE ALONG - ROCK PAPER SCISSORS


import random

def play_round():
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    player_choice = input("Enter your choice (rock, paper or scissors)")
    print(f"computer chose {computer_choice}")
    if player_choice.lower() == computer_choice:
        return "tie"
    elif player_choice.lower() == "rock":
        if computer_choice == "scissors":
            return "user"
        else:
            return "computer"
    elif player_choice.lower() == "paper":
        if computer_choice == "rock":
            return "user"
        else:
            return "computer"
    elif player_choice.lower() == "scissors":
        if computer_choice == "paper":
            return "user"
        else:
            return "computer"
    else:
        print("Invalid choice, try again")
        return play_round()

num_rounds = 0
user_wins = 0
computer_wins = 0
play_again = "y"


while play_again.lower() == "y":
    num_rounds += 1
    result = play_round()
    if result == "user":
        user_wins += 1
        print("You win!")
    elif result == "computer":
        computer_wins += 1
        print("computer wins!")
    else:
        print("tie game")
    print(f"Rounds played: {num_rounds}")
    print(f"User wins: {user_wins}")
    print(f"Computer wins: {computer_wins}")
    play_again = input("Do you want to play again? y/n : ")