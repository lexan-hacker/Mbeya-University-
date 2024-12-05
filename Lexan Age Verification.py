# Just around 11:45 am on 5 December 2024 was this file casually created by lexan-hacker
# A simple age verification program ...

print(" Welcome to A Simple Lexan Age Verification Using Python Language ")

name = input( " Enter your Name : ")

age = int( input ( " Please enter your age : ") ) #the int specifies that the variable accepts integer values only

if 18 > age > 0:
    print( " You are still young to use this platform \n " )
    print ( " You Must be 18 years and above ")

elif 100 > age > 18 :
    print( " You have passed the age verification and can continue using the platform \n ")

else :
    print (" Please enter the correct age from 1 to 100 ")

# print( f" Your Name is {name} and your age is {age}" )   This was for initially checking if my variables run correctly

# print( " Congratulations , there was no any errors in the program ")        #This is for checking if there is no any problems with the program and
                                                                              #if it finishes correctly