array = [1, 0, -1, 0, -2, 2]

if not array :
    print(array)
else :
    array.sort()
    left = 0
    right = len(array) - 1
    target = 0
    total = 0
    result = []

    for i in range(0,len(array)):

        if i > 0 and array[i] == array[i-1]:          # skip duplicate for i
                continue
        
        for j in range(i +1, len(array)) :

            if j > i+1 and array[j] == array[j-1]:       #skip duplicate for j
                continue

            left = j + 1
            right = len(array) - 1

            while left < right :
                total =  array[i] + array[j] + array[left] + array[right]

                if total == target :
                    result.append([array[i], array[j], array[left], array[right]])
                    left += 1
                    right -= 1
                
                 # Skip duplicate values for left
                    while left < right and array[left] == array[left - 1]:
                        left += 1

                    # Skip duplicate values for right
                    while left < right and array[right] == array[right + 1]:
                        right -= 1

                elif total < target:
                    left += 1
                else:
                    right -= 1


    print(result)
