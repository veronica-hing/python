print("Countdown")
def countdown(num):
    list = []
    for val in range(num, -1, -1):
        list.append(val)
    return list
print(countdown(5))

print("Print and Return")
def print_and_return(list):
    #prints first val and returns second
    print(list[0])
    return list[1]
print(print_and_return([1,2]))

print("First Plus Length")
def first_plus_length(list):
    return list[0] + len(list)
print(first_plus_length([1,2,3,4,5]))

print("Values greater than second")
def values_greater_than_second(list):
    newList = []
    if(len(list) < 2):
        return False
    filter = list[1] #get the second value in list
    for val in range(0, len(list)):
        if(list[val] > filter):
            newList.append(list[val])
    ##end for loop going through parameter list
    print(len(newList))
    return newList
print(values_greater_than_second([5,2,3,2,1,4]))

print("This length, That value")
# returns list of length parameter1, with values parameter2
def length_and_value(length, value):
    list = []
    for val in range(length):
        list.append(value)
    return list
print(length_and_value(4,7))
