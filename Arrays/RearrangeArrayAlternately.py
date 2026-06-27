array = [1, 2, 3, 4, 5, 6, 7]

if not array :
    print("Empty array !")
else :
    left = 0 
    right = len(array) - 1
    result = []

    while left < right :
        result.append(array[right])
        result.append(array[left])
        right -= 1
        left += 1
    
    if left == right:
        result.append(array[left])

    print(result)