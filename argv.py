#!/bin/python
import sys

print("you typed : ", str(sys.argv))
print("0 ->", str(sys.argv[0]))
print("1 ->", str(sys.argv[1]))
print("2 ->", str(sys.argv[2]))
print("3 ->", str(sys.argv[3]))


'''
┌──(user㉿kali)-[~]
└─$ python3 argv.py this is python
you typed :  ['argv.py', 'this', 'is', 'python', '3']
0 -> argv.py
1 -> this
2 -> is
3 -> python
'''