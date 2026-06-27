array = [2, 3, -2, 4]

if not array :
    print("Empty Array ")
else :
    
    max_prod = 1
    min_prod = 1 
    best = float("-inf")

    for num in array :
        new_max = max(num, num * max_prod, num * min_prod)
        new_min = min(num, num * max_prod, num * min_prod)
        max_prod = new_max
        min_prod = new_min
        best = max(max_prod, best)

    print(best)
