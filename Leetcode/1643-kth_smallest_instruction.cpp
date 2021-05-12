#include <vector>
#include <iostream>
#include <string>

using namespace std;
class Solution {
public:
    string kthSmallestPath(vector<int>& destination, int k) {
        vector<vector<int>> dp(16, vector<int>(16, 1));
        for (int i = 1; i < dp.size(); i++) {
            for (int j = 1; j < dp[0].size(); j++) {
                dp[i][j] = dp[i-1][j] + dp[i][j-1];
            }
        }
        string res = "";
        int row = destination[0];
        int col = destination[1];
        while (row > 0 && col > 0) {
            if (dp[row][col-1] >= k) {
                col--;
                res.push_back('H');
            } else {
                k-=dp[row][col-1];
                row--;
                res.push_back('V');
            }
        }
        while (row > 0) {
            row--;
            res.push_back('V');
        }
        while (col > 0) {
            col--;
            res.push_back('H');
        }
        return res;
    }
};

int main() {
    vector<int> dest = {2, 3};
    int k = 3;
    Solution sol;
    cout << sol.kthSmallestPath(dest, k) << endl;
}