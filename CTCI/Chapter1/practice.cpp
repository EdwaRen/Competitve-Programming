#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int oneAway(string s1, string s2) {
  unordered_map<int, int> myMap;

  if (s1.length() < s2.length()) {
    string temp;
    temp = s1;
    s1 = s2;
    s2 = temp;
  }

  for (int i = 0; i < s1.length(); i++) {
    myMap[s1[i]]++;
  }

  for (int i = 0; i < s2.length(); i++) {
    myMap[s2[i]]--;
  }

  int count = 0;
  for (int i = 0; i < s1.length(); i++) {
    if (myMap[s1[i]] != 0) {
      count++;
    }
    if (count > 1) {
      return false;
    }
  }
  return true;

}


int main() {
  cout << "result: " << oneAway("Hello", "Hell") << endl;
}
