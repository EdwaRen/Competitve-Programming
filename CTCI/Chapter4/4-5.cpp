#include <iostream>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
};

int checkBst(TreeNode a, int min, int max) {
  if (a == NULL) {
    return true;
  }
  if (min != NULL && a->val < min) {
    return false;
  }
  if (max != NULL && a->val > max) {
    return false;
  }

  int l = checkBst(a->left, min, a->val);
  int r = checkBst(a->right, a->val, max);
  if (l == 0 || r == 0) {
    return false;
  }

  return true;
}
