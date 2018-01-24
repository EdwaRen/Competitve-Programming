#include <iostream>

using namespace std;

class FixedMultiStack {
private:
  int numberOfStacks;
  int stackCapacity;
  int *values;
  int *sizes;
public:
  FixedMultiStack(int stackSize) {
    stackCapacity = stackSize;
    values = new int[stackSize*numberOfStacks];
    sizes = new int[stackSize];
  }
  void push(int stackNum, int value) {
    if (isFull(stackNum)) {
      return;
    } else {
      sizes[stackNum]++;
      values[stackNum*stackCapacity + sizes[stackNum] -1] = value;
    }
  }
  void pop(int stackNum) {
    if (isEmpty(stackNum)) {
      return;
    } else {
      values[stackNum*stackCapacity + sizes[stackNum]-1] = 0;
      values[stackNum]--;
    }
  }
  int peek(int stackNum) {
    if (isEmpty(stackNum)) {
      return 0;
    } else {
      return values[stackNum*stackCapacity + sizes[stackNum]-1];
    }
  }
  int isEmpty(int stackNum) {
    return sizes[stackNum] == 0;
  }
  int isFull(int stackNum) {
    return sizes[stackNum] == stackCapacity;
  }
};

int main() {
  return 0;
}
