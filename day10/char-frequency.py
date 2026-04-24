def charFrequency():
  fileName = input("Enter the name of the folder(.txt): ")+".txt"

  file = open(fileName, "r")

  freq = {}

  fileData = file.read()

  for char in fileData:
    if char in freq.keys():
      freq[char] += 1
    else:
      freq[char] = 1

  file.close()

  print("Frequencies of characters in", fileName+" :")
  
  for i in freq:
    print(repr(i), ':', freq[i], 'times')

charFrequency()
