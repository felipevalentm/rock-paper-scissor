import random 
import re

while True:

    print("Welcome to the game")
    user_option = input("Insert your option (R)ock, (P)aper, (S)cissors, (E)xit: ")  

    if (not re.match ("[SPRE]", user_option)) or len(user_option) != 1:
        print ("Please choose a letter!")
        print ("[R]ock, [S]cissors, [P]aper or [E]xit")
        continue
    
    print(f"Your option: {user_option}")
    
    if user_option == "E" or user_option == "e":
        print("Exiting")
        break

    options = ['R', 'S', 'P']

    opponent = random.choice(options)
    print(f"Oponnent's option: {opponent}")
          
    if opponent == user_option:
        print("Tie!")
    elif opponent == 'P' and user_option == 'R':
        print("Opponent Wins!")
    elif opponent == 'S' and user_option == 'P':
        print("Opponent Wins")
    elif opponent == 'R' and user_option == 'S':
        print("Opponent Wins")
    else:
        print("You win!")
        break