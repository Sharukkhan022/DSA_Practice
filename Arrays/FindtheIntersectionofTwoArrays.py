array_1 = [1, 2, 2, 1]
array_2 = [2, 2, 3]

if not array_1 or not array_2:  # ✅
    print("Empty array!")
else :
     
    my_set = set(array_1)
    final_set = set()

    for num in array_2 :
        if num in my_set :
            final_set.add(num)
    
    print(list(final_set))

