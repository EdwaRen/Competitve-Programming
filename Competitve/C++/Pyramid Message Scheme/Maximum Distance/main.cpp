//
//  main.cpp
//  Maximum Distance
//
//  Created by - on 2017/07/02.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <cstring>

using namespace std;

int main(int argc, const char * argv[]) {
//    cout << "Hi" << endl;

    int N;
    cin >> N;
//    cout << "Hi" << endl;

    for (int i = 0; i < N; i++) { //For each set of coordinates (only 1 set in the example)
        int T;
        cin >> T;
        
        int myCount = 0;
        string nodesKey[2001];
        
        int nodesNum[2001];
        string strNodeOg;
        cin >> strNodeOg;
        
        const int distLength = 100;
        
        int dist[distLength][distLength];
        
        
        for (int j = 0; j < distLength; j++) {
            for (int k = 0; k < distLength; k++) {
                dist[j][k] = 2000;
            }
        }
        
        nodesNum[0] = 0;
        nodesKey[myCount] = strNodeOg;
        myCount++;
        
        int homeNum = 0;
        bool onlOnce = true;
//        cout << "Hi" << endl;
        for (int j = 1; j < T; j++) {
            
            string strNode;
            cin >> strNode;
            
            
            bool isOriginal = true;
            for (int k = 0; k < myCount; k++) {
                if (nodesKey[k] == strNode) {
                    
                    nodesNum[j] = k;

                    isOriginal = false;
                
                }
            }
            
            if (isOriginal == true) {
                nodesKey[myCount] = strNode;
                nodesNum[j] = myCount;
                myCount++;
                
                
               
                

            }
            if (j == T-1) {
                for (int c = 0; c < T; c++) {
                    if (nodesKey[c] == strNode) {
//                        cout << "set homenum " <<  strNode << " " << c << " " << endl;
                        homeNum = c;
                        
                        for (int p = 0; p < T; p++) {
//                            cout << nodesKey[p] << endl;
                        }
                        
                        
                        break;
                    }
                }
            }
            
            
            
        }
        
        for (int j = 0; j < T-1; j++) {
            dist[nodesNum[j]][nodesNum[j+1]] = 1;
            dist[nodesNum[j+1]][nodesNum[j]] = 1;

        }
        
        for (int l =0; l < myCount; l++) {
            for (int m = 0; m < myCount; m++) {
                for (int n = 0 ; n < myCount; n++) {
                    if (dist[m][n] > dist[m][l] + dist[l][n]) {
                        dist[m][n] = dist[m][l] + dist[l][n];
                    }
                    
                }
            }
        }
        
        int maxSum = 0;
//        cout << "homeNum " << homeNum << endl;
        
        for (int j = 0; j < myCount; j++) {
            for (int k = 0; k < myCount; k++) {
                if (dist[j][k] > maxSum && dist[j][k] != 2000 && (j == homeNum and k != homeNum)) {
//                    cout << "j and k " << j << " " << k << " " << nodesKey[k] << " " << nodesKey[j] << " " << homeNum << endl;
                    maxSum = dist[j][k];
                }
            }
        }
//        cout << maxSum << endl;
        cout << T*10 - maxSum*20 << endl;
        
        
        
        
//        for (int j = 0; j < T; j++) {
//            cout << nodesNum[j] << " ";
//        }
//        cout << endl;
        
        
        
        
    }
    
    
    
    // insert code here...
    return 0;
}
