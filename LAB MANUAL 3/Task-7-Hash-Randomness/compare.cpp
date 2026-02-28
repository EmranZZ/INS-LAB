#include <iostream>
#include <string>
using namespace std;

// Convert hex char to binary string
string hexToBinary(char c) {
    switch(toupper(c)) {
        case '0': return "0000";
        case '1': return "0001";
        case '2': return "0010";
        case '3': return "0011";
        case '4': return "0100";
        case '5': return "0101";
        case '6': return "0110";
        case '7': return "0111";
        case '8': return "1000";
        case '9': return "1001";
        case 'A': return "1010";
        case 'B': return "1011";
        case 'C': return "1100";
        case 'D': return "1101";
        case 'E': return "1110";
        case 'F': return "1111";
    }
    return "";
}

int main() {
    string hash1, hash2;
    cout << "Enter Hash 1 (without spaces): ";
    cin >> hash1;
    cout << "Enter Hash 2 (without spaces): ";
    cin >> hash2;

    string bin1="", bin2="";
    for(char c: hash1) bin1 += hexToBinary(c);
    for(char c: hash2) bin2 += hexToBinary(c);

    int same = 0;
    for(int i=0; i<bin1.size(); i++) {
        if(bin1[i] == bin2[i]) same++;
    }

    cout << "Total bits: " << bin1.size() << endl;
    cout << "Same bits: " << same << endl;
    cout << "Different bits: " << bin1.size() - same << endl;

    return 0;
}
