#lambda operation in python

addTwo = lambda firstNumber,secondNumber: firstNumber + secondNumber

sayHello = lambda name: f"hello {name}"

#lambda with a function
def multiply_by_unknown_number(num):
    return lambda a: a + num

print(addTwo(2,6))
print(sayHello("Vincent"))

result = multiply_by_unknown_number(5)
print(result(7))