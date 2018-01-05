#include <iostream>

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
      cout << temp->data << "\t";
      temp = temp->next;
    }
  }
  void insert_position(int value, int pos) {
    node *pre=new node;
    node *cur=new node;
    node *temp=new node;
    cur=head;
    for(int i=1;i<pos;i++)
    {
      pre=cur;
      cur=cur->next;
    }
    temp->data=value;
    pre->next=temp;
    temp->next=cur;

  }
  void delete_position(int pos) {
    node *cur = new node;
    node *pre = new node;

    cur = head;

    for (int i = 1; i < pos; i++) {
      pre = cur;
      cur = cur->next ;
    }
    pre->next = cur->next;


  }



};




int main() {
  list obj;
	obj.createNode(25);
	obj.createNode(50);
	obj.createNode(90);
	obj.createNode(40);
  obj.delete_position(2);
	cout<<"\n--------------------------------------------------\n";
	cout<<"---------------Displaying All nodes---------------";
	cout<<"\n--------------------------------------------------\n";
	obj.display();

}
