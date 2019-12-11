//
//  main.cpp
//  PalinDrone
//
//  Created by - on 2017/07/13.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>
#include <math.h>

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    unsigned long long N = 0;
    cin >> N;
    unsigned long long totalSum = 0;
    if ( N < 25) {
        for (int i = 1; i <= N; i++) {
            
            unsigned long long power = ceil(i/2.0)-1;
            //        cout << "power " << power << " " << N/2<< endl;
            totalSum += pow(10, power)*9;
            //        cout << "totalsum " << totalSum << endl;
            
        }
        
        cout << totalSum % 1000000000 << endl;
    } else {
        cout << "999999998" << endl;
    }
    
    return 0;
}
