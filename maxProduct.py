nums = [2,3,-2,4]
outputArr = []
maxProduct = float('-inf')

for pos, num in enumerate(nums):
    maxProduct = num
    product = num
    outputArr.append(num)
    for i in range(pos,len(nums)):
        product *= nums[i]
        if product > maxProduct:
            maxProduct = product
            outputArr.append(nums[i])
        else:
            del outputArr[0]
print(outputArr)