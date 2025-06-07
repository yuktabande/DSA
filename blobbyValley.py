for test in range(int(input())):
    n = int(input())
    s = input()
    alice, bob = 0,0
    server = 'A'
    for i in range(n):
        if server == s[i]:
            if server == 'A': alice += 1
            else: bob += 1
        else:
            if server == 'A': server = 'B'
            else: server = 'A'
    print(alice,bob)
