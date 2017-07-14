//
//  main.cpp
//  Professional Network
//
//  Created by - on 2017/06/26.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <array>

using namespace std;
int getFree(int arr[][2], int A, int n);


int main(int argc, const char * argv[]) {
    
    int n = 0;
    cin >> n;
    
    int arr[200001][2];
    
    for (int i = 0; i < n; i++) {
        cin >> arr[i][0];
        cin >> arr[i][1];
        
    }
    
    int A = 0;
    A = getFree(arr, 0, n);
    sort(arr, arr + sizeof(arr) / sizeof(arr[0]));
    
    
    for (int i = 0; i < n; i++) {
        cout << arr[i][0] << " " << arr[i][1] << endl;
    }
   
    
    
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
int getFree (int arr[][2], int A, int n) {
    for (int i = 0; i < n; i++) {
        if (arr[i][0] <= A) {
            n--;
            A +=1;
            arr[i][0] = 0;
            i = 0;
        }
    }
    
    return A;
    
}
