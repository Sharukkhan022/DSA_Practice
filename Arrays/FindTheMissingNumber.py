array = [1, 2, 3, 5]
n = len(array) + 1  # n-1 elements means n = length + 1

if not array:
    print('Empty array!')
else:
    actual_sum = 0

    for num in array:
        actual_sum += num
    expected_sum = (n * (n + 1)) // 2   # formula: 1+2+...+n

    if actual_sum == expected_sum:
        print('Nothing is missing')
    else:
        print(f'Missing number is {expected_sum - actual_sum}')
