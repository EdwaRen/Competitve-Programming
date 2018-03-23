#include <unordered_map>
#include <vector>
#include <iostream>

using namespace std;


vector<int> twoSum(vector<int>& nums, int target) {
  unordered_map<int, int> myMap;
  for (int i = 0; i < nums.size(); i++) {
    myMap[nums[i]] = i;
  }
  vector<int> v;

  for (int i = 0; i < nums.size(); i++) {
    if( (myMap.find(target - nums[i]) != myMap.end()) && (i != myMap[target-nums[i]])) {
      v.push_back(i);
      v.push_back(myMap[target - nums[i]]);

      return v;
    }
  }
  return v;

}


int main() {
  vector<int> nums = {3, 2, 4};

  vector<int> result = twoSum(nums, 6);

  cout <<  result[0] << " " << result[1];

}
