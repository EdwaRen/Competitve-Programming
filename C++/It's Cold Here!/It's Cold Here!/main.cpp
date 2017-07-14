//
//  main.cpp
//  It's Cold Here!
//
//  Created by - on 2017/06/19.
//  Copyright © 2017 Edward Ren-inc. All rights reserved.
//

#include <iostream>
#include <map>
#include <algorithm>

using namespace std;
int main(int argc, const char * argv[]) {
    
    map<int, string> mymap;
    
    string i = "hello world";
    int p[10001];
    int count = 0;
    while (i != "Waterloo") {
        int temp;
        string name;
        
        char tmp[101];
        scanf("%100s %d", tmp, &temp);
        name = tmp;
//        cout << "name: " << name << " temp: " << temp << endl;
        mymap[temp] = name;
        i = name;
        p[count] = (temp);
        count++;
        
    }
    sort(p, p+count);
    cout << mymap[p[0]] <<endl;

    
    return 0;
}
