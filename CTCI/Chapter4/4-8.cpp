#include <iostream>
#include <unordered_map>

using namespace std;

struct TreeNode {
  int val;
  TreeNode* parent;
  TreeNode* left;
  TreeNode* right;
};

TreeNode* parent(TreeNode* a, TreeNode* b) {
  unordered_map<int, int> map;
  while (map[a->parent] != 2) {
    map[a->parent]++;
    map[b->parent]++;
    a = a->parent;
    b = b->parent;
  }
  return a->parent;
}
