def IsPalindrome(string):

  if string == string[::-1]:
    return True
  else:
    return False
  
a = input("Enter a string 1: ")

def Reverse(string):
  
  if string:
    altStr = string[0:(len(string)-1)]
    reverse = string[-1] + Reverse(altStr)
    return reverse
  else:
    return ""


if IsPalindrome(a):
  print("The string is palindrome")
else:
  print("The string is not a palindrome")

if a == Reverse(a):
  print("The string is a palindrome (recursion)")
else: 
  print("The string is not a palindrome (recursion)")