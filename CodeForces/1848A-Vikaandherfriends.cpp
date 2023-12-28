#include <iostream>
#include<tuple>
#include<vector>
#include <bits/stdc++.h>
using namespace std;
int main(){
    int cases;
    cin >> cases;
    while (cases>0){
        int n, m, f;
        cin >> n;
        cin >> m;
        cin >> f;
        cases--;
        tuple <int, int> Player;
        vector<tuple<int,int>> Friends;
        for(int i = 0; i <= f; i++){
            int x;
            int y;
            cin >> x;
            cin >> y;
            if (i == 0)
                Player = make_tuple(x,y);
                continue;
            Friends.emplace_back(make_tuple(x,y));
        }
        for(int i = 0; i < f; i++){
            vector<tuple<int,int>> neighbor = neighbors(n,m, Friends[i]);
        }
    }
}

vector<tuple<int,int>> neighbors(int n, int m, tuple<int,int> t){
    int x = get<0>(t);
    int y = get<1>(t);
    vector<tuple<int,int>> ToReturn;
    if((x-1)>=1 && (y)>=1){
        ToReturn.emplace_back(make_tuple((x-1),y));
    }
    else if((x)>=1 && (y-1)>=1){
        ToReturn.emplace_back(make_tuple((x,(y-1))));
    }
    else if((x+1)<=n,y<=m){
        ToReturn.emplace_back(make_tuple((x+1),y));
    }
    else if(x<=n, (y+1)<=m){
        ToReturn.emplace_back(make_tuple(x,(y+1)));
    }
    return ToReturn;
}



bool state(tuple <int, int> Player,vector<tuple<int,int>> Friends){
    for(auto & element: Friends){
        if((get<0>(element) == get<0>(Player)) && (get<1>(element) == get<1>(Player))){
            return true;
        }
    }
    return false;
}