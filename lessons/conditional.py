"""demonstarte bahvior of conditionals"""

user_input: str = input("Pick a number: ")
print(type(user_input))
user_number: int = int (user_input)
print (type(user_number))
print(user_input)

# if user_number is even, then print "even"

if user_number % 2 ==0: 
    print("even")
else:
    print("odd")
    
