def CheckPalindrome():

  string = input("Enter a number to check if it is a PALINDROME: ")

  l = len(string)

  isPalindrome = True

  for i in range(l):
    if string[i] != string[-i-1]:
      isPalindrome = False
      break

  if isPalindrome:
    print("The string is a Palindrome!")
  else:
    print("The string is not a Palindrome")

CheckPalindrome()