import random
 
print("\n\nWinning Rules of the Rock paper scissor game as follows: \n"
                                +"Rock vs paper->paper wins \n"
                                + "Rock vs scissor->Rock wins \n"
                                +"paper vs scissor->scissor wins \n")
 
while True:
    choice = input("Enter a choice (\n--> rock\n--> paper\n--> scissors): \n")
    possible_actions = ["rock", "paper", "scissors"]
    choice = choice.lower()
    if choice != "rock" and choice != "paper" and choice != "Scissor":
        print("Please choose a correct answer ")
        continue
    
    comp_choice = random.choice(possible_actions)
    print(f"\n\nYou chose {choice}, \n\ncomputer chose {comp_choice}.\n")
       
    
    if choice == comp_choice:
          print(f"Both players selected {choice} ")
          print("It's a tie")
    elif choice == "rock":
           if comp_choice == "scissors":
             print("Rock smashes scissors! You win!")
           else:
            print("Paper covers rock! You lose.")

    elif choice == "paper":
        if comp_choice == "rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif choice == "scissors":
        if comp_choice == "paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break