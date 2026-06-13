array = [5, 1, 3, 4, 2, 2, 3, 5, 5]

count = {}

for num in array:
    count[num] = count.get(num, 0) + 1


for num, frequency in count.items() :
    if frequency > 1 :
        print(num)

    