//
//  main.cpp
//  Selective Cutting
//
//  Created by - on 2017/06/27.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

// C++ code to demonstrate operations of Binary Index Tree
#include <iostream>
#include <algorithm>
#include <functional>

using namespace std;

struct greater
{
    template<class T>
    bool operator()(T const &a, T const &b) const { return a > b; }
};

/*            n  --> No. of elements present in input array.
 BITree[0..n] --> Array that represents Binary Indexed Tree.
 arr[0..n-1]  --> Input array for whic prefix sum is evaluated. */

// Returns sum of arr[0..index]. This function assumes
// that the array is preprocessed and partial sums of
// array elements are stored in BITree[].

int getSum(int BITree[], int index)
{
    int sum = 0; // Iniialize result
    
    // index in BITree[] is 1 more than the index in arr[]
    index = index + 1;
    
    // Traverse ancestors of BITree[index]
    while (index>0)
    {
        // Add current element of BITree to sum
        sum += BITree[index];
        
        // Move index to parent node in getSum View
        index -= index & (-index);
    }
    return sum;
}

// Updates a node in Binary Index Tree (BITree) at given index
// in BITree.  The given value 'val' is added to BITree[i] and
// all of its ancestors in tree.
void updateBIT(int BITree[], int n, int index, int val)
{
    // index in BITree[] is 1 more than the index in arr[]
    index = index + 1;
    
    // Traverse all ancestors and add 'val'
    while (index <= n)
    {
        // Add 'val' to current node of BI Tree
        BITree[index] += val;
        
        // Update index to that of parent in update View
        index += index & (-index);
    }
}

// Constructs and returns a Binary Indexed Tree for given
// array of size n.
int *constructBITree(int arr[], int n)
{
    // Create and initialize BITree[] as 0
    int *BITree = new int[n+1];
    for (int i=1; i<=n; i++)
        BITree[i] = 0;
    
    // Store the actual values in BITree[] using update()
    for (int i=0; i<n; i++)
        updateBIT(BITree, n, i, arr[i]);
    
    // Uncomment below lines to see contents of BITree[]
    //for (int i=1; i<=n; i++)
    //      cout << BITree[i] << " ";
    
    return BITree;
}


// Driver program to test above functions
int main()
{
    int N, Q;
    int queries[100001][3];
    int qOrder[100001];
    fill(qOrder, qOrder+N, 0);

    cin >> N;
    
    int trees[100001];
    fill(trees, trees+N, 0);
    
    for (int i = 0; i < N; i++) {
        cin >> trees[i];
    }
    cin >> Q;
    
    for (int i = 0; i < Q; i++) {
        scanf ("%d %d %d", &queries[i][0], &queries[i][1], &queries[i][2]);
        qOrder[i] = queries[i][2];
    }
    
    sort(qOrder, qOrder+N, greater<int>());
    int *BITree2[100001];
    
    for (int i = 0; i < Q-1; i++) {
        if (qOrder[i] != qOrder[i+1]) {
            BITree2[qOrder[i]] = constructBITree(trees, N);
            if (i == Q-2 && qOrder[i+1] != qOrder[i]) {
                BITree2[qOrder[i+1]] = constructBITree(trees, N);
                
            }
        }
        
    }
    
    for (int i = 0; i < Q; i++) {
        cout << getSum(BITree2[queries[i][2]] , queries[i][1]) - getSum(BITree2[queries[i][2]] , queries[i][0]-1)<< endl;
    }
    
    
    
    
//    int freq[] = {2, 1, 1, 3, 2, 3, 4, 5, 6, 7, 8, 9};
//    
//    int *BITree = constructBITree(trees, N);
//    cout << "Sum of elements in arr[0..5] is "
//    
//    // Let use test the update operation
//    freq[3] += 6;
//    updateBIT(BITree, N, 3, 6); //Update BIT for above change in arr[]
//    
//    cout << "\nSum of elements in arr[0..5] after update is "
//    << getSum(BITree, 5);
//    
    return 0;
}




