array = [3, 1, 7, 2, 9, 4]

largest = float('-inf')         # Box 1
second_largest = float('-inf')  # Box 2


if not  array :
    print("Array is empty !")

else :    
    for num in array:
        if num > largest :        # Q1: is num greater than Box1?
            second_largest = largest   # old Box1 goes to Box2
            largest = num         # Box1 gets new number

        elif num > second_largest and num != largest :      # Q2: less than Box1 but greater than Box2?
            second_largest = num

print("Second largest:", second_largest)