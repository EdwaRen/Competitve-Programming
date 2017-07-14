//
//  main.cpp
//  Maximum Distance
//
//  Created by - on 2017/07/05.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>

using namespace std;

long binarySearch(long arr[],long value, long low, long high) {
    while (low <= high) {
//        cout << endl;
        
//        for (int x = low; x<= high  ;x++) {
//            cout << numElements[x] << " ";
//        }
        
        long middle = (low+high+1)/2;
        
        if (arr[middle] > value) {
            if (low == middle-1) {
                break;
            }
            low = middle-1;
        } else if (arr[middle] < value) {
            if (high == middle + 1) {
                break;
            }
            high = middle +1;
        } else if (arr[middle] == value) {
//            cout << "Value has been found! " << middle << "," << low << "," << high << endl;

            return middle;
        }
//        cout << "looping through " <<middle << " " << low << " " << high << " " <<value << endl;
        
    }
    
    return -1;
    
}

int main(int argc, const char * argv[]) {
    
    
    // insert code here...
    int N;
    
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        long T;
        cin >> T;
        
        long X[100001];
        long Y[100001];
        long previousNum = 9999999;
        
        for (int j = 0; j < T; j++) {
            cin >> X[j];
        }
        for (int j = 0; j < T; j++) {
            cin >> Y[j];
        }
        
        
        long localMax = 0;
        //Solver is here
        
        for (int j = 0; j < T; j++) {

            
            if (X[j] != previousNum) {
                previousNum = X[j];
                long firstPosition = -1;
                
                long positionCount = 0;
                
                if (Y[j] >= X[j] && T!=1) {
                    
//                    cout << i << " localmax changed " << Y[j] << " " << X[j] << endl;
                    
                    while (firstPosition == -1) {
                        firstPosition = binarySearch(Y, X[j]+positionCount, 0, T);
                        positionCount++;
//                        cout << firstPosition << " " << positionCount << " " <<i << " " << X[j] << endl;
                    }
                    
                    while (firstPosition < T-1) {
                        if (Y[firstPosition] == Y[firstPosition+1]) {
                            firstPosition++;
                        } else {
                            break;
                        }
                    }
                    
                    if (firstPosition - j > localMax) {
                        localMax = firstPosition-j;
                    }
                } else {

                }

                
            }
            
            
        }
        
        cout << "The maximum distance is " <<localMax << endl;
        
        
        
        
        
    }
    
    
    
    return 0;
}
