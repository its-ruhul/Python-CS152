def reverseLines():
  fileRead = input("Enter the name of the folder(.txt) to read: ")+".txt"

  file = open(fileRead, "r")
  lines = file.readlines()
  file.close()

  lines.reverse()

  lines[0] += '\n'

  for i in lines:
    print(i, end="")

reverseLines()