#include <iostream>

using namespace std;

struct node {
  int data;
  node *next;
}

public:
  list() {
    head = NULL;
    tail = NULL;
  }
  node* getHead() {
    return head;
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
      cout << temp->data << " " << endl;
      temp = temp->next;
    }
  }
};

node* loopdetect(node *n) {

  node *n1 = n;
  node *n2 = n;
  while (n1->next != NULL && n2->next != NULL) {
    if n1->next == n2->next {
      break;
    }
    n1 = n1->next;
    n2 = n2->next->next;

  }
  if (n1 == NULL || n2 == NULL) {
    return NULL;
  }
  n1 = n;
  while (n->next != n2->next) {
    n = n->next;
    n2 = n2->next;
  }
  return n

}

int main() {

}
