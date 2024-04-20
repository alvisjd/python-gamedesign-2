"""
map and filter in python are used for manipulating data like lists,dictionary,set,etc

"""
# add two to every number in the list nums = [1,2,3,4,5,6]
nums = [1,2,3,4,5,6]

#map example using a normal function
def addTwo(num):
    return num + 2

map_data1 = map(addTwo,nums)

#map example using a lambda function
map_data2 = list(map(lambda num:num + 2,nums))

print("map_data 1 with normal function",map_data1)

print("map_data 2 with lambda function",map_data2)

#filter() example

#using a normal function
def get_evens(num):
    return num % 2 == 0

filter_data = list(filter(get_evens,nums))

#using a lambda function


filter_data2 = list(filter(lambda num: num % 2 == 0,nums))


print("filtered list using normal function",filter_data)

print("filtered list using lambda function",filter_data2)


