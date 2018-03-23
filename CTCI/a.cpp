#include <iostream>
#include <string>
#include <unordered_map>

using namespace std;

int main()
{
  unordered_map<int, int> myMap;

  int arr[] = {1, 7, 5, 9, 2, 12, 3};
  for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
    myMap[arr[i]] = 1;
  }
  // unordered_map<std::string, int> months;
  // months["1"] = 31;
  // months["7"] = 28;
  // months["5"] = 31;
  // months["9"] = 30;
  // months["2"] = 31;
  // months["12"] = 30;
  // months["3"] = 31;

  // cout << "september -> " << months["1"] << endl;
  // cout << "april     -> " << months["7"] << endl;
  // cout << "december  -> " << months["5"] << endl;
  // cout << "february  -> " << months["9"] << endl;
  // cout << "february  -> " << months["8"] << endl;
  int total = 0;
  for (int i = 0; i < sizeof(arr)/sizeof(arr[0]); i++) {
    if (myMap[arr[i]+2] == 1 ) {
      cout << "arr[i] " << arr[i] << endl;
      total++;
    }
  }
  cout << total << endl;

  return 0;
}
