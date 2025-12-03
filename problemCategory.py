# cook your dish here
T = int(input())
while T > 0:
    num = int(input())
    if num >= 1 and num < 100:
        print('Easy')
    elif num >= 100 and num < 200:
        print('Medium')
    else:
            print('Hard')
    T-= 1
