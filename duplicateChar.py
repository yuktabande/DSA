s = "Geeksforgeeks"
s1 = s.lower()
done_list = []

for i in s1:
    if i not in done_list:  # Check if the character is already processed
        count = 0
        for j in s1:
            if i == j:
                count += 1
        done_list.append(i)  # Mark the character as processed
        print(f"{i}, count = {count}")
