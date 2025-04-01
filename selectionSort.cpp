/*Assume 2 parts of array - sorted and unsorted 
first the entire array is unsorted. Select the smallest element and 
swap it with 0th position element. Now in unsorted list, find the smallest element
and add it to the sorted list*/
#include<iostream>
using namespace std;

void printArray(int arr[], int n){
    for(int i = 0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout << endl;
} 
void selectionSort(int arr[], int n) {
    for(int i=0; i<n-1; i++){
    int smallestIdx = i; //unsorted part starting
    for(int j=i+1; j<n; j++){
        if(arr[j] < arr[smallestIdx]) {
            smallestIdx = j;
        }
    }
    swap(arr[i], arr[smallestIdx]);
}
}

int main(){
    int n = 5;
    int arr[] = {4,1,5,2,3};
    selectionSort(arr,n);
    printArray(arr, n);
    return 0; 
}