
#include <iostream>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases;
    cin >> cases;
    for(int i = 0; i < cases; i++){
        int n;
        cin >> n;
        int k;
        cin >> k;
        int numbers[n];
        //Taking input of Numbers into to numbers array
        for(int j = 0; j < n; j++){
            cin >> numbers[j];
        }
        sort(numbers, numbers + n);
        int diff[n-1];
        for(int j = 1; j < n; j++){
            diff[j-1] = numbers[j] - numbers[j-1];
        }
        int count = 0;
        int maxcount = 0;
        for(int i = 0; i < n; i++){
            count++;
            if(diff[i] > k){
                if(count > maxcount)
                    maxcount = count;
                count = 0;
            }
        }
        if(count > maxcount)
            maxcount = count;
        if(n == 1)
            maxcount = 1;
        cout << (n-maxcount) << endl;
    }
    return 0;
}