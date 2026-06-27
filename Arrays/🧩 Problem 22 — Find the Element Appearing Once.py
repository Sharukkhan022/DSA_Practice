array = [2, 3, 5, 4, 5, 3, 4]

if not array :
    print("Empty array !")
else :
#     count = {}

#     for num in array :
#         count[num] = count.get(num, 0) + 1

#     for num, frequency in count.items() :
#         if frequency == 1 :
#             print(num)


    result = 0 
    for num in array :
        result = result ^ num 

        
    print(result)
  