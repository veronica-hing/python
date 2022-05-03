#1
def number_of_food_groups():
    return 5
print(number_of_food_groups())
#returns 5

"""
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())
#returns error since days in week not defined
"""
#3
def number_of_books_on_hold():
    return 5
    return 10
print(number_of_books_on_hold())
#returns 5


#4
def number_of_fingers():
    return 5
    print(10)
print(number_of_fingers())
#returns 5

#5
def number_of_great_lakes():
    print(5)
x = number_of_great_lakes()
print(x)
#returns none after printing 5

#6
def add(b,c):
    print(b+c)
    return b + c #added this so print on line 40 can print something
print(add(1,2) + add(2,3))
#prints 3, prints 5 error since no return


#7
def concatenate(b,c):
    return str(b)+str(c)
print(concatenate(2,5))
#returns "2"+"5", so "25"


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:
        return 5
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())
#prints 100, returns 10, so we print 10 in line 60


#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3))
#prints 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#prints 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3))
#prints(7 + 14) which prints 21

#10
def addition(b,c):
    return b+c
    return 10
print(addition(3,5))
#prints( 3+5 which is 8)


#11
b = 500
print(b)
#prints 500
def foobar():
    b = 300 #this is a side-effect
    print(b)
#prints(300) when called
print(b)
#prints(500) since b is still 500
foobar()#changes b to 300
print(b)
#prints 300


#12
print("#12")
b = 500
#reset b to 500
print(b)
#prints 500
def foobar():
    b = 300
    print(b)
    return b
print(b)
#prints 500
foobar()
#prints 300 then changes b to 300
print(b)
#prints 300


#13
print("#13")
b = 500
print(b)
#prints 500
def foobar():
    b = 300
    print(b)
    return b
print(b)
#prints 500
b=foobar()
#prints 300 as side effect
print(b)
#prints 300 since b is 300


#14
def foo():
    print(1)
    bar()
    print(2)
def bar():
    print(3)
foo()
#prints 1, then calls bar to print 3 then prints 2


#15
def foo():
    print(1)
    x = bar()
    print(x)
    return 10
def bar():
    print(3)
    return 5
y = foo()
#prints 1 as side effect, prints 3 as side effect, prints 3 from calling bar prints 5 which is returned from calling bar
print(y)
#prints 10 which is returned from foo()