#Question 1
nums = [1,2,3,4,5,6]
def double_numbers(num):
    return num * 2

map_data = map(double_numbers,nums)

print("map_data",map_data)

#Question2
def filter_even_numbers(num):
    return num % 2 == 0

filter_data = list(filter(filter_even_numbers,nums))

print("even numbers",filter_data)

#Question3
celsius = [1,2,3,4,5,6]
def celsius_to_fahrenheit(celsius):
    return celsius == 9/5(celsius + 32)

map_data2 = map(celsius_to_fahrenheit,celsius)

print("fahrenheit",map_data2)

#Question4
integers = [-1,2,-3,4,-5,6]
def filter_positive_numbers(integer):
    return integer >= 0

filter_data = list(filter(filter_positive_numbers,integers))

print("positive numbers",filter_data)
