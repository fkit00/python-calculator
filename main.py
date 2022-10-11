import art
from replit import clear 

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

def math_things(a, b, c):
  return a(b,c)
  
new_number

def calcucator():
  first_number=int(input('Please enter your first number '))
# pick an operator 
  operate=input('Please pick an operator ')                  
#take in second number 
  second_number=int(input('Please enter your second number '))
#then return a calucation
  function= operations[operate]
  new_number=math_things(function, first_number, second_number)
  print(new_number)
  response=input(f'Do you want to do another calculation with {new_number}? Type yes or no: ')
  return response

# we want to take in the first number

print('welcome to my calculator')

if calcucator() == 'yes':
  number=int(input('please pick a number '))
  operate=input('Please pick an operator ')
  function= operations[operate]
  new_number=math_things(function, new_number, number)
  print(new_number)
  



    


  
  



