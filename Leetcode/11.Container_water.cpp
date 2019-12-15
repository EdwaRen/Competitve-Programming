#include <vector>
#include <algorithm>    // std::max
#include <iostream>
using namespace std;


int maxArea(vector<int>& height) {
  int max_area = 0;
  int r, l;
  r = height.size()-1;
  l = 0;
  while (r > l) {
    max_area = max(max_area, ((abs(l-r))*min(height[r], height[l])  ));
    cout << "max_area " << max_area << " " << height[r] << " " << height[l] << " " << l << " " << r << endl;

    if (height[r] > height[l]) {
      l++;
    } else {
      r--;
    }
  }
  return max_area;


}

int main() {
  vector<int> v = {7, 5, 16, 8};
  cout << maxArea(v) << endl;

  return 0;
}
