def TypeOfNum():

  N = int(input("Enter how many numbers you want to add: "))

  oddNo = 0
  evenNo = 0
  positiveNo = 0
  negativeNo = 0
  array = []

  for i in range(N):
    a = int(input("Enter a number: "))

    if a % 2 == 0:
      evenNo += 1
    else:
      oddNo += 1

    if a < 0:
      negativeNo += 1
    elif a > 0: 
      positiveNo += 1
    else:
      print("0 is neither positive nor negative!")

    array.append(a)
  
  print("No of odd numbers: ", oddNo)
  print("No of even numbers: ", evenNo)
  print("No of positive numbers: ", positiveNo)
  print("No of negative numbers: ", negativeNo)

TypeOfNum()