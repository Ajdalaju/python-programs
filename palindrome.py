#!/usr/bin/python3
x = input('Enter the word :')
x = x.lower() #converts the word into lower case

def palindome(x):
 # Set doc string

 if x[::-1] == x: #reverse of the word equals to the word
  print('It is palindrome')
 else:
  print('It is not palindrome') 

palindome(x)
