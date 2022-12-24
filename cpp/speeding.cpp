#include <iostream>
#include <bits/stdc++.h>

using namespace std;

int main()
{
    int num=0;
    cin>>num;
    int times[num] = {};
    int distances[num] = {};
    int index = 0;
    while (num != 0) {
        cin >> times[index];
        cin >> distances[index];
        num--;
        index++;
    }
    int speed[num] = {};
    int time_dif = 0;
    int dis_dif = 0;
    for (int i = 1; i < sizeof(times); i++) 
    {
        time_dif = times[i] - times[i-1];
        dis_dif = distances[i] - distances[i-1];
        speed[i-1] = time_dif/dis_dif;
    }
    
    // int n = sizeof(speed) / sizeof(speed[0]);
    // int max = *max_element(speed,speed+n);
    cout << max;
    return 0;
}