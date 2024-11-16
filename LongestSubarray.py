# arr = [2,7,1,6,4,5]
# k = 3
# n = len(arr)-1

# #sum all numbers and check if it is divisible by k, if not:
#     #for numbers in descending order starting from (total elements-1) number:
#         #subArray[0] = array[0] till subarray[highest_num] = array[highest_num]:
#             #if element sum is divisible by k return, else
#                 #if highest_sum is not last element of array:
#                     #subArray[0] = array[1] till subarray[highest_num] = array[highest_num+1]:
#                         #if element sum is divisible by k return, else
#                             #if highest_sum is not last element of array: continues...
#                 # if highest_sum is last element decrease total pos by 1
# sum = 0
# subarr = []
# for ele in arr:
#     sum += ele 
# if sum%k == 0:
#     print(sum)
# else:
#     sum = 0
#     for num in range(n,-1,-1):
#         for pos in range(0,num+1):
#             subarr[pos] = arr[pos]
#         for ele in subarr:
#             sum += ele
#         if sum%k == 0:
#             print(sum)

# Python3 implementation to find the longest subarray
# with sum divisible by k

def longestSubarrWthSumDivByK(arr, N, k):
	maxl = 0
	for i in range(N):
		sum1 = 0
		for j in range(i, N):
			sum1 += arr[j]
			if sum1 % k == 0:
				maxl = max(maxl, j - i + 1)
	return maxl

# Driver code
arr = [2, 7, 6, 1, 4, 5]
n = len(arr)
k = 3

print("Length =", longestSubarrWthSumDivByK(arr, n, k))






		