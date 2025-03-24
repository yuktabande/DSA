#run a loop over input and create a string output
#if the char in input is output[i] then dont add to output, else add to output 
#if char same, no i+1 
#else add and i + 1
#first term add as it is 

input = "abcddcba"
output = ""
k = 0
for index in range(0,len(input)):
    if index== 0:
        output += input[index]
    else:
        if input[index] == output[k]:
            k = k
        else:
            output += input[index]
            k += 1
print(output)