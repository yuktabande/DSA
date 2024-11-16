arr = [1,2,3,4,5,6]
n = len(arr)

for i in range(n // 2):
    a = arr[i]
    arr[i] = arr[n-i-1]
    arr[n-i-1] = a

for num in range(n):
    print(arr[num])
