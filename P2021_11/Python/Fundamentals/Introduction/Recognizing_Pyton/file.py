num1 = 42 # variable declaration, initialize numbers
num2 = 2.3 # variable declaration, initialize numbers
boolean = True # variable declaration, initialize boolean
string = 'Hello World' # variable declaration, initialize string
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] # variable declaration, initialize list
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} # variable declaration, initialize dictionary
fruit = ('blueberry', 'strawberry', 'banana') # variable declaration, initialize tuple
print(type(fruit)) # print to console, type check
print(pizza_toppings[1]) # print to console, list access value
pizza_toppings.append('Mushrooms') # list add value
print(person['name']) # print to console, dictionary access value
person['name'] = 'George' # dictionary change value
person['eye_color'] = 'blue' # dictionary add value
print(fruit[2]) # print to console, truple access value

if num1 > 45: 
    print("It's greater") # conditional if, print to log
else:
    print("It's lower") # conditional else, printo to log

if len(string) < 5:  # conditional if, print to log
    print("It's a short word!")
elif len(string) > 15:
    print("It's a long word!") # conditional else if, print to log
else:
    print("Just right!") # conditional else, print to log

for x in range(5): # for loop start at 0 and goes up to 5
    print(x)
for x in range(2,5): # for loop start at 2 and goes up to 5
    print(x)
for x in range(2,10,3): # for loop start at 2, goes up to 10 increment by 3
    print(x)
x = 0 # variable declaration, initialize number
while(x < 5): # while loop, variable declaration
    print(x)
    x += 1

pizza_toppings.pop() # list delete value
pizza_toppings.pop(1) # list delete 1 list data

print(person) # print to console, dictionary
person.pop('eye_color') # dictionary delete value
print(person) # print to console, dictionary

for topping in pizza_toppings: # for loop list 
    if topping == 'Pepperoni': # if for loop list
        continue                # continues
    print('After 1st if statement') # print to console
    if topping == 'Olives': # if conditional
        break # stop

def print_hello_ten_times(): # funtion declaration
    for num in range(10): # for loop from 0 to 10
        print('Hello') # print to console

print_hello_ten_times() # call the function

def print_hello_x_times(x): # function declaration with parameter x 
    for num in range(x): # for loop until given value x
        print('Hello')  # print to console

print_hello_x_times(4) # call the function argument 4

def print_hello_x_or_ten_times(x = 10): # function declaration x equal to 10 
    for num in range(x): # for loop until given value x
        print('Hello') #print to console

print_hello_x_or_ten_times() # call the function declaration 10
print_hello_x_or_ten_times(4) # call the function declaration 4


"""
Bonus section
"""

# print(num3) NameError variable name is not defined
# num3 = 72 variable declaration number 
# fruit[0] = 'cranberry' TypeError 
# print(person['favorite_team']) Key Error 
# print(pizza_toppings[7]) Indexerror
#   print(boolean) IndentationError
# fruit.append('raspberry') AttributeError: 'truple object has no attribute 'append'
# fruit.pop(1) AttributeError: 'truple object has no attribute 'pop'