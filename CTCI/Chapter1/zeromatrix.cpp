#include <iostream>

using namespace std;

void zero(int **arr, int m, int n) {
    // ...
    int firstRow = 0;
    int firstColumn = 0;
    for (int i = 0; i < m; i++) {
      if (arr[i][0] == 0) {
        // cout << "first column 0 "<< i << endl;
        firstColumn = 1;
      }
    }
    for (int i = 0; i < n; i++) {
      if (arr[0][i] == 0) {
        // cout << "first row 0 "<< i << endl;

        firstRow = 1;
      }
    }

    for (int i = 1; i < m; i++) {
      for (int j = 1; j < n; j++) {
        if (arr[i][j] == 0) {
          arr[i][0] = 0;
          arr[0][j] = 0;
        }
      }
    }

    for (int i = 0; i < n; i++) {
      if (arr[0][i] == 0) {
        for (int j = 1; j < m; j++) {
          arr[j][i] = 0;
        }
      }
    }

    for (int i = 0; i < m; i++) {
      if (arr[i][0] == 0) {
        for (int j = 1; j < n; j++) {
          arr[i][j] = 0;
        }
      }
    }

    if (firstRow) {
      for (int i = 0; i < n; i++) {
        arr[0][i] = 0;
      }
    }
    if (firstColumn) {
      for (int i = 0; i < m; i++) {
        arr[i][0] = 0;
      }
    }

}


int main() {
  int **arr;
  const int m = 5;

  const int n = 4;
  arr = new int *[m];
  for(int i = 0; i <m; i++) {
    arr[i] = new int[n];
  }

  for(int i = 0; i <m; i++) {
    for(int j = 0; j <n; j++) {
      arr[i][j] = 1;
    }
  }
  arr[0][3] = 0;
  arr[1][2] = 0;


  for(int i = 0; i <m; i++) {
    cout << endl;
    for(int j = 0; j <n; j++) {
      cout << arr[i][j] << " ";
    }
  }
  zero(arr, m, n);
  cout << endl;

  for(int i = 0; i <m; i++) {
    cout << endl;
    for(int j = 0; j <n; j++) {
      cout << arr[i][j] << " ";
    }
  }

  return 1;

}
