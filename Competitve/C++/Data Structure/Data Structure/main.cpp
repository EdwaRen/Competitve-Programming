//
//  main.cpp
//  Data Structure
//
//  Created by - on 2017/07/02.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <map>
#include <algorithm>
#include <vector>
#include <functional>
#include <cstring>
//#include <string.h>



using namespace std;

long long N, M;

long long stableDataY[100001];
long long stableDataX[100001];





void constructPyramid(long long columnSize, long long i) {
 
}

int main(int argc, const char * argv[]) {
    
    
    memset(stableDataX, 1000000001, sizeof(stableDataX));
    
    
    
    cin >> N >> M;
    
//        map <int, int> myData1;
//        myData1[1] = 100;
//        myData1[2] = 200;
//        cout << myData1[3] << " mapdata"<< endl;
    map <long, long> myData;
    
    
    for (long i = 0; i < M; i++) {
        stableDataX[i] = 1000000001;
    }
    for (long long i = 0; i < M; i++) {
        long long a, b;
        cin >> b >> a;

        if ((b < myData[a] || myData[a] == 0)) {
            stableDataX[i] = a;
            stableDataY[i] = b;
//            cout << "My data set: stabledatax " << stableDataX[i] << " stabledatay " << stableDataY[i] << " mydata[sbx] " << myData[stableDataX[i]] << endl;
            myData[stableDataX[i]] = stableDataY[i];
        }
    }
    
    sort(begin(stableDataX), end(stableDataX));
    
    long long totalSum = 0;
    long long currentHeight = 0;
    long dataCount = 0;
    

    
    for (long long i = 0; i < N; i++) {
        if (stableDataX[dataCount]-1 == i) {
//            cout << "datacount is equal to i" << endl;
            long long columnSize = N-myData[stableDataX[dataCount]] + 1;
//                    cout << "column size for i " << i << " = " << columnSize << " " << myData[stableDataX[dataCount]] << endl;
            if (columnSize > currentHeight) {
//                cout << "!!! current height changed " << columnSize << " previous height: " << currentHeight << endl;
                currentHeight = columnSize;
            }
            dataCount++;
            
            while (stableDataX[dataCount] == stableDataX[dataCount-1]) {
                dataCount++;
            }
            

        }
//        cout << "current height: " <<currentHeight << endl;
        if (currentHeight > 0) {
            totalSum += currentHeight;
            currentHeight -=1;
        }
        
    }
//    long long sum = 0;
//    for (long long i = 0; i < N; i++) {
//        //        cout << pyramid[i] << " ";
//        sum += pyramid[i];
//    }
//    //    cout << endl;
    cout << totalSum << endl;
    
    
    
    return 0;
}
