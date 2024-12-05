# This is a simple python calculator program to do simple calculations

# This project was started at 13:36 pm on 5 December 2024 ...

print( "Welcome to Lexan Simple Calculator  \n ")

number1 = float( input( " Enter the First Number : ") )

operation = int ( input ( " Enter the Number of the operation that you want to perform :  \n 1.+ \n 2.- \n 3.* \n 4./ \n  "))

number2 =float ( input ( " Enter the Second Number :  "))

if operation == 1 :
    addition = number1 + number2
    print( f" The Addition of Your Numbers is {addition} ")

elif operation == 2 :
    substraction = number1 - number1
    print( f" The Substraction of your Numbers is {substraction} " )

elif operation == 3 :
    multiplication = number1 * number2
    print( f"The Multiplication of your Numbers is {multiplication}")

elif operation == 4 :
    if number2 == 0 :
        print( " Division By Zero Error ")

    else :
        division = number1 / number2
        print( f" The Division of your Numbers is {division} ")

else :
    print( " Please Enter carefully the Number of the operation that you want to perform above ")

# print( f"The Number you entered are {number1} and {number2} and the operation is {operation} ")
# The above comment was just for knowing if the variables are working just fine