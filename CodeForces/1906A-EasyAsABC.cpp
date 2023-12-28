
    #include <iostream>
    #include <bits/stdc++.h>
    #include <tuple>
    #include <math.h>
    using namespace std;
    int calculator(int x, int y, int b[3][3], int count, int prev_x, int prev_y);
    int main(){
        int width = 3;
        int height = 3;
            int blocks[3][3] = {0};
            int min_val = 'D';
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    char c;
                    std::cin.get(c);
                    if(c == '\n'){
                        j--;
                        continue;
                    }
                    blocks[i][j] = c;
                    blocks[i][j] -= 64;
                    if(blocks[i][j] < min_val){
                        min_val = blocks[i][j];
                    }
                }
            }
            int minimum_returned = 1000000;
            for(int i = 0; i < 3; i++){
                for(int j = 0; j < 3; j++){
                    if(min_val == blocks[i][j]){
                        int temp = calculator(i,j,blocks,1,-1,-1);
                        if(temp < minimum_returned){
                            minimum_returned = temp;
                        }
                    }
                }
            }
            string s = "";
            for(int i = 1; i <= 3; i++){
                int rem = minimum_returned % 10;
                minimum_returned /= 10;
                s = (char) (rem+64) + s;
            }
            cout << s << endl;
        }
    

    int calculator(int x, int y, int b[3][3], int count, int prev_x, int prev_y){
        if(count==3){
            return b[x][y];
        }
        int min = 100000;
        for(int i = x-1; i < x+2; i++){
            for(int j = y-1; j < y+2; j++){
                if((0 <= i && i < 3) && (0 <= j && j < 3)){
                    if(i == x && j == y)
                        continue;
                    if(i == prev_x && j == prev_y)
                        continue;
                    int temp = calculator(i,j,b,count+1,x,y);
                    if(temp<min){
                        min=temp;
                    }
                }
            }
        }
        return min+pow(10,(3-count))*b[x][y];
    }