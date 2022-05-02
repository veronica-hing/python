# Python and JavaScript

## why python
- easy syntax
- readable
- popular

# Syntax: Python vs JS

## Js

function addTwoNumbers(a,b) {
    var total = a + b;
    console.log(total);
    return total;
}

## Python

def add_two_numbers(a, b):
    total = a + b
    print(total)
    return total

## differences
| javaScript        | python            |
|-------------------|-------------------|
| function          | def               |
| {}                | :                 |
| console.log()     | print()           |
| variable dec      | no declaration    |
| indents dont matter| indent matters   |
| if, else if, else | if, elif, else    |
| ===               | ==                |
| camelCase         | snake-case, PascalCase|
| \|\|, &&, !       | or, and, not      |

# Data types

| js | py | js ex | py ex |
| ---|----|-------|-------|
| string | string|" ", ' ', \` \`| " ", or ' ' |
| bool | bool| true or false | True, False |
| arr | list| [...] | [...]|
| ints |numbers| 1,2,3 | 1,2,3|
| floats | numbers| 1.0, 2.2 | 1.0, 2.2 |
| obj|dictionary| { } | { } |
    ** when declaring dictionaries, use {}
    ** when using dictionaries, use []

| JS        | PY             |
|-----------|----------------|
|arr.push() | list.append()  |
|arr.pop()  | list.pop(index)|
| /**/ or //| """  or  #     |
| (i=10; i>10; i--)| i in range(10, 0, -1)
| array.forEach((elem) => {})| for element in array:|
|arr.length | len(arr)       |

# Food for thought
- () are used for prioritizing the things in it to be calculated first.
- need to typecast things to match or with strings, need to use specific formatting techniqes
- key names for key-value pairs in dictionaries MUST be strings
- dictionaries MUST use rectangle brackets
    ex:

        student = {
            "first-name" : "jon",
            "last-name" : "doe",
            "age" : 24
        }

        print(student["first-name])

    looping through a dictionary:

        for key in student:
            print(key, student[key])