def FindSecondSmallest():

  array = [] 

  for i in range(0, 5):
    request = "Enter number: " + str(i+1) + ": "
    element = int(input(request))
    array.append(element)

  print("Your entries: ", array)

  for i in range(0, 5):
    for j in range(i+1, 5):
      if (array[i] > array[j]):
        temp = array[i]
        array[i] = array[j]
        array[j] = temp
  
  print("Sorted array: ", array)
  print("The second smallest number is: ", array[1])

FindSecondSmallest()