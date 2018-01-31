#include <iostream>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* parent;
  TreeNode* left;
  TreeNode* right;
};

TreeNode* Order(TreeNode* a) {
  if (a->right != NULL) {
    TreeNode* b = new TreeNode;
    b = a->right;
    while (b->left != NULL) {
      b = b->left;
    }
    return b;
  } else {
    TreeNode* b = new TreeNode;
    b = a->parent;
    while (b->parent->right != b && b!= NULL) {
      b = b->parent;
    }
    return b->parent;
  }
}
