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
        int b[n];
        for(int i = 0; i < n; i++){
            b[i] = 3;
        }
        std::map<int , std::vector<int>> pairs;
        for(int i = 0; i < n; i++){
            cin >> a[i];
            if(pairs.find(a[i]) != pairs.end()){
                pairs[a[i]].push_back(i);
            }
            else{
                vector<int> t;
                t.push_back(i);
                pairs[a[i]] = t;
            }
            // for(int j = 0; j < i; j++){
            //     if(a[j] == a[i]){
            //         pairs.push_back(make_tuple(j,i));
            //     }
        }
        std::vector<int> keys;
        for (const auto& pair : pairs) {
            keys.push_back(pair.first);
        }
        if(pairs.size() == 1){
            cout << -1 << endl;
            continue;
        }
        else{
            int count = 0;
            for(int i = 0; i < pairs.size(); i++){
                if(pairs[keys[i]].size() >= 2){
                    count++;
                }
            }
            if(count < 2){
                cout << -1 << endl;
                continue;
            } 
        }
        
        int count = 0;
        for(int i = 0; i < pairs.size(); i++){
            if(pairs[keys[i]].size() > 1){
                count++;
            }
            for(int j = 0; j < pairs[keys[i]].size(); j++){
                    if(count%2 == 0){
                        if(j==0){
                            b[pairs[keys[i]][j]] = 1;
                        }
                        else{
                            b[pairs[keys[i]][j]] = 2;
                        }
                    }
                else{
                    if(j==0){
                        b[pairs[keys[i]][j]] = 1;
                    }
                    else{
                        b[pairs[keys[i]][j]] = 3;
                    }
                }
                
            }
        }
        for(int i = 0; i < n; i++){
            cout << b[i] << " ";
        }
        cout << endl;
    }
    return 0;
}
