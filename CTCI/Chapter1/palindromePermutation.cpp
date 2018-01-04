#include <iostream>
#include <string>

using namespace std;

// Questions: What is a palindrome? Case sensitive? Spaces? alphanumeric? ASCII?

int vectorDrome(string str) {
  long long checker = 0;
  for (int i = 0; i < str.length(); i++) {
    if ((str[i] >= 65 && str[i] <= 90) || (str[i] >= 97 && str[i] <= 122)) {
      checker = checker ^ (1<< ((str[i] - 'a')%32));
      cout << "checker " << checker << endl;
    }
  }
  if (checker == 0 || (checker & checker-1) == 0) {
    return true;
  } else {
    return false;
  }
}


int palindromer(string str) {
  // Assume ASCII
  int letters[128] = {0};
  for (int i = 0; i < str.length(); i++) {
    if (str[i] >= 65 && str[i] <= 90) {
      letters[str[i]+32]++;
    } else if (str[i] >= 97 && str[i] <= 122) {
      letters[str[i]]++;
    }
  }
  int oddCount = 0;
  for (int i = 0; i < 128;i++) {
    if (letters[i]%2 ==1) {
      oddCount++;
      cout << "letter: " << i << "\n" << endl;
      if (oddCount >=2) {
        return false;
        break;
      }
    }
  }
  return true;
}

int main() {
  cout << vectorDrome("Tact Coa") << endl;
  return 1;
}
