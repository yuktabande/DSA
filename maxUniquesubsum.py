nums = [1,1,0,1,1]
positiveNumsSet = set([num for num in nums if num > 0])
print(max(nums) if len(positiveNumsSet) == 0 else sum(positiveNumsSet))