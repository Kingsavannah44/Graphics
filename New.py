class Calculator:
 def __init__(self) -> None:
  pass
 
 def add(self,x,y):
  return x+y
 
 def subtract(self,x,y):
  return x-y

 def multiply(self,x,y):
  return x*y

 def divide(self,x,y):
  if y!=0:
   return x/y
  else:
   return"Error:cannot divide by zero"

def main():
 new=Calculator() #create an instance of New class
 print ("welcome to the oblect oriented-oriented New!")
 while True:
  print("\nOPtions:")
  print("1.Add")
  print("2.Subtract")
  print("3.Multiply")
  print("4.Divide")
  print("5.Exit")

  choice= input("Enter your choice (1/2/3/4/5):")

  if choice=='5':
   print("Goodbye!")
   break
  
  num1 =float(input("Entor the second number:"))
  num2=float(input("Enter the second number:"))


  if choice=='1':
   print("Results",new.add(num1,num2))
  elif choice =='2':
    print("Results",new.subtract(num1,num2))
  elif choice =='3':
    print("Results",new.multiply(num1,num2))
  elif choice =='4':
   print("Results",new.divide(num1,num2))
  else:
   print("invalid choice.please select a valid option.")
   