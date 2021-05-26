#include <iostream>
#include <vector>


using namespace std;

class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int n = matrix.size();
        int m = matrix[0].size();
        vector<vector<int>> dp(n, vector<int>(m, 0));

        
        int max_square_size = 0;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (matrix[i][j] == 1) {
                    if (i > 0 && j > 0) {
                        dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1;
                    } else {
                        dp[i][j] = 1;
                    }
                }
                max_square_size = max(max_square_size, dp[i][j]);
            }
        }
        return max_square_size;
    }
};

int main() {
    Solution sol;
    vector<vector<int>> matrix = {
        {"1","0","1","0","0"},
        {"1","0","1","1","1"},
        {"1","1","1","1","1"},
        {"1","0","0","1","0"}
    };
    cout << sol.maximalSquare(matrix) << endl;
}