#include <iostream>
#include <string>

using namespace std;

string urlify(string str, int count) {
  int spaceCount = 0;
  for (int i = 0; i < count; i++ ) {
    if (str[i] == ' ') {
      spaceCount++;
    }
  }

  int index = count + 2*spaceCount;

  if (count < str.length()) {
    str[count] = '\0';
  }

  for (int i = count-1; i>= 0;i--) {
    if (str[i] == ' ' ){
      str[index-1] = '0';
      str[index-2] = '2';
      str[index-3] = '.';
      index = index-3;
    } else {
      str[index - 1] = str[i];
      index--;
    }
  }
  return str;

}

int main() {


cout << urlify("mr John Smith    ", 13);
  return 1;
}
