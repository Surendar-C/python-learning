import random

computer_choice = random.choice(["scissors", "rock", "paper"])

user_choice = input("What\'s your choice - rock, paper (or) scissors?\n")

print("Computer's choice is \n" + computer_choice)

if user_choice == computer_choice :
    print("TIE")
elif user_choice =="rock" and computer_choice == "scissors":
    print("Win")
elif user_choice == "paper" and computer_choice == "rock":
    print("Win")
elif user_choice =="scissors" and computer_choice =="paper":
    print("Win")
else:
    print("You lose :( Computer Wins :)")