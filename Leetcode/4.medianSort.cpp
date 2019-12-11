#include <iostream>
#include <algorithm>
#include <vector>

using namespace std;

double findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
  vector<int> c;
  c.reserve(nums1.size()+nums2.size());
  c.insert(c.end(), nums1.begin(), nums1.end());
  c.insert(c.end(), nums2.begin(), nums2.end());

  sort(c.begin(), c.begin()+c.size());
  if (c.size()%2 == 1) {
    // cout << "odd " << c.size() << endl;
    return static_cast<double>(c[c.size()/2]+0.0);
  } else {
    // cout << "even" << endl;
    return (c[c.size()/2] + c[(c.size()/2)-1] )*0.5;
  }
}


int main() {
  int a[] = {1, 2, 3, 4, 5, 6, 9};
  int b[] = { 7, 10, 14444, 123};
  vector<int> c(a, a+7);
  vector<int> d(b, b+4);

  cout << findMedianSortedArrays(c, d) << endl;;

  return 0;
}
