//
//  main.cpp
//  Intercept
//
//  Created by - on 2017/06/30.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <cmath>

using namespace std;

int main(int argc, const char * argv[]) {
    
    int N, d;
    cin >> N;
    for (int i = 0; i < N; i++) {
        cin >> d;
        
        int arr[12];
        long coEff[12];
        long coEff2[12];
        
        for (int j = 0; j < 12; j++) {
            coEff[j] = 0;
            coEff2[j] = 0;
            arr[j] = 0;
        }
        
        for (int j = 0; j < d; j++) {
            cin >> arr[j];
        }
        long long posX, posY;
        cin >> posX;
        cin >> posY;
        
        

        coEff[0] = 1;
        coEff[1] = -(arr[0]+arr[1]);
        coEff[2] = (-arr[0]*-arr[1]);
        
        for (int k = 0; k < 12; k++) {
            coEff2[k] = coEff[k];
        }
        
        for (int j = 2; j < d; j++) { //For each (x-1) after the original 2
            for (int k = 0; k < 12; k++) {
                coEff2[k] = coEff[k];
            }
            
            for (int k = 0; k < j+2; k++) { //multiplying every array by the xth root
                if (k != 0) {
                    coEff2[k] = coEff[k-1]*(-arr[j]) + coEff[k];
                } else {
                    coEff2[k] = coEff[k];

                }
            }
            for (int k = 0; k < 12; k++) {
                coEff[k] = coEff2[k];
            }
         
            
        }
//        for (int j = 0; j < d+1 ; j++) {
//            
//            cout << coEff2[j] << " ";
//            
//        }
        
        long factor = 1;
        long long xCarry = 0;
       
        for (int j = 0; j < d; j++) {
            xCarry += pow(posX, d-j)*coEff2[j];
            
        }
        xCarry+= coEff2[d];
        if (xCarry == 0) {
            factor = 1;
        } else {
            factor = (posY/xCarry);
        }
//        cout << "factor: "<< factor << " xcary: " << xCarry << " y "<< posY << endl;
        
        for (int j = 0; j < d+1 ; j++) {
            coEff2[j] = coEff2[j]*factor;
            cout << coEff2[j] << " ";
            
        }
        cout << endl;
        
        
    }
    
    
    
    // insert code here...
    return 0;
}
