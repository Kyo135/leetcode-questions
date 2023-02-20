#include<iostream>
using namespace std;

void match(char s1, char s2) {
    int m = s1.length();
    int n = s2.length();
    for (int i = 0; i < m - n; i++) {
        for (int j = 0; j < n; j++) {
            if (s1[i + j]!=s2[j]) {
                break;
            }
        }
        if (j == m) {
            cout << i << endl;
            return;
        }
    }

}

int main() {
    char s1 = "abab";
    char s2 = "ab";
    match(s1, s2);
    return 0;
}