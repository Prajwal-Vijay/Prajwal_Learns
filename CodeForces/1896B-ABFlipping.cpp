#include <iostream>
#include <bits/stdc++.h>
using namespace std;
bool find(std::list<int> done, int i);
int main(){
    int cases;
    cin >> cases;
    while(cases > 0){
        cases--;
        int n;
        cin >> n;
        string s;
        char chars[n];
        cin >> s;
        std::list<int> done;
        for (int i = 0; i < n; i++) {
            chars[i] = s[i];
        }
        int coun,prev_coun;
        prev_coun = -1;
        coun=0;
        // while(prev_coun != coun){
        //     prev_coun = coun;
            for(int i = 0; i < n-1; i++){
                if((chars[i] == 'A' and chars[i+1] == 'B') && (find(done, i) == false)){
                    chars[i] = 'B';
                    chars[i+1] = 'A';
                    coun++;
                    done.push_back(i);
                    i-=2;
                }
            }
        // }
        cout << coun << endl;
    }
}
bool find(std::list<int> done, int i){
    for(auto const& j : done){
        if(i == j){
            return true;
        }
    }
    return false;
}