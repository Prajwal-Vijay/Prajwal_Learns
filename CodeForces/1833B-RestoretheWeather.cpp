#include <iostream>
#include<tuple>
#include<vector>
#include <bits/stdc++.h>
#include <cmath>

using namespace std;
int main(){
    int cases = 0;
    cin >> cases;
    while(cases--){
        int n,k;
        cin >> n >> k;
        int a[n];
        int b[n];
        for(int i = 0; i < n; i++){
            cin >> a[i];
        }
        for(int i = 0; i < n; i++){
            cin >> b[i];
        }
        for(int i = 0; i < n; i++){
            for(int j = 0; j < n; j++){
                if((a[i]-b[j]) <= k){
                    
                }
            }
        }
    }
}