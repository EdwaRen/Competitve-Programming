#include <iostream>
using namespace std;

const int MAX_SIZE = 100;

class Stack {
private:
  int cur;
  int *buf;
  int capacity;
public:
  Stack(int capa = MAX_SIZE) {
    capacity = capa;
    cur = -1;
    buf = new int[capa];
  }

  void updateQueue() {
    // if (bufFilled) {
    for (int i = 0; i < cur; i++) {
      queue[i] = buf[cur-i];
      bufFilled = !bufFilled;
    }
    // } else {
    //   for (int i = 0; i < cur; i++) {
    //     buf[i] = queue[cur-i];
    //     bufFilled = !bufFilled;
    //   }
    // }

  }

  void push(int value) {
    cur++;
    buf[cur] = value;
  }

  void pop() {
    cur--;
  }
  int peak() {
    return buf[cur];
  }
  int size() {
    return cur;
  }
  bool isEmpty() {
    return (cur == -1);
  }
}

class MyQueue {
private:
  Stack stackNew;
  Stack stackOld;
public:
  MyQueue(int capa) {
    stackNew = Stack(capa);
    stackOld = Stack(capa)
  }
  void add(int value) {
    stackNew.push(value);
  }

  void shiftStacks() {
    if (stackOld.isEmpty) {
      while (!stackNew.isEmpty()) {
        stackOld.push(stackNew.peak());
        stackNew.pop();
      }

    }
  }

  int peek() {
    shiftStacks();
    return(stackOld.peak())
  }

  void remove() {
    shiftStacks();
    stackOld.pop();
  }

}
