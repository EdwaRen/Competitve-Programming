//
//  main.cpp
//  String Searching (Hard)
//
//  Created by - on 2017/07/12.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>
#include <cstring>
#include <algorithm>

using namespace std;

int main(int argc, const char * argv[]) {
    string N;
    string A;
    
    cin >> N >> A;
    
    char *pch;
    
    pch = (char*)strstr(N.c_str(), A.c_str());
    
    if (pch - N.c_str() < 0) {
        cout << -1 << endl;
    } else {
        cout << pch - N.c_str()<< endl;
    }
    
    // insert code here...
    return 0;
}
