def CheckListEquality(list1, list2):

  isEqual = True

  if len(list1) == len(list2):

    for i in range(0, len(list1)):
      if list1[i] != list2[i]:
        isEqual = False
        return isEqual

    return isEqual
  
  return False

def InputList():
  arrayLen = int(input("Enter the no. elements in the list: "))

  array = []

  for i in range(arrayLen):
    inputText = "Enter element " + str(i) + ": "
    elem = input(inputText)
    array.append(elem)

  return array

array1 = InputList()
array2 = InputList()

if CheckListEquality(array1, array2):
  print("The two lists are equal")
else:
  print("The two lists are not equal")