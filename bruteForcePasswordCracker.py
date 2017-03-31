"""
bruteForcePasswordCracker.py
Zack Scriven
Copyright (C) 2017 Zack Scriven
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

"""
import string

# function to convert a number n from base 10 to base b
def numberToBase(n, b):
	digits = []
	while n:
		digits.append(int(n % b))
		n /= b
	return digits[::-1]

# variables
characters = string.printable[:]
base = len(characters)
solved = False
n = 0
maxAttempts = 999999
password = input("Enter a password")


while !solved and n < maxAttempts:
	charList = numberToBase(n,base)
	passwordGuess = ''
	for x in charList:
		passwordGuess = characters[x]
	
	
	if passwordGuess == password:
		solved = True
		print('_______Statistics______')
		print('Password: ' + passwordGuess)
		print('Attempts: ' + str(n))
	else:
		n += 1