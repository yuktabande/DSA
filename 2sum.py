#nums = array of integers[input]; target = intger[input] 
#output = 2 number indices that add up to target 
# steps: for every number in num
#         check if target - number is in array 
#         return indices  

def twoSum(self, nums: List[int], target: int) -> List[int]:
        output = [0,0]
        for index,n in enumerate(nums):
            num = target - n
            if num in nums[:n] or num in nums[n+1:]:
                idx = nums.index(num)
                output[0] = index
                output[1] = idx
        return output
