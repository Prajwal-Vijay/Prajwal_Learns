#include <iostream>
#include <bits/stdc++.h>
#include<map>
#include<vector>
using namespace std;
int vol(int stripes[], int n){
    int vol = 0;
    int water_height = stripes[0];
    for(int i = 1; i < n-1; i++){
        if(stripes[i]<water_height){
            vol += (water_height-stripes[i]);
        }
        else{
            water_height=stripes[i];
        }
    }
}
void update(int stripes[], int l, int r, int n){
    for(int i = l; i <= r; i++){
        stripes[i]++;
    }
}
int main(){
    int cases;
    cin >> cases;
    while(cases > 0){
        cases--;
        int n, q;
        cin >> n >> q;
        int stripes[n];
        for(int i = 0; i < n; i++){
            cin >> stripes[i];
        }
        cout << vol(stripes ,n) << endl;
        for(int i = 0; i < q; i++){
            int l, r;
            cin >> l >> r;
            update(stripes, l, r, n);
            cout << vol(stripes, n) << endl;
        }
    }
}
