"""
randomPasswordGenerator.py
Zack Scriven
Copyright (C) 2017 Zack Scriven
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

"""

import string
import random

def generatePassword(num):
	password = ''
	
	for n in range(num):
		x = random.randint(0,94)
		password += string.printable[x]
	
	return password

	
# generate and print a 16 character random password
print generatePassoword(16)