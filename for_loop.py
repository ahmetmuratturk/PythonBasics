#To loop through a set of code a specified number of times, we can use the range() function,
#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number.

# exercise 1 ***************************************************************************

for i in range(5,21):
  print(i)
print('Loop has been completed\n')

# exercise 2 ***************************************************************************


for i in range(1,101):
  if i % 5 == 0:
    print(i)
 
print('Loop has been completed\n')


# exercise 3 ***************************************************************************

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9,10]
for i in numbers:
  print(i)
 
print('Loop has been completed\n')


# exercise 4 ***************************************************************************

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3):
    
for x in range(2, 30, 3):
  print(x)
print('Loop has been completed\n')  

# exercise 5 ***************************************************************************


#With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
print('Loop has been completed\n')    

# exercise 6 ***************************************************************************


#Loop through the letters in the word "banana"
for x in "banana":
  print(x)
print('Loop has been completed\n')    

# exercise 7 ***************************************************************************

#With the break statement we can stop the loop before it has looped through all the items 
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break    
print('Loop has been completed (actually it\'s not) \n')   

# exercise 8 ***************************************************************************


#Exit the loop when x is "banana", but this time the break comes before the print
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x) 
print('Loop has been completed\n')    

# exercise 9 ***************************************************************************

#With the continue statement we can stop the current iteration of the loop, and continue with the next  
fruits = ["apple", "banana", "cherry", "dragon fruit"]
for x in fruits:
  if x == "banana":
    continue
  print(x)
print('Loop has been completed\n')    


# exercise 10 ***************************************************************************

#The "inner loop" will be executed one time for each iteration of the "outer loop"

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y) 
    
# exercise 11 ***************************************************************************


    