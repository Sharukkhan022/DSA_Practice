array = [0, 1, 0, 0, 0]

left = 0

for right in range(len(array)) :
    if array[right] != 0:
        array[left], array[right] = array[right], array[left]
        left += 1

print(array)


# insert_pos = 0 

# for num in array :
#     if num != 0 :
#         array[insert_pos] = num
#         insert_pos += 1

# while insert_pos < len(array) :
#     array[insert_pos] = 0
#     insert_pos += 1

# print(array)