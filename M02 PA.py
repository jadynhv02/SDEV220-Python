"""
Name: Vessels, Jadyn
Date: 01/25/2024
Course: SDEV 220
Instructor: Francis,Christopher
Assignment: M02 Programming Assignment
"""

## CH. 4: Things to Do
## 4.1
print("\nCH. 4: THINGS TO DO")
print("4.1\n")

secret = 8
guess = 8

if guess < secret:
    print("too low!")
elif guess > secret:
    print("too high!")
else:
    print("just right!")
    
print()



## 4.2
print("4.2\n")

small = True
green = False

if small:
    if green:
        print("pea")
    else:
        print("cherry")
else:
    if green:
        print("watermelon")
    else:
        print("pumkin")
        
print()       



## CH. 6: Things to Do
## 6.1
print("CH. 6: THINGS TO Do")
print("6.1\n")

list = [3, 2, 1, 0]
for n in list:
    print(n)

print()



## 6.2
print("6.2\n")

guess_me = 7
number = 1

while True:
    if number < guess_me:
        print("too low")
    elif number == guess_me:
        print("found it!")
        break
    else:
        print("oops")
        break
    number += 1
  
print()
   


## 6.3
print("6.3\n")

guess_me = 9
for number in range(10):    
    if number < guess_me:
        print("too low")  
    elif number == guess_me:
        print("found it!")
        break
    else: 
        print("oops")
        break
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
