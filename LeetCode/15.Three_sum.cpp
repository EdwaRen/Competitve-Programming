#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

vector<vector<int>> threeSum(vector<int>& nums) {
  sort(nums.begin(), nums.begin()+nums.size());
  vector<vector<int>> sums;
  for (int i = 0; i < nums.size(); i++) {
    cout << (nums[i]) << endl;
    int l = 0;
    int r = nums.size()-1;
    while (l != r) {
      int current_sum = nums[l] + nums[r] + nums[i];
      if (current_sum == 0) {
        if (l == 0 || nums[l] != nums[l-1]) {
          if (r == nums.size()-1 || nums[r] != nums[r+1]) {
            vector<int> solution;
            solution.push_back(nums[i]);
            solution.push_back(nums[r]);
            solution.push_back(nums[l]);
            sums.push_back(solution);
          }
        }
      } else if (current_sum < 0) {
        l++;
      } else {
        r--;
      }
    }

    // for (auto i = sums.begin(); i != sums.end(); ++i)
    //   cout << *i << ' '<< endl;
  }

  return sums;

}


int main() {
  int inputarr[] = {-1, 0, 1, 2, -1, -4};
  vector<int> inputvec (inputarr, inputarr+6) ;
  vector<vector<int>> a = threeSum(inputvec);
  for (int i = 0; i < a.size(); i++) {
    for (int j = 0; j < a[i].size(); j++) {
      cout << "i and j" << i << " " << a[i][j] << endl;
    }
    cout << endl;
  }
}
