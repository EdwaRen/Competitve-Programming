#include <iostream>
#include <vector>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* parent;
  TreeNode* left;
  TreeNode* right;
};

void printVec(vector<int> prefix) {
  cout << "{ ";
  for (int i = 0; i < prefix.length(); i++) {
    cout << prefix[i]<< " ";
  }
  cout << " }" << endl;
}

void weave(TreeNode* l, vector<int> prefix) {
  if (l->right == NULL) {
    prefix.push_back(l->val);
    TreeNode* n new TreeNode;
    n = r;
    while (n->next != NULL) {
      prefix.push_back(n->val);
    }
    prefix.push_back(n->val);
    printVec(prefix);
  } else if (l->right == NULL) {

    prefix.push_back(l->val);
    TreeNode* n new TreeNode;
    n = l;
    
    while (n->next != NULL) {
      prefix.push_back(n->val);
    }
    prefix.push_back(n->val);
    printVec(prefix);
  } else {
    weave(l->left, prefix.push_back(l->val));
    weave(l->right, prefix.push_back(l->val));
  }
}

// void weave(vector<int> left, vector<int> right, vector<int> prefix) {

  // if (left.length() == 0) {
  //   prefix += right;
  //   cout << "{ " << prefix << " }" << endl;
  // } else if (right.length() == 0) {
  //   prefix += left;
  //   cout << "{ " << prefix << " }" << endl;
  // } else {
  //   int lastLeft = left[left.length()-1];
  //   int lastRight = right[right.length()-1];
  //
  //   weave(left.pop_back(), right, prefix+lastLeft);
  //   weave(left, right.pop_back(), prefix+lastRight);
  // }
}

void bstArr(TreeNode* a) {
  vector<int> arr;
  arr[0] = a->val;

}
