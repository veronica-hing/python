print("1. Update Values in Dictionaries and Lists")
x = [ [5,2,3], [10,8,9] ]
#update value in list
x[1][0] = 15
print(x)
students = [
    {'first_name':  'Michael', 'last_name' : 'Jordan'},
    {'first_name' : 'John', 'last_name' : 'Rosales'}
]
#update value in dictionary that's in a list
students[0]['last_name'] = 'Bryant'
print(students)
sports_directory = {
    'basketball' : ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer' : ['Messi', 'Ronaldo', 'Rooney']
}
#update value in dictionary that's in a dictionary
sports_directory['soccer'][0] = 'Andres'
print(sports_directory)
z = [ {'x': 10, 'y': 20} ]
#change z from 20 to 30
z[0]['y'] = 30 # dictionary is in a 1 item list
print(z)

print("2. Iterate through a List of Dictionaries")

students = [
        {'first_name':  'Michael', 'last_name' : 'Jordan'},
        {'first_name' : 'John', 'last_name' : 'Rosales'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]

def iterateDictionary(listy):
    for val in range(len(listy)): #go through each item in list
        line = ""#this is the string we will print
        for key in listy[val]: #read out the first and last name
            line += (f"{key} - {listy[val][key]},")
        line = line[:-1]
        print(line)

iterateDictionary(students) 
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)
"""first_name - Michael, last_name - Jordan
first_name - John, last_name - Rosales
first_name - Mark, last_name - Guillen
first_name - KB, last_name - Tonel
"""
print("3. Get values from a List of Dictionaries")
#given a key name and a list, print values stored in that key for each dictionary
def iterateDictionary2(key_name, some_list):
    for val in range(len(some_list)):
        print(some_list[val][key_name])

iterateDictionary2('first_name',students)
iterateDictionary2('last_name',students)

print("4. Iterate through a Dictionary with List Values")
dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}

def printInfo(dict_of_lists):
    #we start with the keys since dictionaries are indexed by keys
    for deet_key in dict_of_lists:
        list_len = len(dict_of_lists[deet_key])
        print(f"{list_len} {deet_key.upper()}")
        #when we put the key in the dict of lists we get a list that we iterate through
        for val in range(list_len):
            print(dict_of_lists[deet_key][val])
                #dictionary[deet_key] gives us a list
                # when we have the list, listy[val] gives us the value at that index

printInfo(dojo)
"""# output:
7 LOCATIONS
San Jose
Seattle
Dallas
Chicago
Tulsa
DC
Burbank
    
8 INSTRUCTORS
Michael
Amy
Eduardo
Josh
Graham
Patrick
Minh
Devon
"""