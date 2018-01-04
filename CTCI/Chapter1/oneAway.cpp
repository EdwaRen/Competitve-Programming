#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int oneAway(string str1, string str2) {
  if (str1.length() < str2.length()) {
    string temp = str1;
    str1 = str2;
    str2 = temp;
  }

  unordered_map<int, int> myMap;

  for (int i = 0; i < str1.length(); i++) {
    myMap[str1[i]]++;
  }
  for (int i = 0; i < str2.length(); i++) {
    myMap[str2[i]]--;
  }
  int count = 0;
  for (int i = 0; i < str1.length(); i++) {
    if (myMap[str1[i]] != 0) {
      count++;
      if (count > 1) {
        return false;
      }
    }
  }
  return true;
}

int main() {
  cout << oneAway("pale", "bale") << endl;

}
