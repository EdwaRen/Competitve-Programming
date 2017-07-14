//
//  main.cpp
//  Blood Distribution
//
//  Created by - on 2017/06/27.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
using namespace std;

int main(int argc, const char * argv[]) {
    
    
    int s[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    int n[8] = {0, 0, 0, 0, 0, 0, 0, 0};
    int p = 0;

    for (int i = 0; i < 8; i++) {
        cin >> s[i];
    }
    for (int i = 0; i < 8; i++) {
        cin >> n[i];
    }
    for (int i = 0; i < 8; i++) {
        
        if (s[i] >= n[i]) {
            s[i] = s[i] - n[i];
            p = p + n[i];
            n[i] = 0;
        } else {
            n[i] = n[i] - s[i];
            p = p + s[i];
            s[i] = 0;
        }
        
        
    }
 
    
    for (int i = 1; i < 8; i++) {
        
        if (n[i] > 0 and i!= 5 and i!= 4) {
            if (i%2 != 0) {
                for (int j = 1; j < i; j+=2) {
                    
                    if (s[j] >= n[i]) {
                        s[j] = s[j] - n[i];
                        p = p+ n[i];
                        n[i] = 0;
                    } else {
                        n[i] = n[i] - s[j];
                        p = p + s[j];
                        s[j] = 0;
                    }
                    
                }
                for (int j = 0; j < i; j+=2) {
                    
                    if (s[j] >= n[i]) {
                        s[j] = s[j] - n[i];
                        p = p+ n[i];
                        n[i] = 0;
                    } else {
                        n[i] = n[i] - s[j];
                        p = p + s[j];
                        s[j] = 0;
                    }
                    
                }
            } else {
                
                for (int j = 0; j < i; j+=2) {
                
                    if (s[j] >= n[i]) {
                        s[j] = s[j] - n[i];
                        p = p+ n[i];
                        n[i] = 0;
                    } else {
                        n[i] = n[i] - s[j];
                        p = p +  s[j];
                        s[j] = 0;
                    }
                }
            }
                
//            cout << "added for i = " << i << " p is now " << p << endl;
//            for (int i = 0; i < 8; i++) {
//                cout << s[i] << " ";
//            }
//            cout << endl;
//            for (int i = 0; i < 8; i++) {
//                
//                cout << n[i] << " ";
//            }
//            cout << endl;
//            cout << endl ;

        } else if (n[i] > 0 && i == 5) {
            for (int j = 1; j < 2; j++) {
                
                if (s[j] >= n[i]) {
                    s[j] = s[j] - n[i];
                    p = p+ n[i];
                    n[i] = 0;
                } else {
                    n[i] = n[i] - s[j];
                    p = p + s[j];
                    s[j] = 0;
                }
                if (j == 2) {
                    j = j+2;
                }
                
            }
            
            for (int j = 0; j < i; j++) {
                
                if (s[j] >= n[i]) {
                    s[j] = s[j] - n[i];
                    p = p+ n[i];
                    n[i] = 0;
                } else {
                    n[i] = n[i] - s[j];
                    p = p + s[j];
                    s[j] = 0;
                }
                if (j == 2) {
                    j = j+2;
                }
                
            }
            
        } else if (n[i] > 0 && i == 4) {
            
            for (int j = 0; j < i; j+=4) {
                
                if (s[j] >= n[i]) {
                    s[j] = s[j] - n[i];
                    p = p+ n[i];
                    n[i] = 0;
                } else {
                    n[i] = n[i] - s[j];
                    p = p + s[j];
                    s[j] = 0;
                }
                
                
            }
            
        }

    }
    cout << p << endl;
    
    
    
    
    
    // insert code here...
    return 0;
}
