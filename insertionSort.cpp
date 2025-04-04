/*In an array of numbers, a current number is 
compared with each and every element to place
it on the right position*/

#include<iostream>
using namespace std;

void printArray(int arr[], int n){
    for(int i = 0; i<n; i++){
        cout<<arr[i]<<" ";
    }
    cout << endl;
} 
void insertionSort(int arr[], int n) {
    for(int i=1; i<n; i++){
        int curr = arr[i];
        int prev = i-1;

        while(prev >= 0 && arr[prev] > curr) {
            arr[prev+1] = arr[prev];
            prev--;
        }

        arr[prev+1] = curr;
    }
}
int main() {
    int n = 5; 
    int arr[] = {4, 1, 5, 2, 3};

    return 0;
}