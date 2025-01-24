nums = [4, 5, 6, 7, 0, 1, 2]
target = 0

for index, num in enumerate(nums):
    if num == target:
        print(index)  
        break
else:
    print(-1)  