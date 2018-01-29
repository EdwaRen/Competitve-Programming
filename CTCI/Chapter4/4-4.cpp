#include <iostream>
#include <math.h>
using namespace std;

struct Node {
  int val;
  Node* next;
};

struct TreeNode {
  int val;
  TreeNode* left;
  TreeNode* right;
};

int balanceTree(TreeNode a) {
  if (a == NULL) {
    return -1;
  } else {
    l = balanceTree(a->left);
    if (l == -2) {
      return -2;
    }
    r = balanceTree(a->right);
    
    if (r == -2) {
      return -2;
    }
    int height = abs(l-r);

    if (height > 1) {
      return -2;
    } else {
      if (l>r) {
        return l+1
      } else {
        return r+1;
      }
    }
  }
}
