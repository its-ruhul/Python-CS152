def MakeArrays():

  array = []

  for i in range(10):
    a = int(input("Enter a number: "))
    array.append(a)

  for i in range(10):
    for j in range(i+1, 10):
      if (array[i] > array[j]):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp

  print("Biggest number is: ", array[9])
  print("Smallest number is: ", array[0])

MakeArrays()