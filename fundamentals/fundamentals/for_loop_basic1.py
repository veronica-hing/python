for num in range(0,151):
    print(num)

for num in range(5,1001,5):
    print(num)

for num in range(1,101):
    str = ""
    if num % 5 == 0:
        str += "Coding"
    if num % 10 == 0:
        str += " Dojo"
    if len(str) == 0:
        print(num)
    else:
        print(str)

sum = 0
for num in range(1,500000,2):
    sum += num
print(sum)

for num in range(2018, 0, -4):
    print(num)

def flexCounter(lowNum = 2, highNum = 9, mult = 3):
    for num in range(lowNum, highNum+1):
        if(num % mult == 0):
            print(num)

flexCounter()
