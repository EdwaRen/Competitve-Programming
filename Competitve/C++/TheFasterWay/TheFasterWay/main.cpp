//
//  main.cpp
//  TheFasterWay
//
//  Created by - on 2017/07/13.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <math.h>

using namespace std;

long addCumulative(long a) {
    long k = a;
    for (long i = 1; i < k; i++) {
        a += i;
    }
    return a;
}

int main(int argc, const char * argv[]) {
    // insert code here...
    
    long N, R, M;
    cin >> N >> R >> M;
    long rocketStop[100001] = {};
    long customers[100001] = {};
    
    for (long i = 0; i < R; i++) {
        cin >> rocketStop[i];
    }
    for (long i = 0; i < M; i++) {
        cin >> customers[i];
    }
    
    sort(rocketStop, rocketStop+R);
    sort(customers, customers+M);
    
//    for (long i = 0; i < R; i++) {
//        cout << rocketStop[i];
//    }
//    for (long i = 0; i < M; i++) {
//        cout << customers[i];
//    }
    
    long rocketCustomers = 0;
    long busCustomers = 0;
    
    for (int i = 0; i < M; i++) {
        int j = 0;
        bool rideRocket = false;
        for (int k = j; j < R; j++) {
            if (customers[i] == rocketStop[j] && rocketCustomers < ceil(M/2)){
                rocketCustomers++;
                rideRocket = true;
                break;
            }
        }
        if (!rideRocket) {
            busCustomers++;
        }
        
    }
//    cout << "customers " << rocketCustomers << " " << busCustomers << endl;
    cout << addCumulative(rocketCustomers) + addCumulative(busCustomers) << endl;
    
    
    
//    std::cout << "Hello, World!\n";
    return 0;
}
