nums = [1, 2, 3, 4]

prefix = [1] * len(nums)
suffix = [1] * len(nums)
outputArr = [1] * len(nums)

for i in range(1, len(nums)):
    prefix[i] = prefix[i - 1] * nums[i - 1]

for i in range(len(nums) - 2, -1, -1):
    suffix[i] = suffix[i + 1] * nums[i + 1]

for i in range(len(nums)):
    outputArr[i] = prefix[i] * suffix[i]

print("Output Array:", outputArr)
