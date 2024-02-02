"""
Name: Vessels, Jadyn
Date: 02/01/2024
Course: SDEV 220
Instructor: Francis, Christopher
Assignment: M03 Programming Assignment
"""

## CH. 7: Things to Do
## 7.4

things = ['mozzarella', 'cinderella', 'salmonella']


## 7.5
print(things[1].capitalize())

print()
##Question: Capitalizing a single element in things did not change the element in the list

    
##7.6
things[0] = things[0].upper()
print(things)

print()

##7.7
things.pop(2)
print(things)

print()



## CH. 9: Things to Do
##9.1
def good():
    return ['Harry', 'Ron', 'Hermione']
print(good())

print()


##9.2
def get_odd():
    for number in range(1, 10, 2):
        yield number
        
count = 1
for number in get_odd():
    if count == 3:
        print("The 3rd old number is: ", number)
        break
    else:
        count +=1




































