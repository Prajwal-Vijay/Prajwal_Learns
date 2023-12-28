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
        long a[n], b[n];
        long long int sum_a = 0, sum_b = 0;
        long long int min_a = LONG_MAX, min_b = LONG_MAX;
        for(int i = 0; i < n; i++){
            cin >> a[i];
            if(a[i] < min_a)
                min_a = a[i];
            sum_a += a[i];
        }
        for(int i = 0; i < n; i++){
            cin >> b[i];
            if(b[i] < min_b)
                min_b = b[i];
            sum_b += b[i];
        }
        if(0 < (sum_a + n*min_b)-(sum_b + n*min_a)){
            cout << (sum_b + n*min_a) << endl;
        }
        else{
            cout << (sum_a + n*min_b) << endl;
        }
    }
}