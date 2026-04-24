def WriteToFile():
  fileName = input("Enter the name of the folder(.txt): ")+".txt"

  file = open("./" + fileName, "w")

  print("Writing Hello World...")

  file.write("Hello World!")

  file.close()
  
  print("Successfully written to file.")

WriteToFile()