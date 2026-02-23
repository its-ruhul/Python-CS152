def LCM(num1, num2):

  if num1 > num2:
    smaller = num2
  else:
    smaller = num1

  for i in range(smaller, num1 * num2 ):
    if (i % num1 == 0 and i % num2 == 0 ):
      return i
    
def HCF(num1, num2):

  if num1 > num2:
    smaller = num2
  else:
    smaller = num1

  for i in range(smaller, 1, -1):
    if (num1 % i == 0 and num2 % i == 0):
      return i
    
num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))

print(LCM(num1, num2))
print(HCF(num1, num2))
  
