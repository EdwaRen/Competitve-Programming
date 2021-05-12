#include <iostream>
#include <vector>
#include <map>
#include <unordered_set>

using namespace std;

class Solution {
public:
    int findPairs(vector<int>& nums, int k) {
        unordered_set<int> recorded;
        map<int, int> seen;
        for (auto& num:nums) {
          seen[num]++;
        }
        int res = 0;
        for (auto& p:seen) {
          if ((k == 0 && p.second > 1) || (k > 0 && seen.count(p.first+k)>0)) {
            res++;
          }
        }
        return res;
    }
};

int main() {
    Solution solution;
    vector<int> nums = {3, 1, 4, 1, 5};
    int k = 4;

    cout << solution.findPairs(nums, k) << endl;
    return 0;
}