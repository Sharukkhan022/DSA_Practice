array = [3,2,2,3]

print("Before : ",array)

for i in range(len(array)):
    for j in range(i + 1, len(array)):
        if array[i] == array[j]:
            array.remove(array[j])
        
        else:
            j = j + 1

print("After : ",array)