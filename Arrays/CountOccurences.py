array = [1,2,2,3,1,4,2]

max_count = 0

for i in range(0,len(array)) :
    count = 0
    for j in range(1,len(array)) :
        if array[i] == array[j] :
            count += 1
            max_count = max(count ,max_count)

print(f"{array[i]} is occues {max_count} times")