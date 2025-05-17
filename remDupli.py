nums = [0,0,1,1,1,2,2,3,3,4]
k = len(nums) 
# print(k)
#case for less than 2 elements
if k < 3:
    if k == 1:
        print(nums[0])
    else:
        if nums[0] == nums[1]:
            nums.remove(nums[1])
            nums.append('_')

#case otherwise
left,right = 0,1
while left < right and right < len(nums) and left < len(nums):
    if nums[left] == nums[right]:
        nums.remove(nums[right])
    elif nums[left] != nums[right]:
        left += 1
        right += 1
#adding empty spaces
n = len(nums)
for space in range(0,(k-n)):
    nums.append('_')
print(nums)

