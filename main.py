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
# we want to take in the first number
print('welcome to my calculator')

#ask if they want to continue calculation with the result or press 'n' to start a new calculation- n will clear the screen 
#for y we want to call whatevers next with the first thing

def calcucator():
  first_number=int(input('Please enter your first number '))
# pick an operator 
  operate=input('Please pick an operator ')                  
#take in second number 
  second_number=int(input('Please enter your second number '))
#then return a calucation
  function= operations[operate]
  new_number=function(first_number, second_number)
  print(new_number)
  response=input(f'Do you want to do another calculation with {new_number}? Type yes or no: ')
  return response

calcucator()

if calcucator() =='yes':
  operate=input('Please pick an operator ')  
  second_number=int(input('Please enter your second number '))
  function= operations[operate]
  new_number=function(first_number, second_number)
  print(new_number)  

elif calcucator() == 'no':
  clear()
  calculator()

    


  
  



