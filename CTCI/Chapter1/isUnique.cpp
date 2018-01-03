#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int bitVector(string str) {
  // Checker basically stores a history of all characters by using bitwise OR
  // 1<<val ensures that each character uses only a single 1 in a max 26 bit number
  // Basically a = 0000000...00001 -> 26 total 1 and 0s
  // b = 0000... 00010 etc until
  // z = 10000...000000 


  int checker = 0;
  for (int i = 0; i < str.length(); i++) {
    int val;
    val = str[i]-'a';
    if (checker & (1<<val) > 0) {
      return false;
    }
    checker |= 1<<val;
  }
  return true;
}

int isUnique(string str) {
  if (str.length() > 128) {
    return 0;
  }
  int chars[128] = {0};
  for (int i = 0; i < str.length(); i++) {
    if (chars[str[i]]) {
      return 0;
    } else {
      chars[str[i]] = 1;
    }
  }
  return 1;


}

int main() {
  cout << "usUnique: " << isUnique("Helo") << endl;



  return 1;
}
