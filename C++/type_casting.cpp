#include <iostream>

using namespace std;

int main() {
    char character = 'A'; // initializing a variable of char data type
    int ASCII; // declares a variable of int type
    // converts the char data type into int explicitly
    ASCII = (int) character;
    cout << "ASCII value = " << ASCII << endl; // prints the ASCII value of the variable

    int number = 90;
    char character2 = number;
    cout << "character2 = " << character2 << endl;

    string text = "hey this is a string 12 yes ..."; // always with double quote
    // Strings are not allocated a fixed amount of memory during the time of declaration.
    cout << "text = " << text << endl;

    cout << "Please enter a number: " << endl;\
    float num;
    cin >> num;
    cout << "The number you have enterted is " << num;
}