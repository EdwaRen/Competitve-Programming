//
//  main.cpp
//  Pinball Ranking
//
//  Created by - on 2017/07/13.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    vector<int> myArray[9];
    for (int i = 0; i < 9; i++) {
        myArray[i] = 6;
    }
    myArray.insert(myArray.begin()+5, 100);
    
    
    // insert code here...
    return 0;
}
