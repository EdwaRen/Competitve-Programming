//
//  main.cpp
//  Circle Of Life
//
//  Created by - on 2017/06/30.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>

using namespace std;
long long N, T;

long long findPowerTwo(long long newT) {
    bool endThis = false;
    long long PoT = 1;
    
    while (endThis == false) {
        PoT <<= 1;
        if (PoT > newT) {
            PoT >>=1;
            return PoT;
            endThis = false;
        }
    }
    
    return PoT;
}
char AoD(char a, char b) {
//    cout << "AoD: " << a << " " << b << endl;
    if (a == '0' && b == '0') {
        return '0';
    } else if (a == '1' && b == '1') {
        return '0';
    } else {
        return '1';
    }
}

string Helix(string a, long long PoT) {
    string b;
    b = a;
    
    for (int i = 0; i < N; i++ ) {
        long long added, subtract;
        added = i + static_cast<long long>(PoT%N);
        if (added > N-1) {
            added = i - (N-(static_cast<long long>(PoT%N)));
        }
        subtract = i-(static_cast<long long>(PoT%N));
        if (subtract < 0) {
            subtract = i + (N-(static_cast<long long>(PoT%N)));
        }
        
        b[i] = AoD(a[added], a[subtract]);
//        cout << "Helix: " << b[i] << ": " << a[added] << ": " << a[subtract] << endl;
    }
    return b;
    
    
}


int main(int argc, const char * argv[]) {
    
    cin >> N;
    cin >> T;
    string a;
    cin >> a;
    
    for (int i = 0; i < N; i++) {
//        a[i] -= 64;
       
    }
    
    bool endThis = false;
    
    long long temp;
    temp = 0;
    long long PoT;
    
    
    while (endThis == false) {
        if (temp == T) {
            break;
        } else {
            PoT = findPowerTwo(T-temp);
            temp += PoT;
            a = Helix(a, PoT);
//            cout << a<< ": " << PoT << ": " << temp << endl;
        }
        
    }
    cout << a << endl;

    
    
    
    
    
    // insert code here...
    return 0;
}
