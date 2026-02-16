num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
num3 = int(input("Enter the 3rd number: "))

if num1 > num2:
  if num3 > num1:
    biggest = num3
  else:
    biggest = num1
else:
  if num3 > num2:
    biggest = num3
  else:
    biggest = num2

print("The biggest number is:", biggest)