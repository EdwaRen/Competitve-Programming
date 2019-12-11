//
//  main.cpp
//  Chances Of Winning
//
//  Created by - on 2017/07/11.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>

using namespace std;
void resetArrays(int scoresNew[], int scoresOg[], bool gamesPlayedNew[][4], bool gamesPlayedOg[][4]);
int findPaths(int scores[], bool gamesPlayed[][4], int t1, int t2, int winner, int game);



int T;
int G;
int counterS = 0;
int totalCount = 0;
int scoreData[100000][4];


int main(int argc, const char * argv[]) {
    
    // insert code here...

   
    cin >> T >> G;
    
    bool gamesPlayed[4][4];
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            gamesPlayed[i][j] = false;
        }
    }
    
    gamesPlayed[0][0] = true;
    gamesPlayed[1][1] = true;
    gamesPlayed[2][2] = true;
    gamesPlayed[3][3] = true;






    
    int scores[4] = {0, 0, 0, 0};
    
    for (int i = 0; i < (G); i++) {
        
        int t1, t2, s1, s2;
        cin >> t1 >> t2 >> s1 >> s2;
        gamesPlayed[t1-1][t2-1] = true;
        gamesPlayed[t2-1][t1-1] = true;
//        cout << "inputs " << t1 << " " << t2 << " " << s1 << " " << s2 << endl;
        if (s1 > s2) {
            scores[t1-1] += 3;
        } else if (s2 > s1) {
            scores[t2-1] += 3;
        } else {
            scores[t1-1] += 1;
            scores[t2-1] += 1;
        }
        
    }
//    cout << scores[0] << scores[1] << scores[2] << scores[3] << endl;
    
    int a = 0;
    
//    for (int z = 0; z < 4; z++) {
//        for (int y = 0; y < 4; y++) {
//            cout << gamesPlayed[z][y] << " ";
//        }
//        cout << endl;
//    }
    
    for (int i = 1; i < 4; i++) {
        for (int j = 0; j < i; j++) {
//            cout << "initial j and i " << j << " " << i << endl;

            if (gamesPlayed[j][i] == false) {
                
                bool gamesPlayed2[4][4];
                for (int z = 0; z < 4; z++) {
                    for (int y = 0; y < 4; y++) {
                        gamesPlayed2[z][y] = gamesPlayed[z][y];
                    }
                }
//                cout << "gameplay changed " << i << " " << j << endl;
                gamesPlayed2[j][i] = true;
//                
//                for (int z = 0; z < 4; z++) {
//                    for (int y = 0; y < 4; y++) {
//                        cout << gamesPlayed2[z][y] << " ";
//                    }
//                    cout << endl;
//                }
                
                int scores2[4] = {scores[0], scores[1], scores[2], scores[3]};
                a+=findPaths(scores2, gamesPlayed2, i, j, i, G+1);
                cout << a << endl;
                
                resetArrays(scores2, scores, gamesPlayed2, gamesPlayed);
                gamesPlayed2[j][i] = true;
                a += findPaths(scores2, gamesPlayed2, i, j, j, G+1);
                cout << a << endl;

                resetArrays(scores2, scores, gamesPlayed2, gamesPlayed);
                gamesPlayed2[j][i] = true;
                a += findPaths(scores2, gamesPlayed2, i, j, 5, G+1);
                cout << "final " << a << endl;


            }
        }
    }
//    int a = findPaths(scores, gamesPlayed, 0, 1, 0, G);

    cout << counterS <<  " " << totalCount <<endl;
    
//    for (int i = 0; i < counterS; i++) {
//        for (int j = 0; j < 4 ; j++) {
//            cout << scoreData[i][j] <<  " " ;
//        }
//        cout << endl;
//    }
//    
//    
    return 0;
}





int findPaths(int scores[], bool gamesPlayed[][4], int t1, int t2, int winner, int game) {
    int mySum = 0;
    
    if (winner == 5) {
        scores[t1] += 1;
        scores[t2] += 1;
    } else {
//        cout << "winner t1 t2 " << winner << " " << t1 << " " << t2 << endl;
        scores[winner] += 3;
    }
//    cout << "game " << game << endl;
    if (game == 6) {
        int largestScore = 0;
        int largestIndex = 1234;
        for (int i = 0; i < 4; i++) {
            if (scores[i] > largestScore) {
                largestScore = scores[i];
                largestIndex = i;
            } else if (scores[i] == largestScore) {
                largestIndex = 1234;
            }
        }
        if (largestIndex == T-1) {
            totalCount++;

            bool scoreMatch = false;
            for (int i = 0; i < counterS ; i++) {
                if (scores[0] == scoreData[i][0] && scores[1] == scoreData[i][1] && scores[2] == scoreData[i][2] && scores[3] == scoreData[i][3]) {
                    scoreMatch = true;
                    break;
                }
            }
            
            cout << "Got it: " << scores[0] << " " << scores[1] << " " << scores[2] << " " << scores[3] << " " << largestScore <<  endl;
//            cout << "Got it teams: " << t1 << " " << t2 << endl;

            if (scoreMatch == false) {
                
                scoreData[counterS][0] = scores[0];
                scoreData[counterS][1] = scores[1];
                scoreData[counterS][2] = scores[2];
                scoreData[counterS][3] = scores[3];
                counterS++;
                
                return 1;
            } else {
                return 0;
            }
        } else {
//            cout << "Dead: " << scores[0] << " " << scores[1] << " " << scores[2] << " " << scores[3] << " " << endl;

            return 0;
        }
    } else {
//        for (int z = 0; z < 4; z++) {
//            for (int y = 0; y < 4; y++) {
//                cout << gamesPlayed[z][y] << " ";
//            }
//            cout << endl;
//        }
        bool onlyOnce = true;
        for (int i = 1; i < 4; i++) {
            for (int j = 0; j < i; j++) {
//                cout << "j and i " << j << " " << i << endl;
                if (gamesPlayed[j][i] == false && onlyOnce == true) {
                    onlyOnce = false;
                    bool gamesPlayed2[4][4];
                    for (int z = 0; z < 4; z++) {
                        for (int y = 0; y < 4; y++) {
                            gamesPlayed2[z][y] = gamesPlayed[z][y];
                        }
                    }
                    gamesPlayed2[j][i] = true;

                    int scores2[4] = {scores[0], scores[1], scores[2], scores[3]};
                    mySum += findPaths(scores2, gamesPlayed2, i, j, i, game+1);
                    
                    resetArrays(scores2, scores, gamesPlayed2, gamesPlayed);
                    gamesPlayed2[j][i] = true;
                    mySum += findPaths(scores2, gamesPlayed2, i, j, j, game+1);
                    
                    resetArrays(scores2, scores, gamesPlayed2, gamesPlayed);
                    gamesPlayed2[j][i] = true;
                    mySum += findPaths(scores2, gamesPlayed2, i, j, 5, game+1);
                    
                    
                }
            }
        }
        return mySum;
        
    }
    
    
}

void resetArrays(int scoresNew[], int scoresOg[], bool gamesPlayedNew[][4], bool gamesPlayedOg[][4]) {
    for (int i = 0; i < 4; i++) {
        scoresNew[i] = scoresOg[i];
    }
    
    for (int i = 0; i < 4; i++) {
        for (int j = 0; j < 4; j++) {
            gamesPlayedNew[i][j] = gamesPlayedOg[i][j];
        }
    }
}












