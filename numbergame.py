#!/usr/bin/python
import time
print('type in your name')
name=raw_input()
print(name+' is avery nice name')
time.sleep(0.5)
print('type in a number any number')
number=raw_input()
number=1
while number!='0':
    print('type in a number any number')
    intedger=raw_input()
if number==int('0'):
    print('bye')
