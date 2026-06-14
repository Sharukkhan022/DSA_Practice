# Method_1
array = [16, 17, 4, 3, 5, 2]

# leader_list = []

# if not array :
#     print("Empty array !")
# else :

#     max_leader = array[-1]
#     leader_list = [max_leader]

#     for num in range(len(array) - 2 , -1, -1) :
#         if array[num] > max_leader :
#             leader_list.append(array[num])
#             max_leader =  array[num]
       

#     print(leader_list)


# Method_2

if not array :
    print("Empty array !")
else :

    max_leader = array[-1]
    leader_list = [max_leader]

    for right in range(len(array) - 2, -1 ,-1) :
        if array[right] > max_leader :
            leader_list.append(array[right])
            max_leader = array[right]

    print(leader_list)