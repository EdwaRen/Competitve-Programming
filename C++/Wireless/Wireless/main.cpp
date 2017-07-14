//
//  main.cpp
//  Wireless
//
//  Created by - on 2017/07/10.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>
#include <vector>
#include <cmath>
using std::vector;

using namespace std;

int main(int argc, const char * argv[]) {
    // insert code here...
    
    int M, N, K;
    
    cin >> M >> N >> K;
    
//    vector<vector<vector<double> > > arrInputs;
//    arrInputs.resize(M);
//    for (int i = 0; i < M; ++i) {
//        arrInputs[i].resize(N);
//        
//        for (int j = 0; j < N; ++j) {
//            arrInputs[i][j].resize(2);
//        }
//    }
    
    int arrInputs[30001][4];

    
    vector<vector<double> > totalBitrates;
    totalBitrates.resize(M);
    for (int i = 0; i < M; ++i) {
        totalBitrates[i].resize(N);
    }

    
    
    
//    int* circleRadius = new int[M * N];
//    int* circleBitrate = new int[M * N];
//
//    int* totalBitrates = new int[M * N];

    
    for (int i = 0; i < K; i++) {
        int x, y, r, b;
        cin >> x >> y >> r >> b;
        arrInputs[i][0] = y-1;
        arrInputs[i][1] = x-1;
        arrInputs[i][2] = r;
        arrInputs[i][3] = b;


    }
    
    
    for (int i = 0; i < K; i++) {
        
        //Find left-most point
        int x, y, r, b;
        y = arrInputs[i][0];
        x = arrInputs[i][1];
        r = arrInputs[i][2];
        b = arrInputs[i][3];


//        cout << "On circle no. " << i << endl;

        
        for (int j = r; j >= 0  ; j--) {
            bool fitOnce = false;
            int trueJ = 0;
            int trueK = 0;
            bool added = false;

            for (int k = r; k >= 0; k--) {
                
                if (sqrt(((k) * (k)) + ((j) * (j))) <= r) {
                    if (fitOnce == false) {
                        trueJ = j;
                        trueK = k;
                    }
                    fitOnce = true;

//                    cout << "changing left/right circle rate k/j "<< k << " " << j << " " << y << " " << x << endl;
                    if (y-(j) >= 0 && x-k >= 0 && y-j < M && x-k < N) {
                        totalBitrates[y-(j)][x-k] += b;
//                        cout << "pos1 bitrate changed for " << totalBitrates[y-j][x-k] << "at y, x "<< y-j << " " << x-k << endl;
                        added = true;
                        
                        if (y-trueJ >= 0 && x+trueK+1 >= 0 && y-trueJ < M && x+trueK+1 < N) {
                            
                            totalBitrates[y-trueJ][x+trueK+1] -= b;
//                            cout << "neg1 bitrate changed for " << totalBitrates[y-trueJ][x+trueK+1] << "at y, x "<< y-trueJ << " " << x+trueK+1 << endl;
                            
                        }
                    }
                    if (y+j >= 0 && x-k >= 0 && y+j < M &&  x-k < N && j!= 0) {
                        totalBitrates[y+j][x-k] += b;
//                        cout << "pos2 bitrate changed for " << totalBitrates[y+j][x-k] << "at y, x "<< y+j << " " << x-k << endl;
                        added = true;
                        
                        if (y+trueJ >= 0 && x+trueK+1 >= 0 && y+trueJ < M && x+trueK+1 < N) {
                            totalBitrates[y+trueJ][x+trueK+1] -= b;
//                            cout << "neg2 bitrate changed for " << totalBitrates[y+trueJ][x+trueK+1] << "at y, x "<< y+trueJ << " " << x+trueK+1 << endl;
                            
                        }
                    }
//                    cout << "\nDiagram " << endl;
//                    for (int i = 0; i < M; i++) {
//                        for (int j = 0; j < N; j++) {
//                            cout << totalBitrates[i][j] << " ";
//                        }
//                        cout << endl;
//                    }
//                    cout << "\nDiagram " << endl;

                    if (added == true) {
                        break;
                    }

                }
            }
            
        }
        
        
    }
//    for (int i = 0; i < M; i++) {
//        for (int j = 0; j < N; j++) {
//            cout << totalBitrates[i][j] << " ";
//        }
//        cout << endl;
//    }
    
    int best = totalBitrates[0][0];
    int bestCount = 1;
    for (int i = 0; i < M; i++) {
        for (int j = 1; j < N; j++) {
            totalBitrates[i][j] += totalBitrates[i][j-1];
            if (totalBitrates[i][j] > best) {
                best = totalBitrates[i][j];
                bestCount = 1;
            } else if (totalBitrates[i][j] == best) {
//                cout << i << " " << j << endl;
                bestCount++;
            }
        }
    }
    cout << best << endl;
    cout << bestCount << endl;
    
//    for (int i = 0; i < M; i++) {
//        for (int j = 0; j < N; j++) {
//            cout << totalBitrates[i][j] << " ";
//        }
//        cout << endl;
//    }
//    
    
    return 0;
}
