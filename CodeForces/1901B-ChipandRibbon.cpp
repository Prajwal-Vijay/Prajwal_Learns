#include <iostream>
#include <bits/stdc++.h>
#include<map>
#include<vector>
using namespace std;
int main(){
    int cases;
    cin >> cases;
    while(cases > 0){
        cases--;
        int n;
        cin >> n;
        int c[n+1];
        for(int i = 0; i < n; i ++){
            cin >> c[i];
        }
        c[n] = 1;
        long long int teleports = 0;
        for(int i = 0; i < n; i++){
            if(c[i+1] < c[i]){
            teleports += (long long int) (c[i]-c[i+1]);
            }
            if(i == n-1 && c[n-1] == 0){
                teleports += (c[i] - c[i+1]);
            }
        }
        cout << teleports << endl;
    }
}