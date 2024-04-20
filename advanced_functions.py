#args
def sum_all(*args):
    total = 0
    for arg in args:
        total+= arg
    return total

print(sum_all(1,2,4,56))

#kwargs
def print_info(**data):
    for key,value in data.items():
        print(f"{key} : {value}")

print_info(name="Alvis",age=13,city="Adenta",salary=12000)

#lambda
double_even = lambda num
    for num in num:
        if num % 2 == 0:
            return lambda num: num * 2
    
print(double_even([1,2,3,4,5,6]))

#args and kwargs
def get_data(*args,**kwargs):
    print(args)
    print(kwargs)

get_data(1,2,3,4,name="Alvis",age=12,city="Adenta")

#Advanced application
def sum(num1,num2):
    return num1 + num2

def apply_operation(num1,num2,sum):
    return lambda num1,num2: sum(num1,num2)

print(apply_operation(lambda num1,num2:sum(num1,num2)))