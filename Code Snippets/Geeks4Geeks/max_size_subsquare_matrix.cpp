#include <vector>
#include <iostream>

using namespace std;

int max_subsquare(vector<vector<int>> matrix, int K) {
    int n = matrix.size();
    int m = matrix[0].size();
    vector<vector<int>> prefix_sum(n+1, vector<int>(m+1, 0));
    
    for (int i = 1; i <= n; i++) {
        for (int j = 1; j <= m; j++) {
          prefix_sum[i][j] = prefix_sum[i-1][j] + prefix_sum[i][j-1] + matrix[i-1][j-1] - prefix_sum[i-1][j-1];
        }
    }

    int res = 0;
    for (int i = 1; i <= n; i++) {
      for (int j = 1; j <= m; j++) {
        if (i+res >= n || j+res >= m) {
          break;
        }
        int mid;
        int lo = res;
        int hi = min(n-i+1, m-j+1);

        while (lo <= hi) {
          mid = lo + ((hi - lo)/2);
          if (prefix_sum[i+mid-1][j+mid-1] + prefix_sum[i-1][j-1] - prefix_sum[i+mid-1][j-1] - prefix_sum[i-1][j+mid-1] <= K) {
            lo = mid+1;
            res = max(res, mid);
          } else {
            hi = mid-1;
          }
        }
      }
    }
    
    return res;
}

int main() {
    vector<vector<int>> matrix {
        { 1, 1, 3, 2, 4, 3, 2 },
        { 1, 1, 3, 2, 4, 3, 2 },
        { 1, 1, 3, 2, 4, 3, 2 }
    };
    int K = 33;
    cout << max_subsquare(matrix, K) << endl;

    return 0;
}