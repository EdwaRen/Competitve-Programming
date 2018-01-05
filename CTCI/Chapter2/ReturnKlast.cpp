#include <iostream>
#include <algorithm>

using namespace std;

struct node {
  int data;
  node *next;
};

class list {

public:
  node *head;
  node *tail;
  list() {
    head = NULL;
    tail = NULL;
  }
  void createNode(int value) {
    node *temp = new node;
    temp->data = value;
    temp->next = NULL;

    if (head == NULL) {
      head = temp;
      tail = temp;
      temp = NULL;
    } else {
      tail->next = temp;
      tail = temp;
    }
  }
  void display() {
    node *temp = new node;
    temp = head;
    while (temp != NULL) {
      cout << temp->data << " ";
      temp = temp->next;
    }
  }
  int ktoLast(node *n, int k) {

    if (n == NULL) {
      return 0;
    }

    int a = ktoLast(n->next, k)+1;
    if (a == k) {
      cout << n->data << endl;
      return 0;
    } else {
      return a;
    }

  }
};

int main() {
  list obj;
  obj.createNode(2);
  obj.createNode(5);
  obj.createNode(6);
  obj.createNode(7);
  obj.createNode(3);
  obj.createNode(2);
  obj.display();
  cout << endl;
  // cout << obj.head->data << endl;
  obj.ktoLast(obj.head, 4);

}
