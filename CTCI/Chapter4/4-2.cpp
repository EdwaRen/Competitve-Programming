#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <algorithm>
#include <queue>
#include <string>
#include <memory>
#include <limits>

struct node {
  node(int val) : val(val) {}
  int val;
  node* left;
  node* right;
};

node* treeConstruct(int *arr, int start, int end) {
  if ((start-end) < 1 ){
    return nullptr;
  }

  node* r = new node(arr[(start-end)/2]);
  r->left = treeConstruct(arr, start, ((start-end)/2)-1);
  r->right = treeConstruct(arr, ((start-end)/2)+1, end);
  return r;
}

void print_tree(node* node, const int depth = 0) {
	// if (node == nullptr) {
	// 	return;
	// }
  //
	// int indents = 3 * depth;
	// char spaces[indents + 1] = { '\0' };
	// for (int i = 0; i < indents; i++) {
	// 	spaces[i] = ' ';
	// }
  //
	// print_tree(node->left, depth + 1);
	// printf("%s%i\n", spaces, node->val);
	// print_tree(node->right, depth + 1);
}

int main(int argc, char** argv) {
	int sorted_list[] = { 0, 1, 2, 3, 4, 5, 6, 7, 8 };
	node* root = treeConstruct(sorted_list,0, 9);
	// print_tree(root);
  return 0;
}
