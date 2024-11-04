def sum_even_numbers(numbers):
    numbers=[1,2,3,4,5,6]
    even_numbers=sum(num for num in numbers if num % 2 == 0)
    print(numbers)


sum_even_numbers
