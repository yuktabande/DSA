nums1 = [0]
m = 0
nums2 = [1]
n = 1

if n == 0:
    print(nums1)
else:
    i = 0
    while m<len(nums1) and i<len(nums2):
        nums1[m] = nums2[i]
        m+=1
        i+=1
    nums1.sort()
    print(nums1)