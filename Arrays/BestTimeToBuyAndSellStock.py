# array = [7, 1, 5, 3, 6, 4]
array = [7, 6, 4, 3, 1] 

min_price = float('inf')
max_profit = 0

if not array :
    print("Empty array !")
else :
    for price in array :
        min_price  = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
        
    print(max_profit)