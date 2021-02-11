# Python program to find the L.C.M. of two input number

# define gcd function
def gcd(x, y):
   """This function implements the Euclidian algorithm
   to find G.C.D. of two numbers"""

   while(y):
       x, y = y, x % y

   return x

# define lcm function
def lcm(x, y):
   """This function takes two
   integers and returns the L.C.M."""

   lcm = (x*y)//gcd(x,y)
   return lcm

def check():
  user_input = input('What are the numbers? (comma separated)')
  numbers = user_input.split(',')

  # change the values of num1 and num2 for a different result
  num1 = int(numbers[0])
  num2 = int(numbers[1])

  # uncomment the following lines to take input from the user
  #num1 = int(input("Enter first number: "))
  #num2 = int(input("Enter second number: "))

  print("The L.C.M. of", num1,"and", num2,"is", lcm(num1, num2))
  check()

check()