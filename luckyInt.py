length = {}
for i in range(len(arr)):
  if arr[i] not in length:
    length[arr[i]] = 1
  else:
    length[arr[i]] += 1
        
res = -1
for key in length:
  if length[key] == key:
    res = max(res, key)
return res
