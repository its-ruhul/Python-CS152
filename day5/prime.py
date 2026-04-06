def CheckPrime(num):

  

  isPrime = True

  for i in range(2, int(num ** (1/2)) + 1):
    if num % i == 0:
      isPrime = False
      break

  if isPrime:
    print("The number entered is Prime")
  else:
    print("The number entered is Composite")

  return isPrime

num = int(input("Enter a number: "))
CheckPrime(num)