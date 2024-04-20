#tuples are a collection of an ordered items which are not changeable 
#they are used to store multiple items in a single variable

#example
my_tuple = ("Vincent","Accra",11,"Waakye") #user information
print(my_tuple[1])

#tuple unpacking
#name = my_tuple[0]
#location = my_tuple[1]

#print(name,"lives at",location)

name,location,age,favourite_food = my_tuple

print(name,location,age)

#create a function that returns a tuple
def dimensions(x,y):
    return(x,y)

x,y = dimensions(20,80)
print("x: ",x)
print("y: ",y)

#create a tuple that contains your detail like name,location,age,school,etc
#unpack those into their respective variables

user_info = ("Alvis","Adenta",13,"Waakye")
#name = student_information[0]
#location = student_information[1]
#age = student_information[2]
#school = student_information[3]

user_name,user_location,user_age,user_favourite_food = user_info

print(f"User Name: {name}\n,User Location:{location}\n,User Age:{age}")
      
#unpack tuple into dictionary values
user_dic = {}

user_dic["username"],user_dic["userage"],user_dic["userlocation"],user_dic["userff"] = user_info

print(user_dic)