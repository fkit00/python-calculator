import art
print(art.logo)

def multiply(a,b):
  return a*b

def divide(a,b):
  return a/b

def add(a,b):
  return a+b

def minus(a,b):
 return a-b




operations={
  "+":add,
  "-":minus,
  "*": multiply,
  "/":divide
}
# we want to take in the first number
print('welcome to my calculator')
first_number=int(input('Please enter your first number '))
# pick an operator 
operate=input('Please pick an operator ')                  
#take in second number 
second_number=int(input('Please enter your second number '))
#then return a calucation
function= operations[operate]
print(function(first_number, second_number))
#ask if they want to continue calculation with the result or press 'n' to start a new calculation- n will clear the screen 
#for y we want to call whatevers next with the first thing





