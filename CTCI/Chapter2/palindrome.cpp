#include <iostream>

using namespace std;

struct node {
  int data;
  node *next;
};

struct result {
  node *rnode;
  int palin;
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

result* recurse(node* n, int l) {
  if (l == 1) {
    result *middle = new result;
    middle->rnode = n;
    middle->palin = 1;
    return middle;

  } else if (l == 2) {
    if (n->data == n->next->data) {
      result *middle = new result;
      middle->rnode = n->next;
      middle->palin = 1;
      return middle;
    } else {
      result *middle = new result;
      middle->rnode = n->next;
      middle->palin = 0;
      return middle;

    }

  } else {
    cout << "resulting" << endl;
    result *a = recurse(n->next, l-2);
    if (a->rnode->next == NULL) {
      cout <<"Palinfinal: " << a->palin << endl;

      cout <<"Palin: " <<  a->palin << endl;
      return a;
    } else {
      cout <<"Palin: " << a->palin << endl;

      cout << "not null "<< a->rnode->data << n->data << endl;
      if (a->rnode->next->data == n->data) {
        a->rnode = a->rnode->next;
        return a;
      } else {

        a->rnode = a->rnode->next;
        a->palin = 0;
        return a;
      }
    }
  }
}

int main() {
  list obj;
  obj.createNode(1);
  obj.createNode(2);
  obj.createNode(3);
  obj.createNode(2);

  obj.createNode(2);
  // obj.createNode(50);
  result *a = new result;
  a = (recurse(obj.getHead(), 5));
  cout << "palin final: " << a->palin <<" final end: " << endl;


  // obj.deleteNode(2);
  cout<<"\n--------------------------------------------------\n";
  cout<<"---------------Displaying All nodes---------------";
  cout<<"\n--------------------------------------------------\n";
  obj.display();
}
