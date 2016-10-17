// AUTHOR: Jackson Hsu jaxhsu@bu.edu



#include <iostream>
#include <iomanip>
#include <cmath>
#include <fstream>
#include <string>
using namespace std;



int binary_to_decimal(string n)
{
	int NumLen = n.length();
	int bin = stoi(n);
	int rem, dec = 0;
	int base = 2;

	if (NumLen > 32){
		return 0;
	}

	else{
		while (bin > 0)
		{
			rem = bin % 10;
			dec = dec + rem * base;
			base = base * 2;
			bin = bin / 10;
		}
		return dec/2;
	}
}

int binary_sum(string fileName)
{
	int sum = 0;
	string line;
	ifstream file;
	file.open(fileName);


	while (!file.eof()){
		getline(file, line);
		sum = sum + binary_to_decimal(line);
	}
	
	return sum;
}

int main()
{
	int a;
	int fin = 0;
	fin = binary_sum("file.txt");

	cout << fin;
	cin >> a;
}