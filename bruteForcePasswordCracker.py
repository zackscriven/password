"""
bruteForcePasswordCracker.py
Zack Scriven
Copyright (C) 2017 Zack Scriven
 
This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.
"""
import time
import string

maxattempts = 100000
start       = time.time()
chars       = list(string.printable)[:95]
base        = len(chars)
n           = 0
solved      = False
password    = input("Enter your password:")


print(chars)

# converts number N base 10 to a list of digits base b
def numberToBase(n, b):
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


# check edge cases like empty, or 0
if password == '':
    print('Your password is empty')
    solved = True
    
elif password == chars[n]:
    print('Your password is ' + chars[n])
    solved = True
    
else:
    n = 1






# begin systematically checking passwords
if not solved:
    while n < maxattempts:
        lst = numberToBase(n, base)
        print(lst)
        word = ''
        for x in lst:
            word += str(chars[x])
        print(word)
        if password == word:
            solved = True
            print('-Stats-')
            print('Pass: ' + word)
            print('Attempts: ' + str(n))
            print('time: ' + str((time.time() - start)) + ' sec')
            break
        else:
            n += 1

# the password is beyond our maxattempts
if not solved:
    print('Unsolved after ' + str(n) + ' attempts!')
