// checking the validity of a number 

#include<stdio.h>

int main () {
	
	printf( "Checking whether a number is negative or positive \n ") ;
	
	int number ;
	printf ( " Please enter a number : \n ") ;
	
	scanf ( "%d" , &number ) ;
	if ( number > 0 ) {
		
		printf ( " Your number %d is a positive number " , number ) ;
		
	}
	
	else if ( number == 0 ) {
		
		printf ( " The number %d you entered is zero and neither a negative or positive number " , number ) ;
	}
	
	else {
		
		printf ( " Your number %d is a negative number " , number ) ;
	}
	
	
	
	return 0;
}