
k = 27529676
operations = [0,1,0,0,1,1,1,1,1,1,0,0,0,1,1,0,1,0,1,1,1,0,0,1,1]
n, i = 1, 0
while n < k:
    n *= 2 
    i += 1
d = 0
while n > 1:
    if k > n // 2:
        k -= n // 2
        d += operations[i - 1]
    n //= 2
    i -= 1
print(chr(d % 26 + ord("a")))