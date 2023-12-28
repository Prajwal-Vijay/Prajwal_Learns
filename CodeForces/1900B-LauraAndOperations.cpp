
    #include <iostream>
    #include <bits/stdc++.h>
    using namespace std;
    int main(){
        int cases;
        cin >> cases;
        while(cases > 0){
            int a,b,c;
            cin >> a >> b >> c;
            if(abs(b-c)%2 == 0){
                cout << "1" << " ";
            }else{
                cout << "0" << " ";
            }
            if(abs(a-c)%2 == 0){
                cout << "1" << " ";
            }
            else{
                cout << "0" << " ";
            }
            if(abs(a-b)%2 == 0){
                cout << "1" << " ";
            }else{
                cout << "0" << " ";
            }
            cout << endl;
            cases--;
        }
    }