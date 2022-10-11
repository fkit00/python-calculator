# we want to take in the first number
# pick an operator 
#take in second number 
#then return a calucation
#ask if they want to continue calculation with the result or press 'n' to start a new calculation- n will clear the screen 
#for y we want to call whatevers next with the first thing

import art


print(art.logo)
print('welcome to my calculator')

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

function= operations["+"]
print(function(2,3))