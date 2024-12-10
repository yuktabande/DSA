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






		