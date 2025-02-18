#armstrong number 

num = 153
last_digit = num%10
str_num = str(num)
total = 0
for digit in str_num:
    total += int(digit)**last_digit
if total == num:
    print("Armstrong")
else:
    print("Not Armstrong")