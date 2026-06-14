# METHOD_1

array = [40,10,47,2324,12]
array2 = []

for i in range(len(array) - 1, -1 ,-1) :
    array2.append(array[i])

print(array2)

# METHOD_2 :

array = [3545,423423,323,3234,4]

left = 0
right = len(array) - 1

while left < right :
    array[left], array[right] = array[right], array[left]
    left += 1
    right -= 1

print(array)

