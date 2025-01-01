# Guess the Number While Loop

import random

i = 0

while i < 10 :

    num = float ( input ( " Enter your number :  "))

    x = random.randint(1,6)

    if num == x : 
        print ( " \n You Guessed the Correct Number : " , num , " = " , x , " \n " )

    else :
        print ( " \n You Guessed the wrong Number  ")
        print ( " The Correct Number was :  " , x )

    i = i + 1

saveterminal = float ( input ( " Enter any Number to Exit "))