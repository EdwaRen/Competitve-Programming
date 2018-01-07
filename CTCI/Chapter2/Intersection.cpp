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


node* intersection(node *n1, node *n2, int len1, int len2) {

  int bigLen = len1;

  if (len1 > len2) {
    for (int i = 0; i < len1-len2; i++) {
      bigLen = len2;
      n1 = n1->next;
    }
  }

  if (len2 > len1) {
    for (int i = 0; i < len2-len1; i++) {
      bigLen = len1;
      n2 = n2->next;
    }
  }

  for (int i = 0; i < bigLen; i++) {
    if (n1->next == n2->next) {
      return n1;
    } else {
      n1 = n1->next;
      n2 = n2->next;
    }
  }
  return NULL;



}

int main() {
  list obj;
  obj.createNode(1);
  obj.createNode(2);
  obj.createNode(3);
  obj.createNode(2);
  obj.createNode(2);
  
  // obj.createNode(50);
  a = intersection(node *n1, node *n2, int len1, int len2)
  cout << "palin final: " << a->palin <<" final end: " << endl;


  // obj.deleteNode(2);
  cout<<"\n--------------------------------------------------\n";
  cout<<"---------------Displaying All nodes---------------";
  cout<<"\n--------------------------------------------------\n";
  obj.display();
}
