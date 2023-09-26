import sys
import random
import argparse
def Welcome(name):
    msg = f"{name}"
    print("Welcome to the game,",msg)
    
if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="Provides a personal greeting"
    )
    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )
    args = parser.parse_args()
    Welcome(args.name) 


    i = 0
    computer_score = 0
    player_score = 0
    while i == 0:
        computer_choice = random.randrange(1,3)
        player_choice = int(input("Enter your choice: "))
        if computer_choice == player_choice:
            print("Congratulation! You win")
            player_score += 1
            print("Your score: ",player_score)
            print("Computer's Score: ",computer_score)
            choice = input("Do you want to play again? \n")
            if choice == 'N' :
                break
            elif choice == 'Y' :
                continue
            else:
                choice = input("Sorry, please choose again! \n")
        else:
            print("Opps! You lose")
            computer_score += 1
            print("Your score: ",player_score)
            print("Computer's score: ",computer_score)
            choice = input("Do you want to play again?\n")
            if choice == 'N':
                break
            elif choice == 'Y':
               continue

    print("Thanks for playing the game")             
