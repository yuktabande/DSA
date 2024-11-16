#finding next permutation in lexicographic order 
arr = [1,1,5]
n = len(arr) - 1

if arr[n-1] < arr[n]:
    a = arr[n-1]
    arr[n-1] = arr[n]
    arr[n] = a
    print(arr)

elif arr[n-1] > arr[n]:
    a = arr[n-1]
    arr[n-1] = arr[n]
    arr[n] = a 

    if arr[n-2] < arr[n-1]:
        b = arr[n-2]
        arr[n-2] = arr[n-1]
        arr[n-1] = b
        print(arr)