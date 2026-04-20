def Add(a, b):
  return a+b

def Subtract(a,b):
  return a-b

def Multiply(a,b):
  return a*b

def Divide(a,b):
  return a/b

def Arithematic():

  print("\n SELECT THE DESIRED OPERATION:")
  print("Type [-] for subtract \nType [+] for addition")
  print("Type [*] for mulitiplication \nType [/] for division")

  func = input("Enter the operation you want to perform: ")

  a = int(input("Enter the first number: "))
  b = int(input("Enter the second number: "))

  if func == '-':
    ans = Subtract(a,b)
  elif func == '+':
    ans = Add(a,b)
  elif func == '*':
    ans = Multiply(a,b)
  elif func == '/':
    ans = Divide(a,b)
  else:
    print("Invalid input! Please try again \n")
    Arithematic()

  print("Your answer is:", ans)

Arithematic()

  