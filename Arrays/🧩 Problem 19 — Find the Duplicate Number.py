array = [1, 3, 4, 2, 2]

if not array :
    print("Empty Array !")
else :
    count = {}

    for num in array:
        count[num] = count.get(num, 0) + 1


    for num, frequency in count.items() :
        if frequency > 1 :
            print(num)

# actual_sum = 0
# n = max(array)

# expected_sum = n * (n + 1) // 2

# for num in array :
#     actural_sum = actural_sum + num

# duplicate = actural_sum - expected_sum

# print(duplicate)

