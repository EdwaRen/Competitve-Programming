#include <iostream>

using namespace std;

int insertion(int n, int m, int i, int j) {
  int allOnes = ~0;
  int left = allOnes << (j+1);
  int right = (1<<i)-1;
  left = left | right;
  n = n & left;
  int m_shift = m << i;
  return m_shift | n;
}
