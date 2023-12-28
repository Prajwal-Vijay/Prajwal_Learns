#include <iostream>
#include<tuple>
#include<vector>
#include <bits/stdc++.h>
#include <cmath>

using namespace std;
int main(){
    int cases;
    cin >> cases;
    while(cases--){
        int xA, yA;
        cin >> xA;
        cin >> yA;
        int xB, yB;
        cin >> xB;
        cin >> yB;
        int xC, yC;
        cin >> xC;
        cin >> yC;
        int sABx = xB - xA, sABy = yB - yA;
        int sACx = xC - xA, sACy = yC - yA;
        int x = 0, y = 0;
        if((sABx >= 0 && sACx >=0) ||(sABx <= 0 && sACx <= 0)){
            x = min(abs(sABx),abs(sACx));
        }
        if((sABy <= 0 && sACy <=0) ||(sABy >= 0 && sACy >= 0)){
            y = min(abs(sABy),abs(sACy));
        }
        cout << (x+y+1) << endl;
    }
}