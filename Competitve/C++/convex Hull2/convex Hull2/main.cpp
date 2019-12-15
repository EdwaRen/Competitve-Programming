//
//  main.cpp
//  Convex Hull
//
//  Created by - on 2017/07/01.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <algorithm>



using namespace std;


int minDistance(int query[2001], bool sptSet[], int N) {
    //find minimum distance, adjacent nodes, sptSet == false
    int distance = 99999;
    int nextSrc = 0;
    for (int i = 0; i < N; i++) {
        if (query[i] < distance && sptSet[i] == false) {
            distance = query[i];
            nextSrc = i;
        }
    }
    return nextSrc;
}

int main() {
    int K, N, M;
    int starter, ender;
    int query[2001];
    
    
    
    cin >> K;
    cin >> N;
    cin >> M;
    int arr[2001][2001];
    bool sptSet[2001];
    //
    //    for (int i = 0; i < N; i++) {
    //        fill_n(arr[i], 2001, 0);
    //    }
    //
    //    fill_n(query, 2001, 20000);
    //    fill_n(sptSet, 2001, 0);
    //
    //    for (int i = 0; i < M; i++) {
    //        int a, b, c, d;
    //        cin >> a;
    //        cin >> b;
    //        cin >> c;
    //        cin >> d;
    //        arr[a][b] = c;
    //        arr[b][a] = c;
    //    }
    //
    //    cin >> starter;
    //    cin >> ender;
    //
    //
    //    query[starter-1] = 0;
    //
    //    for (int i = 0; i < N-1; i++) {
    //
    //
    //
    //        arr[starter-1][starter-1] = 0;
    //        sptSet[starter-1] = 1;
    //
    //        //find minimum distance, adjacent nodes, sptSet == false
    //        int m = minDistance(query, sptSet, N);
    //        for (int j = 0; j < N; j++) {
    //            if (sptSet[j] == false && arr[m][j] != 0 && query[m] != 20000 && query[m] + arr[m][j] < query[j] ) {
    //                query[j] = query[m] + arr[m][j];
    //            }
    //        }
    //        
    //        
    //        
    //    }
    //    
    //    cout << query[ender] << endl;
    //    
    //    // insert code here...
    return 0;
}
