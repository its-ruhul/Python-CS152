def copyPaste(readFile, writeFile="default.txt"):

  fileCopy = open(readFile, 'r')
  data = fileCopy.readlines()

  filePaste = open(writeFile, 'w')
  filePaste.writelines(data)

def UI():
  readFile = input("Enter the file to copy: ")
  writeFile = input("Enter the file to paste: ")

  if readFile == '':
    print("ERROR: Copy file not mentioned! \n")
    UI()

  copyPaste(readFile, writeFile)
  print("Copied and pasted successfully!")

UI()