/*Starting from the 1st element, start comparing it with the next consecutive element to check
if an element is smaller than the current element(in case of ascending) and swap it.
Do this for all the elements*/

#include<iostream>
using namespace std;

void bubbleSort(int arr[], int n) {//O(n^2)
    for(int i = 0; i < n-1; i++){
        for(int j = 0; j<n-i; j++){
            if(arr[j] > arr[j+1]){
                swap(arr[j], arr[j+1]);
            }
        }
    }
}

void printArray(int arr[], int n){
    for(int i = 0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout << endl;
} 

int main() {
    int n = 5;
    int arr[] = {4,1,5,2,3};
    return 0;

    bubbleSort(arr, n);
    printArray(arr,n);
    return 0;
}