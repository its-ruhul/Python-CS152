def reverseLines():
  fileRead = input("Enter the name of the folder(.txt) to read: ")+".txt"

  file = open(fileRead, "r")
  lines = file.readlines()
  file.close()

  for i in lines:
    i = i[::-1]

  lines[-1] += '\n'

  for i in lines:
    print(i, end="")

reverseLines()