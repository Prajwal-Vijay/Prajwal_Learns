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
        int a[n];
        int k;
        cin >> k;
        int min = 100000;
        int prod = 1;
        bool entered = false;
        int no_even_4 = 0;
        for(int i = 0; i < n; i++){
            cin >> a[i];
            if(a[i]%k == 0 && !entered){
                cout << 0 << endl;
                entered = true;
            }
            prod *= a[i];
            a[i] = k - a[i] % k;
            if(a[i] < min){
                min = a[i];
            }
            if(a[i]%2 == 0){
                no_even_4 += 1;
            }
        }
        if(k == 4 && !entered){
            if(prod % 4 == 0){
                cout << 0 << endl;
            }else if(no_even_4 == 1){
                cout << 1 << endl;
            }else if(min < 2){
                cout << min << endl;
            }else{
                cout << 2 << endl;
            }
        }else if(!entered){
            cout << min << endl;
        }
    }
}