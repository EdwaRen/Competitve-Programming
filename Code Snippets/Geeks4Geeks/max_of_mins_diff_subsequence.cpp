#include <bits/stdc++.h>
#include <vector>
using namespace std;

bool check_min(const vector<int>& A, int min, int B) {
    int prev = A[0];
    int count = 1;
    for (auto& num:A) {
        if (num >= prev + min) {
            count++;
            prev = num;
            if (count == B) {
                return true;
            }
        }
    }
    return false;
}

int find_min_difference(vector<int>& A, int n, int B){
    sort(A.begin(), A.end());
    int lo = 0;
    int hi = A.back() - A[0];
    int res = 0;
    while (lo <= hi) {
        int mid = lo + ((hi - lo)/2);

        if (check_min(A, mid, B)) {
            lo = mid+1;
            res = mid;
        } else {
            hi = mid-1;
        }
    }
    return res;
}

int main()
{
    vector<int> A = { 5, 17, 11 };
    int n = sizeof(A) / sizeof(A[0]);
    int B = 2;
 
    int min_difference = find_min_difference(A, n, B);
    cout << min_difference << endl;
    return 0;
}