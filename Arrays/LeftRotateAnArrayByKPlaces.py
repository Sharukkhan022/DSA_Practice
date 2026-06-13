array = [1,2,3,4,5]

k = int(input("Enter a number :"))

k = k % len(array)
count = 0

if not array :
    print("Empty Array !")
else :
    while count < k :
        left = 0
        for right in range(1,len(array)) :
            array[left] , array[right] = array[right], array[left]
            left += 1
        count += 1

print(array)                        

    
