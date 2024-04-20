"""
    lambda in python is a way creating a function without using the
    def keyword. lambda function does not have a name but rather 
    assigned to a variable.
    They are used for performing less complex operations when you don't want to create a function.
    You create a lambda function using the lambda keyword
"""
#Using normal function
def sumTwo(num1,num2):
    return num1 + num2

#lambda function example
sumTwo = lambda num1,num2: num1 + num2

print(sumTwo(3,6))

"""
create a function that takes a number and
generates even number between 1 and the number
"""

def even_number_generator(limit):
    for number in range(1,limit):
        if number % 2 == 0:
            print(number)

even_number_generator(10)

"""
   create a function that checks whether a number is
   even 

   """

isEven = lambda number: number % 2 == 0

print(isEven(2))


#class Test

"""
Q1
create a function that takes your name and your age.
the function should check whether you are above 18
If you are above 18, it should print "Hello {name}, you are not qualified to vote"
else it should print "Hello{name}, you are qualified to vote"


Q2
write a function that takes a name and return true if your name is "Kofi"
else it will return false
"""

#Q1
def check_age(name,age):
    if age >= 18:
        print(f"Hello {name},you are qualified to vote")
    else:
         print(f"Hello {name},you are not qualified to vote")


print(check_age("Alvis",13))

#Q2
def isKofi(name):
    if name == "kofi":
        return True
    else:
        return False

print(isKofi("Kwame"))