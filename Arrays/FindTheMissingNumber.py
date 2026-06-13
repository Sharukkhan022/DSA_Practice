array = [1,2,4,3,5]


if not array :
    print("Empty array !")

sum = 0
n = max(array)

for num in range(len(array) + 1):
    sum += num

sum_of_n_natural_number = (n * (n + 1)) // 2

if sum == sum_of_n_natural_number :
    print("Nothing is missing ")
else :
    print(f"Missing number is {sum_of_n_natural_number - sum}")
