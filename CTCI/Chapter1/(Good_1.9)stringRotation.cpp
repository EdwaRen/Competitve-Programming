#include <iostream>
#include <sstream>

using namespace std;


int substring(string str1, string str2) {
  if (str1.length() != 0 && (str1.length() == str2.length())) {
    stringstream ss;
    ss<< str1 << str1;
    if (ss.str().find(str2) != string::npos) {
      return true;
    } else {
      return false;
    }

    // return isSubstring(ss.str(), str2);
  }
  return false;
}

int main() {
  cout << substring("waterbottle", "erbottlewat") << endl;
}
