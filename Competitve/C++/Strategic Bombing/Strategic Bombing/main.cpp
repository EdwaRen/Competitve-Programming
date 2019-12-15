//
//  main.cpp
//  Strategic Bombing
//
//  Created by - on 2017/06/27.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <string>
#include <array>
#include <algorithm>
#include <iterator>
#include <cstring>

using namespace std;


int main(int argc, const char * argv[]) {

    bool end = false;
    const int charLength = 27;

    long arr[200][2];
    long lengths[27][27];
    
    for (int i = 0; i < charLength; i++) {
        for (int j = 0; j < charLength; j++) {
            lengths[i][j] = 99999;
        }
    }

    
    long count = 0;
    while (end == false) {
        string edge;
        cin >> edge;
        
        if (edge == "**") {
            end = true;
            
        } else {
            
            arr[count][0] = edge[0] - 65 ;
            arr[count][1] = edge[1] - 65;
            lengths[arr[count][0]][arr[count][1]] = 1;
            lengths[arr[count][1]][arr[count][0]] = 1;

//            cout << "edge 0 to num " << arr[count][0] << " " << arr[count][1] << endl;
            count++;
        }
        
    }
    
    
    for (int i = 0; i < charLength; i++) {
        lengths[i][i] = 0;
    }
//    for (int i = 0; i < count; i++) {
//        for (int j = 0; j < 2; j++) {
//            cout << arr[i][j] << " ";
//        }
//        cout << endl;
//    }
    int positionCount = 0;
    for (int i = 0; i < count; i++) {
        long wArr[27][27];
        
        for (int l = 0; l < charLength; l++) {
            for (int m = 0; m < charLength; m++) {
                wArr[l][m] = lengths[l][m];
            }
        }
        
        wArr[arr[i][0]][arr[i][1]] = 99999;
        wArr[arr[i][1]][arr[i][0]] = 99999;

        
        
        for (int l = 0; l < charLength; l++) {
            for (int m = 0; m < charLength; m++) {
                for (int n = 0; n < charLength; n++) {
                    if (wArr[m][n] > wArr[m][l] + wArr[l][n]) {
                        wArr[m][n] = wArr[m][l] + wArr[l][n];
                    }
                    
                }
            }
        }

//        for (int i = 0; i < count; i++) {
//            for (int j = 0; j < 2; j++) {
//                cout << arr[i][j] << " ";
//            }
//            cout << endl;
//        }
        
        if (wArr[0][1] > 9999 && wArr[1][0] > 9999) {
            positionCount++;
//            cout << "arrcounts: " <<arr[i][0] << " " << arr[i][1] << endl;
            char a = arr[i][0]+65;
            char b = arr[i][1]+65;
            cout << a << b << endl;

        }


//        array<int, count> wArr = arr;
        
        
    }
    if (positionCount != 0) {
        cout << "There are " << positionCount << " disconnecting roads." << endl;
        return 0;
    } else {
        cout << "There are 0 disconnecting roads." << endl;
        return 0;
    }
    cout << "hello" << endl;
    
    // insert code here...
    return 1;
}
