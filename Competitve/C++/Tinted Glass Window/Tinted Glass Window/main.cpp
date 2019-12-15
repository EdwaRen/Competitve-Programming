//
//  main.cpp
//  Tinted Glass Window
//
//  Created by - on 2017/07/11.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>
#include <vector>

using namespace std;

int main(int argc, const char * argv[]) {
    cout << "start" << endl;
    int N;
    long T;
    cin >> N >> T;
    cout << "N, T inputted" << endl;

//    vector<vector<double> > array2D;
//    long HEIGHT = 1000001;
//    long WIDTH = 1000001;
//    // Set up sizes. (HEIGHT x WIDTH)
//    array2D.resize(HEIGHT);
//    for (int i = 0; i < HEIGHT; ++i) {
//        array2D[i].resize(WIDTH);
//    }
    
    long largestX = 0;
    long largestY = 0;
    
    for (int i = 0; i < N; i++) {
        cout << "looping " << i << endl;
        long x1, y1, x2, y2, t;
        scanf("%ld", &x1);
        scanf("%ld", &y1);
        scanf("%ld", &x2);
        scanf("%ld", &y2);
        scanf("%ld", &t);

        
        if (y2 > largestY) {
            largestY = y2;
        }
        if (x2 > largestX) {
            largestX = x2;
        }
        
    }
    cout << "Done " <<largestX << " " <<largestY << endl;
    // insert code here...
    return 0;
}
