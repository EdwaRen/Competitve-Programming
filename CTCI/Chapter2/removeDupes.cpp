#include <iostream>
#include <algorithm>
#include <list>
#include <unordered_map>

using namespace std;

int main() {
  int myints[] = {5, 6,5, 4,6,   7, 3, 2, 5, 5};
  list<int> l (myints, myints + sizeof(myints)/sizeof(int));
  // list<int> l = { 7, 5, 16, 8 };
  unordered_map<int, int> myMap;

  for (auto it = l.begin(); it != l.end();) {
    if(myMap[*it]) {
      l.erase(it);
    } else {
      myMap[*it]++;
    }
    ++it;
  }
  for (auto it = l.begin(); it != l.end();) {
    cout << *it << " ";
    ++it;
  }
  cout << endl;

  cout << myMap[5] << " ";
  cout << myMap[6] << " ";
  cout << myMap[7] << " ";
  cout << myMap[3] << " ";
  cout << myMap[2] << " ";

return 1;

}
