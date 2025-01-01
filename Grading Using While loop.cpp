// Grading system using while loop

#include <iostream>

using namespace std ;

int main ( ) {
	
	int i = 0 ;
	
	cout << " Welcome to Lexan Grading System using Loops \n " ;
	
	
	while ( i < 20 ) {
		
		int num ;
	cout << " Enter your Marks \n " ;
	cin >> num ;
	
	if ( num >= 75 and num <=100 ) {
		
		cout << " Your Grade is : A \n " ;
	}
	
	else if ( num >= 65 and num < 75) {
		
		cout << " Your Grade is : B \n " ;
	}
	
	else if ( num >= 45 and num < 65 ) {
		
		cout << " Your Grade is : C \n " ;
		
	}
	
	else if ( num >=30 and num < 45 ) {
		
		cout << " Your Grade is : D \n " ;
	}
	
	else if ( num >= 0 and num < 30 ) {
		
		cout << " Your Grade is : F \n " ;
		
	}
	
	
	else {
		
		cout << " Please input correct marks \n " ;
	}
		
		
		i++ ;
	}
	
	return 0 ;
}
