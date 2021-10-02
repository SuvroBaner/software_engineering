#include <iostream>

using namespace std;

int main() {
    int integer = 2147483649; // The maximum value that can be stored in a variable of type int is 2147483647 for both pos and neg  i.e. 4 bytes
    long int long_integer = 2147483649; // it increases the memory allocation by 4 more bytes

    int integer2 = 32768;
    short int short_integer = 32768; // short reserves 2 bytes of memeory i.e. 2^16 split across both pos and neg i.e. max short can hold is 32767

    int integer3 = -10;
    unsigned int unsigned_integer = 4294967295; // only stores non-negative values i.e. unsigned

    char character = 'A';
    unsigned char unsigned_character = 'B';
    signed char signed_character = 'C';

    cout << "integer = " << integer << endl;
    cout << "long_integer = " << long_integer << endl;
    cout << "integer2 = " << integer2 << endl;
    cout << "short_integer = " << short_integer << endl;
    cout << "integer3 = " << integer3 << endl;
    cout << "unsigned_integer = " << unsigned_integer << endl;
    cout << "character = " << character << endl;
    cout << "unsigned_character = " << unsigned_character << endl;
    cout << "signed_character = " << signed_character << endl;
    
}