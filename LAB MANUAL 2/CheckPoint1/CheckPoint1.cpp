#include <iostream>
#include <string>
using namespace std;

// Decrypt with a given shift
string decrypt(string text, int shift) {
    string result = "";
    for (char c : text) {
        if (c >= 'a' && c <= 'z') { // only lowercase letters
            result += char((c - 'a' - shift + 26) % 26 + 'a');
        } else {
            result += c; // keep other characters unchanged
        }
    }
    return result;
}

int main() {
    string cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo";

    // Try all possible shifts
    for (int shift = 0; shift < 26; shift++) {
        cout << "Shift " << shift << ": " << decrypt(cipher, shift) << endl;
    }

    return 0;
}

//For Finding Patter, Looked into Shift 10: ethereumisthebestsmartcontractplatformoutthere
//ie "ethereum is the best smart contract platform out there"
