array = [1, 4, 20, 3, 10, 5]

if not array :
    print('Empty array !')
else :
    target = int(input("Enter a number :"))
    start = 0
    window_sum = 0
    found = False
    
    for end in range(len(array)) :
        window_sum += array[end]

        while window_sum > target and start <= end :
            window_sum -= array[start]
            start += 1

        if window_sum == target :
            print(f"start = {start} , end = {end} --> {array[start : end + 1]}")
            found = True
            break
    if not found :
        print("Not found !")
        

