#include <iostream>

using namespace std;

const int MAX_INT = ~(1<<31);

typedef struct node {
  int value;
  int min;

} node;

class StackWithMin {
public:
  StackWithMin(int size = 1000) {
    buf = new node[size];
    buf[0].min = MAX_INT;
    cur = 0;
  }

  void push(int val) {
    buf[cur+1]->value = val;
    cur++;
    if (buf[cur-1]->min > val) {
      buf[cur]->min = val
    } else {
      buf[cur]->min = buf[cur-1]->min
    }
  }
  void pop() {
    cur--;
  }
  int top() {
    return buf[cur].val;
  }
  bool empty() {
    return (cur == 0);
  }

  int min() {
    return buf[cur].min;
  }

private:
  node *buf;
  int cur;
}

int main() [

]
