#include <iostream>

using namespace std;

const STACK_SIZE = 1000;

typedef struct node {
  int value;
  node *next;
}

class Stack {
private:
  int cur;
  int *buf;
  int capacity;
public:
  Stack(int capa = STACK_SIZE) {
    capacity = capa;
    cur = -1;
    buf = new int[capa];
  }

  void push(int value) {
    cur++;
    bur[cur] = value;
  }
  void pop() {
    cur--;
  }
  int top() {
    return buf[cur];
  }
  bool isEmpty() {
    return cur == -1;
  }
  bool full() {
    return cur == capacity-1;
  }
}

class SetStack() {
private:
  int cur;
  Stack *set;
  int capacity;
public:
  SetStack(int capa = STACK_SIZE) {
    capacity = capa;
    cur = 0;
    set = new Stack[capa];
  }
  void push(int value) {
    if set[cur].full() {
      cur++;
      set[cur].push(value);
    } else {
      set[cur].push(value);
    }
  }

  void pop() {
    if set[cur].isEmpty() {
      cur--;
    }
    set[cur].pop();
  }
}
