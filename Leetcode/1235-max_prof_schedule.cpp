#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <iterator>     // std::next

using namespace std;
class Solution {
public:
    static bool sortEndTime(const vector<int>& v1, const vector<int>& v2) {
      return v1[1] < v2[1];
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<vector<int>> allProfits;
        for (int i = 0; i < startTime.size(); i++) {
          allProfits.push_back({startTime[i], endTime[i], profit[i]});
        }
        sort(allProfits.begin(), allProfits.end(), sortEndTime);
        map<int, int> endProfits = {{0, 0}};
        int maxProfits = 0;
        for (auto& row:allProfits) {
          int curMax = prev(endProfits.upper_bound(row[0]))->second + row[2];
          maxProfits = max(maxProfits, curMax);
          if (curMax > endProfits.rbegin()->second) {
            endProfits[row[1]] = curMax;
          }
        }

        return maxProfits;
    }
};

int main() {
    Solution solution;
    int initStartTime[] = {1, 2, 3, 3};
    int initEndTime[] = {3, 4, 5, 6};
    int initProfit[] = {50, 10, 40, 70};

    vector<int> startTime(initStartTime, initStartTime+4);
    vector<int> endTime(initEndTime, initEndTime+4);
    vector<int> profit(initProfit, initProfit+4);

    cout << solution.jobScheduling(startTime, endTime, profit) << endl;
    return 0;
}