#IMPLEMENTATION USING LINEAR SEARCH
#time complexity - o(n)

#initialize an array 
arr = [1,5,4,2,3]

#finding the maximum element
max_ele = arr[0]
for element in arr:
    if element > max_ele:
        max_ele = element 

#finding the minimum element 
min_ele = arr[0]
for element in arr:
    if element < min_ele:
        min_ele = element

print(f"The maximum element is: {max_ele}\nThe minimum element is {min_ele}")

