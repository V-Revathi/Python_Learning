#comments
# this is the first comment
spam = 1  # and this is the second comment
          # ... and now a third!
text = "# This is not a comment because it's inside quotes."

# Python as a Calculator:
# Numbers
x=10
y=20
print(x+y) 
# Output = 30.
  

#Division(/) always returns float value and returns the quotient.
Sample1 = (50 - 5*6) / 4
print("(50 - 5*6) / 4",Sample1) # output  = 5.0

#Floor Division(//) returns integer value and returns the quotient.
Sample2 = (50 - 5*6) // 4
print("(50 - 5*6) // 4",Sample2) # output  = 5

# % returns the integer value and returns the remainder.
Sample3 = 17 % 3
print("17 % 3",Sample3) # output  = 2

# returns the integer value and ** returns the power value.
Sample4 =  5 ** 2 
print("5 ** 2",Sample4) # output  = 25

#In interactive mode, the last printed expression is assigned to the variable _. But this is not good practice. We need to define a variable and assign the value.
tax = 12.5 / 100
price = 100.50
print(price * tax)
#12.5625
print(price + _)
#113.0625

#Text

Sample5 = 'spam eggs'  #Single quote
print(Sample5)
# spam eggs

Sample6 = "spam eggs"  #Double quotes
print(Sample6)
# spam eggs

#use \' to escape the single quote.... 
Sample7 = 'doesn\'t' 
print("Sample7",Sample7) #output = doesn't 

Sample8 = "doesn't"
print("Sample8",Sample8) #output = doesn't 

#To Escape we use \ , To Newline we use \n , To print raw data we use r 
print('C:\some\name') # here \n means newline!

#Output: 
#C:\some
#ame

print(r'C:\some\name')
#Output = C:\some\name

#Strings can be concatenated with the + operator & repeated with *.
Sample9 = 4*'Rev' + 'Shefu'
print(Sample9)
# RevRevRevRevShefu

#Two or more string literals (i.e. the ones enclosed between quotes) next to each other are automatically concatenated.
Sample10 = 'Revathi' 'V' 'Shefu'
print(Sample10)
# RevathiVShefu

#Strings are immutable, we cant insert the values in string and we can only access it. The negative index starts with -1.
 Word = 'Revathi'
>>> print(Word[0])
# R
print(Word[-1])
# i
print(Word[0:6])
# Revath
print(Word[0:])
# Revathi
print(Word[:4])
# Reva
print(Word[:-3])
# Reva

print(word[22])
# Traceback (most recent call last):
#   File "<python-input-104>", line 1, in <module>
#     print(word[22])
#           ~~~~^^^^
# IndexError: string index out of rang

#List 

sampleList = ['Revathi' , "10" , 20 , 'shefu'] 
print("List",sampleList)
# List ['Revathi', "10", 20, 'shefu']

len(sampleList) 
# 4

squares = [1, 4, 9, 16, 25]
print(squares)
# [1, 4, 9, 16, 25]

print(squares[0])  # indexing returns the item
# 1
print(squares[-1])
# 25
print(squares[-3:])  # slicing returns a new list
[9, 16, 25]

# lists are a mutable type
cubes = [1, 8, 27, 65, 125]  # something's wrong here
# 4 ** 3  # the cube of 4 is 64, not 65!
# 64
cubes[3] = 64  # replace the wrong value
print(cubes)
# [1, 8, 27, 64, 125]

# add new items at the end of the list, by using the list.append() method
cubes.append(216)  # add the cube of 6
cubes.append(7 ** 3)  # and the cube of 7
print(cubes)
# [1, 8, 27, 64, 125, 216, 343]

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

# 0
# 1
# 1
# 2
# 3
# 5
# 8

# keyword argument end can be used to avoid the newline after the output
a,b=0,1
    while a < 1000:
     print(a,end=',')
     a, b = b, a+b

# 1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
