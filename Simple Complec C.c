// Input and out put operations 

#include<stdio.h>

int main () {
	
	int age ;   // This is the declaration of age so that a user may be able to enter his or her age 
	
	int thinking ;
	
	printf ( " Welcome to my simple Lexan program \n ") ;
	
	printf ( " May you Please enter your age for verification \n ") ;   // prompting a user to enter an inout which was then stored in a variable 
	
	scanf ( "%d" , &age ) ;        // this is how we get a user inout 
	
	printf ( " Is your age %d " , age ) ;
	
	// printf( " Welcome to Lexan and this is the main program ") ;
	
	return 0;
}