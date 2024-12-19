#Задание 1
import random

def analyze_array():
    
    array = [random.randint(1, 100) for _ in range(10)]
    max_element = max(array)
    smaller_count = 0
    larger_count = 0

    for element in array:
        if element < max_element:
            smaller_count += 1
        elif element > max_element:
            larger_count +=1


    print("Array:", array)
    print("Maximum element:", max_element)
    print("Number of elements smaller than maximum:", smaller_count)
    print("Number of elements larger than maximum:", larger_count)
analyze_array()

#Задание 2
def sum_greater_than_five():
    array = []
    for i in range(10):
        while True:
            try:
                num = int(input(f"Enter integer number {i+1}: "))
                array.append(num)
                break
            except ValueError:
                print("Invalid input. Please enter an integer.")

    sum_greater = sum(num for num in array if num > 5)
    print("Array:", array)
    print("Sum of numbers greater than 5:", sum_greater)

sum_greater_than_five()