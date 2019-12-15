#include <iostream>
#include <string>
#include <algorithm>
using namespace std;

int lengthOfLongestSubstring(string s) {
  int array[256] = {0};
  int ans = 0;
  int i = 0;

  for (int j = 0; j < s.length(); j++) {
    // cout << "ans: " << ans << endl;
    i = max(i, array[s[j]]);
    // cout << "values: " <<ans << " " << j-i+1 << " " << max(ans, j - i +1)  << endl;
    ans = max(ans, j - i +1);
    array[s[j]] = j+1;
  }

  return ans;
}

int main() {
  cout << lengthOfLongestSubstring("abcdefabc") << endl;
}
