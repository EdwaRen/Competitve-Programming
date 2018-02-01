#include <iostream>
#include <unordered_map>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
};

int countpaths(TreeNode* a, int targetSum, int curSum, unordered_map<int, int> map) {
  if (a == NULL) {
    return 0;
  }

  curSum += a->val;

  int totalCount = map[curSum-targetSum];
  if (curSum == targetSum) {
    totalCount++;
  }

  map[curSum]++;
  totalCount += countpaths(a->left, targetSum, curSum, unordered_map<int, int> map);

  totalCount += countpaths(a->right, targetSum, curSum, unordered_map<int, int> map);
  map[curSum]--;



  return totalCount;

}
