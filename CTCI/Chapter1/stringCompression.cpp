#include <iostream>
#include <string>
#include <sstream>

using namespace std;

string compress(string str) {
  stringstream ss;
  int count = 1;
  for (int i = 0; i < str.length(); i++) {
    if (str[i] != str[i+1]) {
      ss<<str[i]<<count;
      count = 0;
    }
    count++;
  }
  if (ss.str().length() > str.length()) {
    return str;
  } else {
    return ss.str();
  }
}

int main() {
  cout << compress("abcdefgh") << endl;
}
