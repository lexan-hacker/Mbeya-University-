#include <iostream>

// This project was created on 5 December 2024 and it was such an amazing way to remember the past memories of this language 
// Learning Cpp language is dedicated to Ibrahim Mavika who helped me 
// I remembered it very easily ... By Lexan-hacker ...
// I don't know why ... but why is this font so good ... Logged out of here at 14:56 pm 

int main ( ) {
	
	std::cout << " Welcome to Lexan Even or Odd Number Checker \n " ;
	
	int number ;
	std::cout << " \n Enter the number you want to know if it is odd or even : \n " ;
	std::cin >> number ;
	
	if ( number % 2 == 0 ) {
		
		std::cout << " The Number you entered is Even Number \n " ;
	}
	
	else if ( number % 2 != 0 ) {
		
		std::cout << " The Number you entered is Odd Number \n " ;
	}
	
	else {
		
		std::cout << " Please enter a number above \n " ;
		
	}
	
	
	return 0 ;
}