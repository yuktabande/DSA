nums = [3,2,3]
hash = {}
res = majority = 0

for n in nums:
    hash[n] = 1 + hash.get(n,0)
    if hash[n] > res:
        res = n
        majority = hash[n]
print(res)
