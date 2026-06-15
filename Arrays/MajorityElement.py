# Method_1
array = [2, 2, 1, 1, 2, 2, 2]

if not array :
    print("Empty array !")
else :
    count = {}
    n = len(array)

    for num in array:
        count[num] = count.get(num, 0) + 1

    for num, frequency in count.items() :
        if frequency > n/2 :
            print(f"{num} occurse {frequency} > {n/2}")

# Method : 2
# Boyer-Moore Voting Algorithm.

if not array :
    print("Empty array !")
else :
    candidate = None
    count = 0

    for num in array :
        if count == 0 :
            candidate = num 
        if num == candidate :
            count += 1
        else :
            count -= 1

    print(candidate)
