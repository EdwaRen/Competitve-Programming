//
//  main.cpp
//  Battle Positions
//
//  Created by - on 2017/07/13.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>

using namespace std;

int main(int argc, const char * argv[]) {
    
    long I, N, J;
    
    cin >> I >> N >> J;
    
    long myTroops[100001] = {};
    
    for (int i = 0; i < J; i++) {
        long x1, x2, k;
        cin >> x1 >> x2 >> k;
        myTroops[x1-1] += k;
        myTroops[x2] -= k;
    }
    
    long deadStations = 0;
    
    if (myTroops[0] < N) {
        deadStations++;
    }
    
    for (int i = 1; i < I; i++) {
        myTroops[i] = myTroops[i-1] + myTroops[i];
        if (myTroops[i] < N) {
            deadStations++;
        }
    }
    cout << deadStations << endl;
    
    // insert code here...
    return 0;
}
