# ++kwargs +args
# ++kwargs are used to accept multiple key -> value pairs in python
# +args is used to access a list of inputs in python

#args
def sum(*args):
    total = 0
    for arg in args:
        total+= arg
    return total

def letters(*letters):
    for letter in letters:
        print(letter)


#print(sum(1,2,3,4,5,6,7,8,93,5))
#print(letters("a","b","c"))

#kwargs
def userInfo(**data):
    for key,value in data.items():
        print(f"{key} ==> {value}")

userInfo(name="Vincent",age=12,location="Accra")

def get_data(*args,**kwargs):
    print(args)
    print(kwargs)

get_data(1,2,3,4,name="Vincent",location="Accra")