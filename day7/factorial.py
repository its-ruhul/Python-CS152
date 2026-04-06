def Factorial(fact):

  if fact != 1:
    factorial = fact * Factorial(fact-1)
  else:
    factorial = 1

  return factorial

a = input("Enter the number to find its factorial: ")
print(a)