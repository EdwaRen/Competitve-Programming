

#include <iostream>
#include <cstring>
#include <string>
#include <vector>
#include <queue>
#include <functional>

using namespace std;

int hullThick, numIsland, numRoutes;
int starter, ender;


struct Path {
    int dest, time, hullDestruct;
};

struct Island {
    vector<Path> paths;
};

Island islands[2001];

//Create the routes (after reading input)

void addPath(int a, int b, int c, int d) {
    Path myPath = Path();
    myPath.dest = b;
    myPath.time = c;
    myPath.hullDestruct = d;
    islands[a].paths.push_back(myPath);
}

typedef pair<int, int> pii;

unsigned int distanceWithHullDestruct[2001][201]; //The value stored in this 2d array is the time taken. The time taken is for a possible hull of length 0-200
bool islandInQueue[2001];

priority_queue<pii, vector<pii>, greater<pii> > islandQueue;

void setDistance(int a, int b, unsigned int c) {
    distanceWithHullDestruct[a][b] = c;
}

unsigned int getDistance(int a, int b) {
    return distanceWithHullDestruct[a][b];
}

void solver() {
    
    memset(distanceWithHullDestruct, 0x3F, sizeof(distanceWithHullDestruct));
    memset(islandInQueue, false, sizeof(islandInQueue));
    
    islandQueue.push(make_pair(0, starter));
    
    setDistance(starter, 0, 0);
    islandInQueue[starter] = true;
    
    while (islandQueue.empty() == false) {
        int currentIsland = islandQueue.top().second;
        islandInQueue[currentIsland] = false;
        islandQueue.pop();
        
        for (Path currentPath: islands[currentIsland].paths) {
            
            
            
            for (int hLength = 0; hLength < hullThick - currentPath.hullDestruct; hLength++) {
                
                unsigned int alternateDistance = getDistance(currentIsland, hLength) + currentPath.time;
                
                if (alternateDistance < getDistance(currentPath.dest, currentPath.hullDestruct + hLength)) {
                    setDistance(currentPath.dest, currentPath.hullDestruct + hLength, alternateDistance);
                    
                    if (islandInQueue[currentPath.dest] == false) {
                        islandInQueue[currentPath.dest] = true;
                        islandQueue.push(make_pair(alternateDistance, currentPath.dest));
                        
                    }
                }
                
                
                
            }
            
            
            
            
            
        }
    }
    
    
    
}

int main() {
    
    cin >> hullThick >> numIsland >> numRoutes;
    
    for (int i = 0; i < numRoutes; i++) {
        int a, b, c, d;
        cin >> a >> b >> c >> d;
        addPath(a, b, c, d);
        addPath(b, a, c, d);
    }
    
    cin >> starter >> ender;
    solver();
    
    int fastRoute = 0x3F3F3F3F;
    
    for (int i = 0; i < hullThick; i++) {
        fastRoute = min( (int)distanceWithHullDestruct[ender][i], fastRoute);
    }
    
    if (fastRoute == 0x3F3F3F3F) {
        cout << "-1" << endl;
    } else {
        cout << fastRoute << endl;
    }
    
    
    
    
    return 0;
}
