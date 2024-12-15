Array = [170, 45, 75, 90, 802, 24, 2, 66]
maxValue = max(Array)
count = 0
while(maxValue>0):
    maxValue = int(maxValue/10) 
    count += 1

outputArray = [0]*len(Array) 
num = 10
while(count>0):
    for i in range(0,len(Array)):
        outputArray[i] = Array[i]%num
    outputArray = sorted(outputArray)
    num *= 10
    count -= 1 
print(outputArray)
