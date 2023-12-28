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
        
        int i = 0;
        int len = 0;
        cin >> len;
        string s;
        cin >> s;
        vector<int> g;
        g.push_back(i);
        // if(s[0] == '<'){
        //     i++;
        // }
        // else if(s[0] == '>'){
        //     i--;
        // }
        // g.push_back(i);
    //     for(int j = 1; j < len; j++){
    //         if(s[j-1] == '>' && s[j] == '<'){
    //             if(i != *max_element(g.begin(), g.end())){
    //                 i = *max_element(g.begin(), g.end());
    //             }
    //         }
    //         else if(s[j] == '<'){
    //             i++;
    //         }
    //         else if(s[j-1] == '<' && s[j] == '>'){
    //             if(i != *min_element(g.begin(), g.end())){
    //                 i = *min_element(g.begin(), g.end());
    //             }
    //         }
    //         else if(s[j] == '>'){
    //             i--;
    //         }
    //         if(!(std::find(g.begin(), g.end(), i) != g.end())){
    //                 g.push_back(i);
    //         }
    //     }
           
    //    cout<<g.size()<<endl;  
    // }
        int sign_changes = 0;
        for(int j = 1; j < len; j++){
            if(s[j-1] != s[j]){
                sign_changes++;
            }
        }
        if(sign_changes == 0){
            cout << len+1 <<endl;
        }
        else if(sign_changes==len-1){
            cout << 2 <<endl;
        }
        else{
            cout<<len-sign_changes<<endl;
        }
}
}
