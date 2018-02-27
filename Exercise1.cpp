#include <iostream>

using namespace std;

int main() {
	
	int average;
	
	cout << "Please enter your high school average: ";
	cin >> average; 
	
	if (average < 95 )
		cout << "LOL no dinner for you";
	
	else 
		cout << "WOW! Good job, we invite you to our award dinner";
	
	return 0;
}