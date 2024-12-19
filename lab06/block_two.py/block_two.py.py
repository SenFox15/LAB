# Задача 1

def sum_consecutive_odd(numbers):
  
    if not numbers: 
        return 0
    sum_odds = 0
    for num in numbers:
        if num % 2 != 0:
            sum_odds += num
        else:
            break 
    return sum_odds


numbers = [1.5, 3.7, 5.1, 2, 2.3, 7.9]
print(f"Sum etih numbersof: {sum_consecutive_odd(numbers)}")  



# Задача 2

def count_and_sum_digits(n):
    if n <= 0:
        return 0, 0
    count = 0
    sum_digits = 0
    while n > 0:
        digit = n % 10
        sum_digits += digit
        count += 1
        n //= 10
    return count, sum_digits


n = 12345
count, sum_digits = count_and_sum_digits(n)
print(f"Kol. num V {n}: {count}, sum num: {sum_digits}") 
