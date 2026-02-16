a = int(input("Enter a number a: "))

if a % 2 == 0:
  print('The number entered is even', end=" ")
else:
  print('The number entered is odd', end=" ")

if a > 0:
  print('and positive')
elif a < 0:
  print('and negative')
else:
  print('and zero')