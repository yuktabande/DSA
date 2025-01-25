#step1: consider numbers starting from pos1 to pos(n-1) 
#step2: find the largest number and divide the array as numbers on left of largest number and numbers on right
#step3: ptr A at 1st number and ptr B at the next largest number 
#step4: for all the numbers in between, A - no. in between = +c units of water
#step5: for numbers on the right of largest
#step6: ptr A at first number and ptr B at next largest or next equal number
#step7: for all the numbers in between, A - no. in between = +c units of water

#height = [0,1,0,2,1,0,1,3,2,1,2,1]
height = [4,2,0,3,2,5]

del height[0]
del height[-1]

def LeftSideWater(left_part): 
    water_on_left = 0  
    a = left_part[0]
    for i in range(1, len(left_part)):
        if left_part[i]>a: 
            for j in range(left_part.index(a)+1, i):
                water_on_left += a-left_part[j]
            a = left_part[i]
    return water_on_left

def RightSideWater(right_part):
    water_on_right = 0
    a = right_part[0]
    for  i in range(1, len(right_part)):
        if right_part[i]>=a:
            for j in range(right_part.index(a) + 1, i):
                water_on_right += a-right_part[j]
            a = right_part[i]
    return water_on_right
            
def TotalWater(height):
    split_number = max(height) 
    index = height.index(split_number)
    left_part = height[:index + 1]
    right_part = height[index + 1:]

    total_units_of_water = LeftSideWater(left_part) + RightSideWater(right_part)
    return total_units_of_water

print(TotalWater(height))