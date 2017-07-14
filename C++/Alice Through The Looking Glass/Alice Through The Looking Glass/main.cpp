//
//  main.cpp
//  Alice Through The Looking Glass
//
//  Created by - on 2017/07/10.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>
#include <cmath>

using namespace std;

bool zoom(int x, int y, int m) {
    
    int newX = floor(x/(pow(5, m-1)));
    int newY = floor(y/(pow(5, m-1)));
//    cout << "x,y " << x << " " << y << " " << m << " " << newX << " " << newY << endl;
   
    
    if (m == 1) {
        if (newX == 1 && newY == 0) {
            return true;
        } else if (newX == 2 && newY == 0) {
            return true;
        } else if (newX == 2 && newY == 1) {
            return true;
        } else if (newX == 3 && newY == 0) {
            return true;
        } else {
            return false;
            
        }
    }
    if (newX == 1 && newY == 0) {
        return true;
    } else if (newX == 2 && newY == 0) {
        return true;
    } else if (newX == 2 && newY == 1) {
        return true;
    } else if (newX == 3 && newY == 0) {
        return true;
    } else if (m!=1 && newX == 1 && newY == 1) {
//            return true;
        } else if (m!=1 && newX == 2 && newY == 2) {
//            return true;
        } else if (m!=1 && newX == 3 && newY == 1) {
//            return true;
        } else {
            return false;
        }
//    }
    
    
    
    int putX = 0;
    putX =x%(static_cast<int>(pow(5, m-1)) );
    if (putX == x) {
        putX = 0;
    }
    int putY = 0;
    putY = y%(static_cast<int>(pow(5, m-1)) );
    if (putY == y) {
        putY = 0;
    }
    
    return zoom(putX,putY, m-1);
}


int main(int argc, const char * argv[]) {
    // insert code here...
    
//    cout << 5%5 << " " << 6%5 << " " << 4%5 << endl;
    
    int N;
    cin >> N;
    
    
    for (int i = 0; i < N; i++) {
//        cout << "New specimen " << endl;
        int m, x, y;
        cin >> m >> x >> y;
        
        if (zoom(x, y, m) == 0) {
            cout << "empty" << endl;
        } else {
            cout << "crystal" << endl;
        }
        
        
        
    }
    
    return 0;
}
