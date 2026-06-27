# # Method_1 : bruth force
array = [2, 7, 11, 15]

if not array :
    print("Empty array !")
else :
    target = 18
    total = 0
    found = False

    for i in range(len(array)) :
        for j in range(i + 1,len(array)) :

            total = array[i] + array[j]

            if total ==  target :
                print(f"Traget is found at --> {[i,j]}")
                found = True 
                break
    
        if found :
            break
    
    if not found :
        print("Target is not found !")

# Method_2 : Optimal using Dictionary

if not array :
    print("Empty array !")
else :
    target = 17
    storage_box = {}
    found = False
    
    for i, num in enumerate(array) :
        complement = target - num

        if complement in storage_box :
            print(f"Indices of the two numbers: {[storage_box[complement], i]}")
            found = True
            break

        storage_box[num] = i

    if not found :
        print("Not found !")