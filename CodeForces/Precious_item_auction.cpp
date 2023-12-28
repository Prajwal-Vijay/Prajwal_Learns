#include <iostream>
#include<tuple>
#include<vector>
#include <bits/stdc++.h>
#include <cmath>

using namespace std;
int partition(int arr[],int low,int high);
void quickSort(int arr[],int low,int high);
int main(){
    int cases = 0;
    cin >> cases;
    while(cases--){
        int N, K;
        cin >> N;
        cin >> K;
        int bids[N];
        for(int i = 0; i < N; i++){
            cin >> bids[i];
        }
        quickSort(bids,0,N);
        int max = 0;
        int min = bids[N-K-1];
        for(int i = 1; i <= K; i++){
            max += bids[N-2*i];
            min += bids[i-1];
        }
        cout << (min - bids[K-1]) <<" " << max << endl;
    }
}

int partition(int arr[],int low,int high)
{   
  int pivot=arr[high];
  int i=(low-1);
   
  for(int j=low;j<=high;j++)
  {
    if(arr[j]<pivot)
    {
        i++;
        swap(arr[i],arr[j]);
    }
  }
  swap(arr[i+1],arr[high]);
  return (i+1);
}

void quickSort(int arr[],int low,int high)
{
  if(low<high)
  {
    int pi=partition(arr,low,high);
    quickSort(arr,low,pi-1);
    quickSort(arr,pi+1,high);
  }
}