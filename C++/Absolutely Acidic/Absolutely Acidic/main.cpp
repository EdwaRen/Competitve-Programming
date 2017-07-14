//
//  main.cpp
//  Absolutely Acidic
//
//  Created by - on 2017/07/02.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main(int argc, const char * argv[]) {
    
    long N;
    cin >> N;
    int readings[2001]; //counts frequency of sensor readings for each reading possible
    
    memset(readings, 0, sizeof(readings));
    
    for (int i = 0; i < N; i++) {
        int a;
        cin >> a;
        readings[a]++;
    }
    
    //finding largest
    long largest = 0;
    long secondLargest = 0;
    
    for (int i = 0; i < 2001; i++) {
        
        if (readings[i] > largest) {
            largest = readings[i];
        }
//        cout<< "largestand and secondLarge " << largest << " " << secondLargest << endl;

        if (readings[i] < largest && readings[i] > secondLargest) {
            secondLargest = readings[i];
        }
        
    }
    
    long smallestLarge = 2000001;
    long largestLarge = 0;
    
    for (int i = 0; i < 2001; i++) {
        if (readings[i] == largest and i < smallestLarge) {
            smallestLarge = i;
        }
        if (readings[i] == largest and i > largestLarge) {
            largestLarge = i;
        }
    }
//    cout<< "largestLarge and smallest Large " << largestLarge << " " << smallestLarge << endl;
//    cout<< "largestand and secondLarge " << largest << " " << secondLargest << endl;
//
    if (smallestLarge != largestLarge) {
        cout<<  abs(largestLarge - smallestLarge) << endl;
    } else {
        
        long smallestSecondLarge = 2000001;
        long largestSecondLarge = 0;
        
        for (int i = 0; i < 2001; i++) {
            if (readings[i] == secondLargest and i < smallestSecondLarge) {
                smallestSecondLarge = i;
            }
            if (readings[i] == secondLargest and i > largestSecondLarge) {
                largestSecondLarge = i;
            }
        }
        
        if (abs(largestLarge-largestSecondLarge) > abs(largestLarge-smallestSecondLarge)) {
            cout <<abs(largestLarge-largestSecondLarge) << endl;
        } else {
             cout <<abs(largestLarge-smallestSecondLarge) << endl;
        }
        
    }
    
    
    
    
    return 0;
}
