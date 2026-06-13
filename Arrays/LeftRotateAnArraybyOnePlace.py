array = [1,2,3,4,5]

left = 0;

if not array :
    print("Empty array !")
else :
    for right in range(1,len(array)) :
        array[left], array[right] = array[right], array[left]
        left += 1

    
print(array)