Ramesh’s basic salary is input through the keyboard. His dearness allowance is 40% of his basic salary, and his house rent allowance is 20% of his basic salary. Write a program to calculate his gross salary.

Sample Input:

10000

Sample Output:

16000



For example:

Input	Result
10000
16000
a=int(input())
b=0.4*a
c=0.2*a
d=a+b+c
print(int(d))
Input	Expected	Got	
10000
16000
16000
20000
32000
32000
28000
44800
44800
5000
8000
8000
