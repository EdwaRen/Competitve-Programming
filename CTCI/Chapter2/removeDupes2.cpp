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
  void deleteNode(int pos) {
    node *prev = new node;
    node *curr = new node;
    curr = head;
    if (pos == 0 ){
      head = head->next;
    }
    for (int i = 0; i < pos; i++) {
      prev = curr;
      curr = curr->next;
    }
    prev->next = curr->next;
  }

  void deleteDups() {
    node *current = new node;
    current = head;
    while (current != NULL) {
      node *runner = new node;
      runner = current;
      while (runner->next != NULL) {

        if (current->data == runner->next->data) {
          prev->next = runner->next;
        }
      }
      current = current->next;
    }

  }

};



int main() {
  list obj;
	obj.createNode(25);
	obj.createNode(50);
	obj.createNode(90);
	obj.createNode(40);
  obj.createNode(50);
  obj.deleteDups();


  // obj.deleteNode(2);
	cout<<"\n--------------------------------------------------\n";
	cout<<"---------------Displaying All nodes---------------";
	cout<<"\n--------------------------------------------------\n";
	obj.display();

}
