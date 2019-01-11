#include <iostream>
#include <string>

using namespace std;

int main() {
  string a;
  cin >> a;
  int longestPalin = 0;
  for (int i = 0; i < a.length(); i++) {
      for (int j = 0; j < a.length(); j++) {
        int palin = 0;
        if (j-i >= 0 && i+j < a.length()) {
          palin++;
          if (palin > longestPalin) {
            longestPalin = palin;
          }
        }
      }
  }
}
