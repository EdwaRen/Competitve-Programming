#include <iostream>
#include <vector>

using namespace std;

struct Node {
  int val;
  Node* next;
};

struct Tree {
  int val;
  Node* left;
  Node* right;
}


void createLinkedLists(Tree* root, vector<Node> lists, int level) {
  if (lists.length() == level) {
    Node* nLevel = new Node;
    nLevel->val = root->val;
    nLevel->next = NULL;
    lists.push_back(nLevel);
  } else {

  }
  lists[level].push(root->val);
  createLinkedLists(root->left, lists, level+1)
  createLinkedLists(root->right, lists, level+1)

}
