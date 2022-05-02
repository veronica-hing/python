## primitive data types
##variable declarations, numbers
num1 = 42 
num2 = 2.3
##booleans
boolean = True
##string
string = 'Hello World'
##composite data types
##list
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives']
## dictionary
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False}
##tuple
fruit = ('blueberry', 'strawberry', 'banana')
##type check
print(type(fruit))
##access value
print(pizza_toppings[1])
##add value to list
pizza_toppings.append('Mushrooms')
# access dictionary value by key name
print(person['name'])
#access and change dictionary value
person['name'] = 'George'
#add key-value pair to dictionary
person['eye_color'] = 'blue'
##access and display value in tuple
print(fruit[2])

#conditional if
if num1 > 45:
    print("It's greater")
else: #conditional else
    print("It's lower")

#length check of string
if len(string) < 5:
    print("It's a short word!")
elif len(string) > 15: #conditional else if
    print("It's a long word!")
else:
    print("Just right!")
#for loop
for x in range(5):#start at 0 stop before 5
    print(x)
for x in range(2,5): #start at 2 stop before 5
    print(x)
for x in range(2,10,3):#sequence 2-10 increasing by 3
    print(x)
x = 0#start for the while
#while loop
while(x < 5):#end condition of while
    print(x)
    x += 1#increment of while loop

pizza_toppings.pop()
pizza_toppings.pop(1)

print(person)
person.pop('eye_color')
print(person)

for topping in pizza_toppings:
    if topping == 'Pepperoni':
        continue #continue skips it
    print('After 1st if statement')
    if topping == 'Olives':
        break #break breaks out of for
#function declaration with empty parameter
def print_hello_ten_times():
    for num in range(10):
        print('Hello')

print_hello_ten_times()
#function with parameter x
def print_hello_x_times(x):
    for num in range(x):
        print('Hello')
#function with 4 as argument
print_hello_x_times(4)

def print_hello_x_or_ten_times(x = 10):
    for num in range(x):
        print('Hello')#log statement

print_hello_x_or_ten_times()
print_hello_x_or_ten_times(4)

#multi-line comment
"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)
