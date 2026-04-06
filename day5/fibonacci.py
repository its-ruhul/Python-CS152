def Fibonacci(n):

  a = 0
  b = 0
  c = 1

  for i in range(n):
    print(a + b , end=" ")
    b = a + b
    a = c
    c = b

n = int(input("Enter a number: "))
Fibonacci(n)
    


