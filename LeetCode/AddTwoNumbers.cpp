#include <iostream>

using namespace std;

struct ListNode {
  int val;
  ListNode *next;
  ListNode(int x) : val(x), next(NULL) {}
};

ListNode* optimal(ListNode* l1, ListNode* l2) {
  ListNode* a1 = l1;
  ListNode* a2 = l2;
  ListNode* traverse = new ListNode(0);
  ListNode* p = traverse;
  int sum = 0;
  while (a1 != NULL || a2 != NULL) {

    if (a1 != NULL) {
      sum+= a1->val;
      a1 = a1->next;
    }
    if (a2 != NULL) {
      sum+= a2->val;
      a2 = a2->next;
    }
    p->next = new ListNode(sum%10);
    sum /=10;

    // cout << "sum: " << sum << " "<< p->next->val << endl;

    p = p->next;
  }
  if (sum) {
    p->next = new ListNode(1);
  }
  return traverse->next;
}


ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
  ListNode* sum = new ListNode(0);
  ListNode* sumCpy = sum;

  sum->next = NULL;
  sum->val = 0;

  int carry = 0;

  ListNode* l1sweep = l1;
  ListNode* l2sweep = l2;
  // sum->val = l1sweep->val + l2sweep->val + carry;
  // if (sum->val >= 10) {
  //   carry= 1;
  //   sum->val = sum->val%10;
  // } else {
  //   carry = 0;
  // }

   do {
     // cout << "iteration " << sum->val << endl;
    ListNode* nextSum = new ListNode(l1sweep->val + l2sweep->val + carry);

    if (nextSum->val >= 10) {
      carry= 1;
      nextSum->val = nextSum->val%10;
    } else {
      carry = 0;
    }
    nextSum->next = NULL;
    sumCpy->next = nextSum;
    sumCpy = sumCpy->next;

    l1sweep = l1sweep->next;
    l2sweep = l2sweep->next;
  } while (l1sweep != NULL && l2sweep != NULL);

 while (l1sweep != NULL) {
    ListNode* nextSum = new ListNode(l1sweep->val  + carry);
    if (nextSum->val >= 10) {
      carry= 1;
      nextSum->val = nextSum->val%10;
    } else {
      carry = 0;
    }
    nextSum->next = NULL;
    sumCpy->next = nextSum;
    sumCpy = sumCpy->next;
    l1sweep = l1sweep->next;
  }

   while (l2sweep != NULL) {
    ListNode* nextSum = new ListNode(l2sweep->val  + carry);
    if (nextSum->val >= 10) {
      carry= 1;
      nextSum->val = nextSum->val%10;
    } else {
      carry = 0;
    }
    nextSum->next = NULL;
    sumCpy->next = nextSum;
    sumCpy = sumCpy->next;
    l2sweep = l2sweep->next;
  }

  if (carry == 1 ){
    ListNode* nextSum = new ListNode(1);
    nextSum->next = NULL;
    sumCpy->next = nextSum;
  }

  return sum->next;
}

int main() {
  ListNode* num1 = new ListNode(0);
  ListNode* num2 = new ListNode(0);
  ListNode* num3 = new ListNode(0);
  ListNode* num4 = new ListNode(0);

  num1->val = 2;
  num1->next = num2;
  num2->val = 4;
  num2->next = num3;
  num3->val = 9;
  num3->next = NULL;
  // num4->val = 1;
  // num4->next = NULL;

  ListNode* num21 = new ListNode(0);
  ListNode* num22 = new ListNode(0);
  ListNode* num23 = new ListNode(0);
  num21->val = 5;
  num21->next = num22;
  num22->val = 6;
  num22->next = num23;
  num23->val = 4;
  num23->next = NULL;

  ListNode* totalSum = optimal(num1, num21);
  while (totalSum->next != NULL) {
    cout << totalSum->val << endl;
    totalSum = totalSum->next;
  }
  cout << totalSum->val << endl;
return 0;

}
