#include <iostream>
#include <fstream>
#include <map>
#include <vector>
#include <algorithm>
using namespace std;

string readFile(string filename) {
    ifstream file(filename);
    string content((istreambuf_iterator<char>(file)),
                    istreambuf_iterator<char>());
    return content;
}

void frequencyAnalysis(string text) {
    map<char, int> freq;

    for (char c : text) {
        if (isalpha(c)) {
            c = tolower(c);
            freq[c]++;
        }
    }

    vector<pair<char, int>> sortedFreq(freq.begin(), freq.end());

    sort(sortedFreq.begin(), sortedFreq.end(),
         [](pair<char,int> a, pair<char,int> b) {
             return a.second > b.second;
         });

    cout << "\nLetter Frequency (Most Frequent First):\n\n";

    for (auto p : sortedFreq) {
        cout << p.first << " : " << p.second << endl;
    }
}

int main() {

    cout << "1. Analyze Cipher 1\n";
    cout << "2. Analyze Cipher 2\n";

    int choice;
    cin >> choice;

    if (choice == 1) {
        string cipher1 = readFile("cipher1.txt");
        frequencyAnalysis(cipher1);
    }
    else if (choice == 2) {
        string cipher2 = readFile("cipher2.txt");
        frequencyAnalysis(cipher2);
    }

    return 0;
}
