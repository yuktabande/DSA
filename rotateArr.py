#brut force approach 
nums = [-1,-100,3,99]
k = 2
n = len(nums)
k = k%n
result = [0]*n
for i in range(n):
    result[(i+k)%n] = nums[i] 

for i in range(n):
    nums[i] = result[i]

print(nums)

