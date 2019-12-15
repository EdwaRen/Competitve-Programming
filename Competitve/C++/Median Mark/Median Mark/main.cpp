//
//  main.cpp
//  Median Mark
//
//  Created by - on 2017/06/19.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <math.h>
#include <algorithm>
using namespace std;
int N;
long p[1001];

int main(int argc, const char * argv[]) {
    
    scanf("%d", &N);
    for (int x = 0; x < N; x++) {
        scanf("%ld", &p[x]);
    }
    std::sort(p, p+N);
    if (N%2 == 1) {

        int m = (N+1)/2.0;
        cout << p[m-1] << endl;

    } else {
        float x = (p[static_cast<int>((N/2.0)-1)] + p[static_cast<int>((N/2.0))])*0.5;
        cout << round(x) << endl;

    }


    
    return 0;
}
