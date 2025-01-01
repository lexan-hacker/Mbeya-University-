# Rock Paper Scissors 

import random 

print( " Welcome to Rock , Paper , Scissors Game \n ")

choice = float ( input ( " Input your choice \n 1. Rock \n 2. Paper \n 3. Scissors \n  "))

computer = range ( " Rock " , " Paper " , " Scissor ")

computer = str(computer)

if choice == 3 and computer == " Paper " :
    print( " You Loose ")

else : 
    print ( " The results were unexpected ")

