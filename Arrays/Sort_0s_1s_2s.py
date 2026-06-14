array = [2, 0, 1, 2, 0, 1, 1]

# count_0 = 0
# count_1 = 0
# count_2 = 0

# if not array :
#     print("Empty array !")
# else :
#     for num in array :
#         if num == 0 :
#             count_0 += 1
#         elif num == 1 :
#             count_1 += 1
#         elif num == 2 :
#             count_2 += 1

# count_list = [count_0,count_1,count_2]

# sorted_array = []
# for i in range(len(count_list)) :
#     for _ in range(count_list[i]) : 
#         sorted_array.append(i)

# print(sorted_array)

#Method_2

# count_0 = 0
# count_1 = 0
# count_2 = 0

# if not array :
#     print("Empty array !")
# else :
#     for num in array :
#         if num == 0 :
#             count_0 += 1
#         elif num == 1 :
#             count_1 += 1
#         elif num == 2 :
#             count_2 += 1

# # Rebuilding the array based on the counts
# index = 0

# # Put all the 0s first
# for i in range(count_0):
#     array[index] = 0
#     index += 1

# # Then put all the 1s
# for i in range(count_1):
#     array[index] = 1
#     index += 1

# # Finally, put all the 2s
# for i in range(count_2):
#     array[index] = 2
#     index += 1

# print("Sorted Array:", array)

# Method_3
# Dutch National Flag approach 

low = 0 
mid = 0
high = len(array) - 1

while mid <= high :
    if array[mid] == 0 :
        array[low], array[mid] = array[mid], array[low]
        low += 1
        mid += 1
    elif array[mid] == 1 :
        mid += 1
    elif array[mid] == 2 :
        array[mid], array[high] = array[high], array[mid]
        high -= 1

print(array)