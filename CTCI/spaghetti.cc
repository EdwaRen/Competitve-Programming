#include <iostream>

using namespace std;

struct node {
  int data;
  node *next;
};

int main() {
  node* a = new node;
  a->data = 2;
  node* b = a;
  b->data = 5;
  cout << "b data " << b->data << " a data " << a->data<< endl;
  return 0;
}
