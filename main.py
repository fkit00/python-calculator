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
  



def calcucator():
  first_number=float(input('Please enter your first number '))
# pick an operator 
  operate=input('Please pick an operator ')                  
#take in second number 
  second_number=float(input('Please enter your second number '))
#then return a calucation
  function= operations[operate]
  new_number=math_things(function, first_number, second_number)
  print(new_number)
  response=input(f'Do you want to do another calculation with {new_number}? Type yes or no: ')
  
  while response == 'yes':
    operate=input('Please pick an operator ')                  
    second_number=float(input('Please enter your second number '))
    function= operations[operate]
    new_number=math_things(function, new_number, second_number)
    print(new_number)
    response=input(f'Do you want to do another calculation with {new_number}? Type yes or no: ')
    
  if response == 'no':
    clear()
    print(art.logo)
    calcucator()

  
  

# we want to take in the first number- make it a while set a var

print('welcome to my calculator')
calcucator()


    


  
  



