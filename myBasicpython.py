# function for addition

def add(a,b):
    total = a + b
    print total
    return total

add(3,6)

assert add(3,6) == 9

# function for multiplication

def mul(a,b,c):
    total = a * b * c
    print total
    return total

mul(2,4,6)

assert mul(2,4,6) == 48

# function for addition of list / version 1

numbers = [1,2,3,5]

def addOfList(myListNumbers):
    total = myListNumbers[0] + myListNumbers[1] + myListNumbers[2] + myListNumbers[3]
    print total
    return total

addOfList(numbers)

assert addOfList(numbers) == 11

# function for addition of list / version 2

numbers2 = [1,2,3,4,5,6,7,8,9]
numbers3 = [100,340,569]

def addOfList2(myList):
    total = 0
    for num in myList:
        total = total + num
    print "Result version 2"
    print total
    return total

addOfList2(numbers2)

addOfList2(numbers3)

assert addOfList2(numbers2) == 45
assert addOfList2(numbers3) == 1009
