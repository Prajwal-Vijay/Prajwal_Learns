#include <iostream>
#include <bits/stdc++.h>
#include<map>
#include<vector>
using namespace std;
class villager{
    public:
    long long int ai;
    long long int bi;
};
void merge(villager arr[], int l, int m, int r)
{
    int i, j, k;
    int n1 = m - l + 1;
    int n2 = r - m;
 
    // Create temp arrays
    villager L[n1], R[n2];
 
    // Copy data to temp arrays L[] and R[]
    for (i = 0; i < n1; i++)
        L[i] = arr[l + i];
    for (j = 0; j < n2; j++)
        R[j] = arr[m + 1 + j];
 
    // Merge the temp arrays back into arr[l..r
    i = 0;
    j = 0;
    k = l;
    while (i < n1 && j < n2) {
        if (L[i].bi <= R[j].bi) {
            arr[k] = L[i];
            i++;
        }
        else {
            arr[k] = R[j];
            j++;
        }
        k++;
    }
 
    // Copy the remaining elements of L[],
    // if there are any
    while (i < n1) {
        arr[k] = L[i];
        i++;
        k++;
    }
 
    // Copy the remaining elements of R[],
    // if there are any
    while (j < n2) {
        arr[k] = R[j];
        j++;
        k++;
    }
}
 
// l is for left index and r is right index of the
// sub-array of arr to be sorted
void mergeSort(villager arr[], int l, int r)
{
    if (l < r) {
        int m = l + (r - l) / 2;
 
        // Sort first and second halves
        mergeSort(arr, l, m);
        mergeSort(arr, m + 1, r);
 
        merge(arr, l, m, r);
    }
}
 
int main(){
    int cases;
    cin >> cases;
    while(cases > 0){
        cases--;
        long long int n;
        cin >> n;
        long long int p;
        cin >> p;
        villager villagers[n];
        for(int i = 0; i < n; i++){
            cin >> villagers[i].ai; 
        }
        for(int i = 0; i < n; i++){
            cin >> villagers[i].bi;
        }
        mergeSort(villagers,0,n-1);
        if(villagers[0].bi >= p){
            cout << p*n << endl;
            continue;
        }
        long long int cost = 0;
        long long int count = 0;
        long long int i = 0;
        count++;
        cost += p;
        while(count < n){
            if(villagers[i].bi < p){
                cost += villagers[i].bi*villagers[i].ai;
                count += villagers[i].ai;
                if(count > n){
                    cost -= (count - n)*villagers[i].bi;
                    count = n;
                }
                i++;
            }
            else{
                cost += (long long int)(n-count)*p;
                count = n;
            }
        }
        cout << cost << endl;
    }
}
