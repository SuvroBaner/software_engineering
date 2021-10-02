#include <iostream>

using namespace std;

int main() {
    // stores B in a character variable 
    char character = 'B';
    int character_int = (int) character;
    cout << "Given Character = " << character << endl;
    cout << "Character ASCII = " << character_int << endl;

    // initialize another variable character_before
    char character_before;
    character_before = character - 1;
    int character_before_int = (int) character_before;

    cout << "Character before = " << character_before << endl;
    cout << "Character before ASCII =  " << character_before_int;

    return 0;
}