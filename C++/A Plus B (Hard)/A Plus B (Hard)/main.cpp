//
//  main.cpp
//  A Plus B (Hard)
//
//  Created by - on 2017/07/06.
//  Copyright © 2017 Nyce. All rights reserved.
//

#include <iostream>
#include <algorithm>
#include <iterator>
#include <string>

using namespace std;

int findWhichLarger(int num1[], int num2[], long lengthOrig, long lengthOrig2) {
    long length1 = lengthOrig;
    long length2 = lengthOrig2;

    int count1 = 0;
    int count2 = 0;
    
    if (num1[0] == -3) {
        length1--;
        count1 = 1;
    } else {
        length2--;
        count2 = 1;
    }
    
    if (length1 > length2) {
        return 2;
    } else if (length2 > length1) {
        return 3;
    } else {
        
        for (int i = 0; i < length1; i++) {
            if (num1[i + count1] > num2[i+ count2]) {
                return 2;
            } else if (num1[i + count1] < num2[i+ count2]) {
                return 3;
            }
        }
        
        
        
    }
    return 4;
    
}

int main(int argc, const char * argv[]) {
    
    int N;
    cin >> N;
    
    for (int i = 0; i < N; i++) {
        
        string numStr1, numStr2;
        cin >> numStr1 >> numStr2;
        
        int numInt1[100001] = {};
        int numInt2[100001] = {};
//        cout << numStr1 << " " << numStr1.length() << endl;
        
        for (int j = 0; j < numStr1.length(); j++) {
            numInt1[j] = numStr1[j] - '0';
        }
        for (int j = 0; j < numStr2.length(); j++) {
            numInt2[j] = numStr2[j] - '0';
        }
//        for (int j = 0; j < numStr1.length(); j++) {
//            cout << numInt1[j] << " ";
//        }
//        cout << endl;
//
//        for (int j = 0; j < numStr2.length(); j++) {
//            cout << numInt2[j] << " ";
//        }
//        cout << endl;
        
        int finalOperator = 4; //0 for two positives, 1 for 2 negatives, 2 for first negative, 3 for second negative
        if (numInt1[0] != -3 && numInt2[0] != -3) {
            finalOperator = 0;
        } else if (numInt1[0] == -3 && numInt2[0] == -3) {
            finalOperator = 1;
        } else {
            finalOperator = findWhichLarger(numInt1, numInt2, numStr1.length(), numStr2.length());
        }
        
//        reverse(begin(numInt1), end(numInt1));
//        reverse(begin(numInt2), end(numInt2));
        if (numInt1[0] == -3) {
            numInt1[0] = 0;
        }
        if (numInt2[0] == -3) {
            numInt2[0] = 0;
        }

        long largestArr = 0;
        long secondArr = 0;
        if (numStr1.length() > numStr2.length()) {
            largestArr = numStr1.length();
            secondArr = numStr2.length();
        } else {
            largestArr = numStr2.length();
            secondArr = numStr1.length();
        }
        
        int carryOver = 0;
        int answerString[100001];
        
        for (int j = 0; j < largestArr; j++) {
            
            //            if (carryOver == 0) {
            if (finalOperator == 1 || finalOperator == 0) {
//                cout << "numstr1 length - j "<< static_cast<int>(numStr1.length())  - j << endl;
                if (largestArr - j > 0 && secondArr - j > 0) {
                    answerString[j] = abs(numInt1[numStr1.length() - j -1] + numInt2[numStr2.length() - j -1] + carryOver);
//                    cout << "Answer string changed " << answerString[j] << " " << numInt1[numStr1.length() - j -1] << " " << numInt2[numStr2.length() - j -1] << " " << carryOver << endl;
                    carryOver = 0;
                    
                    if (answerString[j] >= 10) {
                        answerString[j] -= 10;
                        carryOver++;
                    }
                } else if (static_cast<int>(numStr1.length())  - j  <= 0) {
                    if (numStr2.length() - j -1 != 0 || numInt2[0] != -3) {
                        answerString[j] = abs(numInt2[numStr2.length() - j -1] + carryOver);
                        carryOver = 0;
                        if (answerString[j] >= 10) {
                            answerString[j] -= 10;
                            carryOver++;
                        }
//                        cout << "Answer- Only str2 changed " << answerString[j] << endl;
                    }

                } else if (static_cast<int>(numStr2.length())  - j <= 0) {
                    if (numStr1.length() - j -1 != 0 || numInt1[0] != -3) {

                        answerString[j] = abs(numInt1[numStr1.length() - j -1] + carryOver);
                        carryOver = 0;
                        if (answerString[j] >= 10) {
                            answerString[j] -= 10;
                            carryOver++;
                        }
//                        cout << "Answer- Only str1 changed " << answerString[j] << endl;
                    }


                }
            
            }
            
            else if (finalOperator == 2) {
                if (largestArr - j > 0 && secondArr - j > 0) {
                    answerString[j] = (numInt1[numStr1.length() - j -1] - numInt2[numStr2.length() - j -1] + carryOver);
//                    cout << "Answer string changed " << answerString[j] << " " << numInt1[numStr1.length() - j -1] << " " << numInt2[numStr2.length() - j -1] << " " << carryOver << endl;
                    carryOver = 0;
                    
                    if (answerString[j] < 0) {
                        answerString[j] += 10;
                        carryOver--;
                    }
                } else if (static_cast<int>(numStr1.length())  - j  <= 0) {
                    if (numStr2.length() - j -1 != 0 || numInt2[0] != -3) {
                        answerString[j] = (numInt2[numStr2.length() - j -1] + carryOver);
                        carryOver = 0;
                        if (answerString[j] < 0) {
                            answerString[j] += 10;
                            carryOver--;
                        }
//                        cout << "Answer- Only str2 changed " << answerString[j] << " " << numInt2[numStr2.length() - j -1] << " " << carryOver << endl;

                    }
                    
                } else if (static_cast<int>(numStr2.length())  - j <= 0) {
                    if (numStr1.length() - j -1 != 0 || numInt1[0] != -3) {
                        
                        answerString[j] = abs(numInt1[numStr1.length() - j -1] + carryOver);
                        carryOver = 0;
                        if (answerString[j] < 0) {
                            answerString[j] += 10;
                            carryOver--;
                        }
//                        cout << "Answer- Only str1 changed " << answerString[j] << " " << numInt1[numStr1.length() - j -1] << " " << numInt2[numStr2.length() - j -1] << " " << carryOver << endl;

                    }
                    
                    
                }

            }
            
            else if (finalOperator == 3) {
                if (largestArr - j > 0 && secondArr - j > 0) {
                    answerString[j] = (numInt2[numStr2.length() - j -1] - numInt1[numStr1.length() - j -1] + carryOver);
//                    cout << "Answer string changed " << answerString[j] << " " << numInt1[numStr1.length() - j -1] << " " << numInt2[numStr2.length() - j -1] << " " << carryOver << endl;
                    carryOver = 0;
                    
                    if (answerString[j] < 0) {
                        answerString[j] += 10;
                        carryOver--;
                    }
                } else if (static_cast<int>(numStr1.length())  - j  <= 0) {
                    if (numStr2.length() - j -1 != 0 || numInt2[0] != -3) {
                        answerString[j] = (numInt2[numStr2.length() - j -1] + carryOver);
                        carryOver = 0;
                        if (answerString[j] < 0) {
                            answerString[j] += 10;
                            carryOver--;
                        }
//                        cout << "Answer- Only str2 changed " << answerString[j] << " " << numInt2[numStr2.length() - j -1] << " " << carryOver << endl;
                        
                    }
                    
                } else if (static_cast<int>(numStr2.length())  - j <= 0) {
                    if (numStr1.length() - j -1 != 0 || numInt1[0] != -3) {
                        
                        answerString[j] = abs(numInt1[numStr1.length() - j -1] + carryOver);
                        carryOver = 0;
                        if (answerString[j] < 0) {
                            answerString[j] += 10;
                            carryOver--;
                        }
//                        cout << "Answer- Only str1 changed " << answerString[j] << " " << numInt1[numStr1.length() - j -1] << " " << numInt2[numStr2.length() - j -1] << " " << carryOver << endl;
                        
                    }
                    
                    
                }

            }
            
        }
        
        bool previousZero = true;
        
        if (carryOver == 1) {
            cout << carryOver ;
            previousZero = false;
        }
        
        if (finalOperator == 1 || finalOperator == 0) {
            for (int j = 0; j < largestArr; j++) {
                if (j == 0 && finalOperator == 1) {
                    cout << "-" ;
                    //                if (answerString[largestArr -1] == -3) {
                    //                    continue;
                    //                }
                }
                if (previousZero == true && answerString[largestArr-j-1] == 0 && largestArr != 1) {
                    
                } else {
                    previousZero = false;
                    cout << answerString[largestArr -j - 1] ;
                }
            }
        }
        
        else if (finalOperator == 2) {
            for (int j = 0; j < largestArr; j++) {
                if (j == 0 && numStr1[0] == '-') {
                    cout << "-" ;
                    //                if (answerString[largestArr -1] == -3) {
                    //                    continue;
                    //                }
                }
                if (previousZero == true && answerString[largestArr-j-1] == 0 && largestArr != 1) {
                    
                } else {
                    previousZero = false;
                    cout << answerString[largestArr -j - 1] ;
                }
            }
            
            
        }
        
        else if (finalOperator == 3) {
            for (int j = 0; j < largestArr; j++) {
                if (j == 0 && numStr2[0] == '-') {
                    cout << "-" ;
                    //                if (answerString[largestArr -1] == -3) {
                    //                    continue;
                    //                }
                }
                if (previousZero == true && answerString[largestArr-j-1] == 0 && largestArr != 1) {
                    
                } else {
                    previousZero = false;
                    cout << answerString[largestArr -j - 1] ;
                }
            }
            
            
        }
        
        else if (finalOperator == 4) {
            cout << 0 << endl;
        }
        cout << endl;
        
        
        
        
//        cout << "final oeprator: " << finalOperator << endl;
        
        
        
        
        
    }
    
    
    
    // insert code here...
    return 0;
}
