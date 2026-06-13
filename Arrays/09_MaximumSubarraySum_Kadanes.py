array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

bag  = 0
best = float('-inf')

if not array :
    print("Empty array !")
else :
    for num in array :
        bag = max(num, bag + num)
        best = max(best, bag)
    print("Maximum subarray sum:", best) 