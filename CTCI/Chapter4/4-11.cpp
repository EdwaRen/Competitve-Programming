#include <stdio.h>
#include <stdlib.h>
#include <algorithm>
#include <queue>
#include <string>
#include <memory>
#include <limits>
#include <list>
#include <random>
#include <iostream>

using namespace std;

struct TreeNode {
  int val;
  int size;
  TreeNode* left;
  TreeNode* right;

  TreeNode(int val) : val(val) {}



  void insertNode(int val) {
    TreeNode** child = val < this->val ? &left : &right;
		if (*child == NULL) {
			*child = new TreeNode(val);
		} else {
			(*child)->insertNode(val);
		}
		size++;
  }

  // void insert(TreeNode* a) {
  //
  //   TreeNode* temp = new TreeNode();
  //   temp=left;
  //   while (temp != NULL) {
  //     if (a->val > temp->val) {
  //       if (a->right == NULL) {
  //         temp->val = a->val;
  //         a->right = temp;
  //       }
  //       temp = a->right;
  //     }
  //   }
  //
  // }
};

void print_tree(TreeNode* node, const int depth = 0) {
	if (node == nullptr) {
		return;
	}

	int indents = 3 * depth;
	string spaces = "";
	for (int i = 0; i < indents; i++) {
		spaces = spaces + ' ';
	}

	print_tree(node->left, depth + 1);
	cout <<  spaces<< node->val << endl;
	print_tree(node->right, depth + 1);
}

// void insert(TreeNode* a, int b) {
//   TreeNode* temp = new TreeNode;
//   temp = &a;
//
//   while (temp != NULL) {
//     if (b->val > temp->val) {
//       temp = temp->right;
//     } else {
//       temp = temp->left;
//     }
//   }
// }

TreeNode* rngTree(TreeNode* a, int r) {

    cout << "logging " << a->val << " and " << r << endl;
   if (a==NULL || r == 0) {
    return a;
  }
  if (a->left == NULL) {
    return rngTree(a->right, r-1);
  }
  if (a->right == NULL) {
    return rngTree(a->left, r-1);
  }

  if (r <= a->left->size+1) {
    return a;
  }
  if (r > a->left->size+1) {
    r = r - a->left->size -2;
    return rngTree(a->right, r);
  } else {
    return rngTree(a->left, r-1);
  }

}

int main() {
  TreeNode* root = new TreeNode(3);
  root->insertNode(1);
	root->insertNode(5);
	root->insertNode(4);
	root->insertNode(2);
	root->insertNode(6);
	print_tree(root);
  TreeNode* a = rngTree(root, 4);
  cout << a->val << "DONE" << endl;
}
