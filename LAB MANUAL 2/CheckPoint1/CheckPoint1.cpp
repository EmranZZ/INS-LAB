#include <iostream>
#include <string>
using namespace std;

string decryptCaesar(string text, int shift) {
    string result = "";

    for (char c : text) {
        if (islower(c)) {
            char decrypted = ((c - 'a' - shift + 26) % 26) + 'a';
            result += decrypted;
        } else {
            result += c;
        }
    }
    return result;
}

int main() {

    string cipher = "odroboewscdrolocdcwkbdmyxdbkmdzvkdpybwyeddrobo";

    cout << "Trying all 25 possible shifts:\n\n";

    for (int shift = 1; shift < 26; shift++) {
        cout << "Shift " << shift << " : ";
        cout << decryptCaesar(cipher, shift) << endl;
    }

    return 0;
}
