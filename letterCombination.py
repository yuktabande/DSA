mapping = {"2":['a','b','c'],
           "3": ['d','e','f'],
           "4": ['g','h','i'],
           "5": ['j','k','l'],
           "6": ['m','n','o'],
           "7": ['p','q','r','s'],
           "8": ['t','u','v'],
           "9": ['w','x','y','z']
           }
digits = "23"

if not digits:
    return []

output = ['']
for digit in digits:
    letters = mapping[digit]
    temp = []
    for combination in output:
        for letter in letters:
            temp.append(combination + letter)
    output = temp
return output 

        

