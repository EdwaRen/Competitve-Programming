#include <iostream>


using namespace std;
// Questions: Is it case sensitive? is whitespace significant?
// Another possible way to do this is to sort the strings

int permutation(string str1, string str2) {
  if (str1.length() != str2.length()) {
    return false;
  }
  int letters[128] = {0};
  for (int i = 0; i < str1.length(); i++) {
    letters[str1[i]]++;
  }
  for (int i = 0; i < str2.length(); i++) {
    letters[str2[i]]--;
    if (letters[str2[i]] < 0) {
      return false;
    }
  }

  return true;



}

int main() {
  cout << permutation("ado", "dca") << endl;

}
