#include <iostream>
#include <algorithm>

using namespace std;

struct node {
  int data;
  node *next;
};

class list {
private:
  node *head;
  node *tail;
public:
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

};

node* partition(node *n, int x) {
  node *beforeStart = new node;
  node *beforeEnd = new node;
  node *afterStart = new node;
  node *afterEnd = new node;


  beforeStart->next = NULL;
  beforeEnd->next = NULL;
  afterStart->next = NULL;
  afterEnd->next = NULL;



  while (n != NULL) {
    node *nx = new node;
    n->next = NULL;
    if (n->data < x) {
      if (beforeStart == NULL) {
        beforeStart = n;
        beforeEnd = n;
      } else {
        beforeEnd->next = n;
        beforeEnd = n;
      }

    } else {
      if (afterStart == NULL) {
        afterStart = n;
        afterEnd = n;
      } else {
        afterStart->next = n;
        afterEnd = n;
      }
    }
    node = nx;
  }

  beforeEnd->next = afterStart;
  return beforeStart;


}
