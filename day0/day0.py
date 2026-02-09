def basics():
  print('Hello World')

  a = int(input('Enter a number: '))
  b = int(input('Enter another number: '))
  print(a+b)

  #Differenet data structure
  string = "My name is "
  integer = 45
  boolean = True
  list1 = [1, 2, 3, 4, 5]
  tuple1 = (6, 7, 8, 9)
  dictionary = {1: "one", 2: "two", 3: "three"}

  print(string, integer, list1, boolean, tuple1, dictionary)

#GeeksforGeeks: Python Data Types
def GeeksForGeeks():
  a = 5         #int
  print(type(a))

  b = 5.0       #float
  print(type(b))

  c = 2 + 4j    #complex
  print(type(c))

  s = 'Welcome to Geeks World'
  print(s)
  print(type(s))

  print(s[1])
  print(s[2])
  print(s[-1])

  a = ["Geeks", "For", "Geeks"]
  print("Accessing element from the list")
  print(a[0])
  print(a[2])

  print('Accessing elements using negative indexing')
  print(a[-1])
  print(a[-3])

def Tuples():
  tup1 = (1, 2, 3, 4, 5)
  tup2 = ('Geeks', 'For')

  print("\n Tuple with the use of String: ", tup2)

  print(tup1[0])
  print(tup1[-1])
  print(tup1[-3])

def Booleans():
  print(type(True))
  print(type(False))
  #print(type(true))

def TruthFalsy():
  
  if 1:
    print('1 is truthy')
  
  if not 0:
    print('0 is falsy')

# Set items cannot be accessed by using indexes
# We can loop through the set items
def Sets():

  s1 = set()

  #Sets items for each letter without duplication
  s1 = set("GeeksForGeeks")
  print(s1)

  s2 = set(["Geeks", "For", "Geeks"])
  print(s2)

  #Duplicate set items are removed automatically
  set1 = set(['Geeks', 'For', 'Geeks'])
  
  print(set1)

  for i in set1:
    print(i, end=" ")

  print('Geeks' in set1)

def Dictionaries():

  d = {1: 'Geeks', 'name': 'For', 3: 'Geeks', }
  print(d)

  d1 = dict({1: 'Geeks', 2: 'For', 3: 'Geeks'})
  print(d1)

  print(d['name'])
  print(d.get(3))

  #d2 = dict([1, 2, 3, 4, 5])
  #ERROR: object is not iterable
  #print(d2)

Dictionaries()