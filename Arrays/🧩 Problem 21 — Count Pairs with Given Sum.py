array = [1, 5, 7, 1]

if not array:
    print("Empty Array!")
else:
    count = 0
    target = 6
    pairs = []

    for i in range(len(array) - 1):
        for j in range(i + 1, len(array)):
            if array[i] + array[j] == target:
                count += 1
                pairs.append(([array[i], array[j]], (i, j)))

    print(f"Total Pairs = {count}")

    for num, (pair, index) in enumerate(pairs, start=1):
        print(f"{num}. Pair: {pair} at index: {index}")