#create a function to add two numbers
def add(first_number,second_number):
    return first_number + second_number

#create a function to multiply two numbers
def multiply(first_number,second_number):
    return first_number * second_number

print(add(4,5))

#create a function that takes another function
def perform_operations(num1,num2,function):
    #call another function and return the result
    result = function(num1,num2)
    return result

def isPrime(numbers):
    for number in numbers:
        if number % 2 != 0:
            print(number,"is a prime number")

def isEven(numbers):
    for number in numbers:
        if number % 2 == 0:
            print(number,"is an even number")

def check_even_or_prime(numbers,is_prime_func,is_even_func):
    if numbers:
        if is_prime_func != None:
            is_prime_func(numbers)
        else:
            print("provide a prime function")
        if is_even_func != None:
            is_even_func(numbers)  
        else:
            print("provide an even function")
    else:
        print("provide a list of numbers")


check_even_or_prime([1,2,3,4,5,6,7],isPrime,isEven)
#print(perform_operations(10,20,add))
#print(perform_operations(10,20,multiply))

#Create a main function that takes a list and an (exponent 2) function as parameter
#and the main function calls the exponent 2 function and returns the result
#The expo
# nent 2 function should take a list and print out the exponents of all the numbers.

def exponent2(numbers):
    for number in numbers:
        print(number * number,"is number exponent 2")

def check_exponent2(numbers,exponent2_func):
    if exponent2_func != None:
        exponent2_func(numbers)
    else:
        print("provide a list of numbers")


check_exponent2([1,2,3,4,5,6,7],exponent2)




