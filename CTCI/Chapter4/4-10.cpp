#include <iostream>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
}

int traverse(TreeNode* a, TreeNode* b) {
  if (a==NULL) {
    return 1;
  }

  if (a->val == b->val) {
    return mix(a->left, b->left) && mix(a->right, b->right);
  }

  return traverse(a->left, b) || traverse(a->right, b);

}

int mix(TreeNode* a, TreeNode b) {
  if (a->val == b->val || (a == NULL && b == NULL)) {
    return mix(a->left, b->left) && mix(a->right, b->right;

  } else {
    return 0;
  }
}
