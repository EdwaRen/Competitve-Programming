//
//  main.cpp
//  Deforestation
//
//  Created by - on 2017/06/19.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
using namespace std;
int N, Q;
long long k[1000001];
int main()
{
    scanf("%d", &N);
    for (int i = 1; i <= N; i++)
    {
        int m;
        scanf("%d", &m);
        k[i] = k[i-1] + m;
    }
    scanf("%d", &Q);
    for (int i = 0 ; i < Q; i++)
    {
        int a, b;
        scanf("%d%d", &a, &b);
        b++;
        printf("%lld\n", k[b] - k[a]);
    }
}
