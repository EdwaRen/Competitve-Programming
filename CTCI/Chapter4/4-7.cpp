#include <iostream>
#include <stack>

using namespace std;
struct  Node {
  int val;
  vector<Node*> children;
  int status = 1;
}

bool doDFS(Node* a, stack<int> s) {
  if (a->status == 0) {
    return false;
  }
  if (children.length() == 0) {
    s.push(a->value);
    return true;
  }
  if (a->status == 1) {
    a->status = 0;
    for (int i = 0; i < a->children.length(); i++) {
      int a = doDFS(a->children[i], s);
      if (a == 0) {
        return false;
      }
    }
    a->status = 2;
    s.push(a->val);
  }


  return true;

}
