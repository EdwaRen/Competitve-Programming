#include <iostream>

using namespace std;

const MAX_SIZE = 100;

class Stack {
private:
  int cur;
  int *buf;
public:
  Stack(int capa = MAX_SIZE) {
    buf = new int[capa];
    cur=-1;
  }
  int size() {
    return cur;
  }
  void push(int value) {
    cur++;
    buf[cur] = value;
  }
  int peak() {
    return buf[cur];
  }
  void pop() {
    cur--;
  }

}

void sortStack(Stack s1) {
  Stack s2 = Stack(s1.size());

  while (!s1.isEmpty()) {
    int temp = s1.peak();
    s1.pop();
    if s2.isEmpty() {
      s2.push(temp);
    } else {
      while (!s2.peak() > temp) {
        s1.push(s2.peak());
        s2.pop();
        if (s2.isEmpty()) {
          break;
        }
      }
      s2.push(temp);
    }
  }
  while (!s2.isEmpty()) {
    s1.push(s2.peak());
    s2.pop();
  }

}
