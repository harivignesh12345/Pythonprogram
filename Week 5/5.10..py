Write a program to check if two strings are balanced. For example, strings s1 and s2 are balanced if all the characters in the s1 are present in s2. The character’s position doesn’t matter. If balanced display as "true" ,otherwise "false".


For example:

Input	Result
Yn
PYnative
True
s1 = input()
s2 = input()


set_s1 = set(s1)
set_s2 = set(s2)


if set_s1.issubset(set_s2):
    print("True")
else:
    print("False")
  Input	Expected	Got	
Yn
PYnative
True
True
Ynf
PYnative
False
False
  
