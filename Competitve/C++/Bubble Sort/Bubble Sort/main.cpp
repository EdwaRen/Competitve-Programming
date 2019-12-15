//
//  main.cpp
//  Bubble Sort
//
//  Created by - on 2017/06/30.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>

using namespace std;

void printFunc(int arr[], int length) {
    for (int i = 0; i < length; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    int N;
    cin >> N;
    int arr[22];
    
    for (int i = 0; i < N; i++) {
        cin >> arr[i];
        
    }
    
    printFunc(arr, N);
    //Bubbling
    
    bool endThis = false;
    
    while (endThis == false) {
        endThis = true;
        for (int i = 0; i < N-1; i++) {
//            cout << "i is: " << i << ": " << N << endl;
            if (arr[i] > arr[i+1]) {
                int temp = arr[i];
                arr[i] = arr[i+1];
                arr[i+1] = temp;
                printFunc(arr, N);
                endThis = false;
            }
        }
    }
    
    
    return 0;
}
