#include <iostream>

using namespace std;

int main() {
    // initialize operand1 amd operand2
    int operand1 = 50; // you can declare them as float as well
    int operand2 = 26;

    // print the values of operand1 and operand2
    cout << "Values of Operands are : " << endl;
    cout << "operand1 = " << operand1 << ", operand2 = " << operand2 << endl;

    // adds operand1 and operand2
    cout << "Addition = " << operand1 + operand2 << endl;

    // subtracts operand1 and operand2
    cout << "Subtraction = " << operand1 - operand2 << endl;

    // multiplication of operand1 and operand2
    cout << "Multiplication = " << operand1 * operand2 << endl;

    // Division of operand1 and operand2
    cout << "Division = " << operand1 / operand2 << endl;

    // Returns remainder of operand1 and operand2
    cout << "Modulus = " << operand1 % operand2 << endl;

    return 0;
}