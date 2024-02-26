"""DEmonstrate basic list syntax"""

# initialize an empty list 
grocery_list: list[str] = list() #list constrcutor 
grocery_list: list[str] = [] # literal



# add items to a list
grocery_list.append("bananas")
grocery_list.append("milk")
grocery_list.append("bread")

print(grocery_list)

# create an already populated list
grocery_list2: list[str] = ["bananas","ilk","break"]
print("Populated list:")
print(grocery_list2)
grocery_list2.append("eggs")
print(grocery_list2)

# indexing
print("Print the first element of string")
print(grocery_list[0])

# Modifying by index
print("Before change:")
print(grocery_list)
grocery_list[1] = "oat milk"
print("After change:")
print(grocery_list)

# the feature only apply to string in the list, not strings. 
# you can have duplicate in the list

# Measuring the length
print("The length of lists:")
print(len(grocery_list))

#Removing an item
grocery_list.pop(1)
print("After removing the first item")
print(grocery_list)

#remember to print out the list, if not print then it will return nothing 

def display(word: list[str])-> None:
    print(word)

display(grocery_list)

#create a list!
#name: create
#parameters: str and str
#RV: list[str]
#put both parameters into list and return that list 


def create(list_1: str, list_2: str)->list[str]:
    my_list: list[str] = [list_1, list_2]
    return my_list

print(create("Hello","Wolrd"))




