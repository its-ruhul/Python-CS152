import os

def FileAccess():
  fileName = input("Enter the name of the folder: ")

  if os.access(fileName, os.F_OK):
    print("The file exists")

    if os.access(fileName, os.R_OK):
      print("The file has read access.")
    else:
      print("The file doesn't have read access")

    if os.access(fileName, os.W_OK):
      print("The file has write access")
    else:
      print("The file doesn't have write access")

    if os.access(fileName, os.X_OK):
      print("The file has execution access")
    else:
      print("The file doesn't have execution access")
  else:
    print("ERROR 404: File not found.")

FileAccess()