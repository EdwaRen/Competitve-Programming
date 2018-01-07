#include <iostream>
#include <math.h>       /* floor */

using namespace std;

struct node {
  int data;
  node *next;
};

class list {
private:
  node *head ;
  node *tail ;
public:
  list() {
    head = NULL;
    tail = NULL;
  }
  node* getHead() {
    return head;
  }
  void setHead(node *n) {
    n->next = head;
    head = n;
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

node* recurse (node* n1, node* n2) {
  if (n1->next == NULL && n2->next == NULL) {
    node *n3 = new node;
    n3->data = n1->data + n2->data;
    n3->next = NULL;
    return n3;
  } else {
    node *a = new node;
    a = recurse(n1->next, n2->next);
    int c = 0;
    c = floor(a->data)/10;
    a->data %= 10;


    node *n3 = new node;
    n3->data = n1->data + n2->data + c;
    n3->next = a;
    return n3;
  }
}
int lengthList(node* n) {
  int l = 1;
  node *temp = new node;
  temp = n;
  while (temp->next != NULL) {
    temp = temp->next;
    l++;
  }
  return l;
}


int main() {
  list obj;
	obj.createNode(1);
	obj.createNode(3);
	obj.createNode(5);
	obj.createNode(7);

  list obj2;
	obj2.createNode(3);
	obj2.createNode(5);
	obj2.createNode(7);

  int len = lengthList(obj.getHead());
  int len2 = lengthList(obj2.getHead());
  cout << "lens " << len << " " << len2 << " " << obj.getHead()->data << endl;
  if (len < len2) {
    for (int i = 0; i < len2 - len; i++) {
      node *z = new node;
      z->data = 0;
      obj.setHead(z);
    }

  }

  if (len > len2) {
    for (int i = 0; i < len - len2; i++) {
      node *z = new node;
      z->data = 0;
      obj2.setHead(z);
    }
  }


  cout << "recursed: "<<recurse(obj.getHead(), obj2.getHead())->data << endl;

  cout << "recursed: "<<recurse(obj.getHead(), obj2.getHead())->next->data << endl;
  cout << "recursed: "<<recurse(obj.getHead(), obj2.getHead())->next->next->data << endl;
  cout << "recursed: "<<recurse(obj.getHead(), obj2.getHead())->next->next->next->data << endl;

  // obj.deleteNode(2);
	cout<<"\n--------------------------------------------------\n";
	cout<<"---------------Displaying All nodes---------------";
	cout<<"\n--------------------------------------------------\n";
	obj.display();

}
