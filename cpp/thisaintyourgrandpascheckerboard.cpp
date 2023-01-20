// https://open.kattis.com/problems/thisaintyourgrandpascheckerboard
// 1.8

#include <bits/stdc++.h>
#include <iostream>
using namespace std;

int main()
{
    bool rowCheck = true;
    int num=0;
    vector<int> consecRowVector;
    vector<int> consecColVector;
    cin >> num;
    char array[num][num] = {};
    for (int i =0; i < num; i++){
        for (int j =0; j < num; j++){
            cin >> array[i][j];
        }
    }
    
    int countB=0;
    int countW=0;
    int consec=0;
    for (int i =0; i < num; i++){
        for (int j =0; j < num; j++){
            if (array[i][j] == 'B')
                countB++;
            else
                countW++;
              
            if (j+1 < num && array[i][j+1] == array[i][j]){
                consec++;
            }else{
                consec = 0;
            }
            
            consecRowVector.push_back(consec);
        }
        consec = 0;
        
        if (countB != countW){
            rowCheck = false;
            break;
        }
        
        int maxConsec = *max_element(consecRowVector.begin(), consecRowVector.end());
        if (maxConsec >= 2){
            rowCheck = false;
            break;
        }
    }
    
    countB=0;
    countW=0;
    consec=0;
    if (rowCheck != false){
        for (int i =0; i < num; i++){
            for (int j =0; j < num; j++){
                if (array[j][i] == 'B')
                    countB++;
                else
                    countW++;
                
                if (j+1 < num && array[j+1][i] == array[j][i]){
                    consec++;
                }else{
                    consec = 0;
                }
                
                consecColVector.push_back(consec);
            }
            consec = 0;
            
            if (countB != countW){
                rowCheck = false;
                break;
            }
            
            int maxConsec = *max_element(consecColVector.begin(), consecColVector.end());
            if (maxConsec >= 2){
                rowCheck = false;
                break;
            }
        }
    }
    
    if (rowCheck == false){
        cout << '0';
    }
    else
        cout << '1';

    return 0;
}