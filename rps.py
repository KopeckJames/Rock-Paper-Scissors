import random

print("Let's Play Rock Paper Scissors!")

option = ["r", "p", "s"]

while True:
    user_choice = input("Make your Choice: (r)rock, (p)aper, (s)cissors?")
    
    if user_choice.lower() in option:
        computer_choice = random.choice(option)
    
        if user_choice == 'r':
            user_full_choice = 'rock'
        elif user_choice == 'p':
            user_full_choice = 'paper'
        else:
            user_full_choice = 'scissors'

        if user_choice == computer_choice:
            print (f"you both chose {user_full_choice}")
            print("A smashing tie!")
        elif (user_choice == 'r' and computer_choice == 'p'):
            print("You chose rock. The computer chose paper.")
            print("Sorry. You lose.")
        elif (user_choice == 'r' and computer_choice == 's'):
            print("You chose rock. The computer chose scissors.")
            print("Yay! You won.")
        elif (user_choice == 'p' and computer_choice == 'r'):
            print("You chose paper. The computer chose rock.")
            print("Yay! You won.")
        elif (user_choice == 's' and computer_choice == 'p'):
            print("You chose scissors. The computer chose rock.")
            print("Sorry. You lose.")
        elif (user_choice == "p" and computer_choice == "s"):
            print("You chose paper. The computer chose scissors.")
            print("Sorry. You lose.")
        elif (user_choice == "s" and computer_choice == "r"):
            print("You chose scissors. The computer chose rock.")
            print("Sorry. You lose.")
    
    print("Would you like to play again?")
    play_again = input("Type (y) to continue or anything else to exit. ")

    if play_again.lower() != "y":
        break
    else:
        print("I don't understand that!")
        print("Next time, choose from 'r', 'p', or 's'.")
print("Thanks for playing!")

