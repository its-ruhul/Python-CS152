#-----------------------------------------------#

# This is a single-line comment

"""
This is a
multi-line comment
or docstring.
"""

#-----------------------------------------------#

x = "Hello World"                 # str
x = 50                            # int
x = 60.5                          # float
complex = 3j                      # complex
x = ["geeks", "for", "geeks"]     # list 
x = ("geeks", "for", "geeks")     # tuple
x = {"name": "Suraj", "age": 24}  # dict
x = {"geeks", "for", "geeks"}     # set
x = True                          # bool
binary = b"Geeks"                 # binary
print(x)

#-----------------------------------------------#

#type() function gives output: <class '[datatype]'>
#type() takes 1 or 3 arguments ???
print(type(complex))
print(type(binary))

#-----------------------------------------------#

# Use .split() method to take more than one inputs in Python

x, y, z = input("Enter three values: ").split()
print("Total number of students: ", x)
print("Number of boys is : ", y)
print("Number of girls is : ", z)

#-----------------------------------------------#

print("Hello, World!")
#sys.stdout.write("Hello, World!")
print(f"Hello, World!")

#-----------------------------------------------#



#-----------------------------------------------#



#-----------------------------------------------#