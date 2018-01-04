#include <iostream>

using namespace std;

int rotate(int arr[][2], int size) {
  int newarr[2][2];
  for (int i = 0; i < size; i++) {
    for (int j = 0; j < size; j++) {
      newarr[i][j] = 0;
    }
  }


  for (int i = 0; i < size/2; i++) {
    // Topleft
    for (int j = i; j < size-i-1; j++) {
      newarr[i][j] = arr[size-j-1][i];
    }

    // Topright
    for (int j = i; j < size-i-1; j++) {
      newarr[j][size-1-i] = arr[i][j];
    }

    // Bottom right
    for (int j = i; j < size-i-1; j++) {
      newarr[size-i-1][size-1-j] = arr[j][size-1-i];
    }

    for (int j = i; j < size-i-1; j++) {
      newarr[size-j-1][i] = arr[size-i-1][size-1-j];
    }
  }

  for (int i = 0; i < size; i++) {
    cout << endl;
    for (int j = 0; j < size; j++) {
      cout << newarr[i][j] << " ";
    }
  }

  return 0;
}


int main() {
  int b[4][4] = {{1, 1, 1, 1}, {3, 4, 5, 2}, {3, 6, 7, 2}, {3, 2, 2, 2} };
  // int b[2][2] = {{1, 2}, {3, 4}};
  int a = rotate(b, 2);
  return 1;
}
