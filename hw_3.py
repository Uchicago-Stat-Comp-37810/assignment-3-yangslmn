# Name: Seulmin, Yang
import math
import random
# hw3.py

##### Template for Homework 3, exercises 1 -  ######


# ********** Exercise 1 ********** 

# Define is_divisible function here
def is_divisible(m,n):
    if(n==0) :
        print("False")
    elif (m % n != 0):
        print("False")
    else:
        print("True")

is_divisible(9,3)

is_divisible(10,5)
is_divisible(18,7)
is_divisible(42,0)

# Test cases for is_divisible
## Provided for you... uncomment when you're done defining your function

is_divisible(10, 5)

is_divisible(18, 7)
is_divisible(42, 0)

# ********** Exercise 2 ********** 

# Define not_equal function here
def not_equal(x,y):
    if(x-y == 0):
        print('False')
    else:
        print('True')



# Test cases for not_equal
##### YOUR CODE HERE #####
not_equal(2,2)
not_equal(2,3)

# ********** Exercise 3 ********** 

## 1 - multadd function
def multadd(a,b,c):
    result= a*b + c
    return (result)
multadd(2,4,8)

## 2 - Equations
##### YOUR CODE HERE #####
angle_test = multadd( math.cos(math.pi/4), 1/2, math.sin(math.pi/4))
ceiling_test = multadd(math.log(12,7), 2, math.ceil(276/19) )

# Test Cases
angle_test = multadd( math.cos(math.pi/4), 1/2, math.sin(math.pi/4))
print( "sin(pi/4) + cos(pi/4)/2 is:")
print(angle_test)

ceiling_test = multadd(math.log(12,7), 2, math.ceil(276/19) )
print ("ceiling(276/19) + 2 log_7(12) is:")
print (ceiling_test)


# ********** Exercise 4 **********

## 1 - rand_divis_3 function
def rand_divis_3():
    num = random.randint(0,100)
    print(num)
    if (num % 3)== 0 :
        return('True')
    else:
        return('False')


# Test Cases
##### YOUR CODE HERE #####
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())
print(rand_divis_3())