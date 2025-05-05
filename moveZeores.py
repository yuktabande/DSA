def swap(val1, val2, pos1, pos2):
    nums[pos1] = val2
    nums[pos2] = val1

#move all the zeroes to the end without disturbing the array and without making a copy of the array 
#scan through the array
#if zero, swap it with the next number 
#move to the next number 
nums = [0,1,0,3,12]

for i,n in enumerate(nums): 
    if n == 0:
        while(nums.index(n)==(len(nums)-1)):
            swap(n,nums[i+1],i,i+1)
        print(nums)

def moveZeroes(self, nums: List[int]) -> None:

        insert_pos = 0
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        for i in range(insert_pos, len(nums)):
            nums[i] = 0
        
        return nums