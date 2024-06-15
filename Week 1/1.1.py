Write a program to convert strings to an integer and float and display its type.

Sample Input:

10

10.9

Sample Output:

10,<class 'int'>

10.9,<class 'float'>



For example:

Input	Result
10
10.9
10,<class 'int'>
10.9,<class 'float'>
a=input()
b=input()
c=int(a)
d=float(b)
d=round(d,1)
print(a,type(c),sep=",")
print(d,type(d),sep=",")
Input	Expected	Got	
10
10.9
10,<class 'int'>
10.9,<class 'float'>
10,<class 'int'>
10.9,<class 'float'>
12
12.5
12,<class 'int'>
12.5,<class 'float'>
12,<class 'int'>
12.5,<class 'float'>
89
7.56
89,<class 'int'>
7.6,<class 'float'>
89,<class 'int'>
7.6,<class 'float'>
55000
56.2
55000,<class 'int'>
56.2,<class 'float'>
55000,<class 'int'>
56.2,<class 'float'>
2541
2541.679
2541,<class 'int'>
2541.7,<class 'float'>
2541,<class 'int'>
2541.7,<class 'float'>
Passed all tests!  
