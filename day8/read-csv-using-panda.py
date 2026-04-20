import pandas as pd

def ReadCSV():

  dataFile = pd.read_csv('example.csv')

  first5 = dataFile.head(5)
  last5 = dataFile.tail(5)

  print("\nFirst five elements are: ")
  print(first5)

  print("\nLast five elements are: ")
  print(last5)
