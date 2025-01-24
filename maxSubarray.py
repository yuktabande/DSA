nums = [-2,1,-3,4,-1,2,1,-5,4]
sum = 0
maxSub = nums[0]
for n in nums:
    if sum < 0:
        sum = 0
    sum += n
    maxSub = max(maxSub, sum)
print(maxSub)