Write a Python program that performs division and modulo operations on two numbers provided by the user. Handle division by zero and non-numeric inputs.

Input Format:

Two lines of input, each containing a number.

Output Format:

Print the result of division and modulo operation, or an error message if an exception occurs.

For example:

Input	Result
10
2
Division result: 5.0
Modulo result: 0
7
3
Division result: 2.3333333333333335
Modulo result: 1
8
0
Error: Cannot divide or modulo by zero.

 try:
    a=float(input())
    b=float(input())
    c=a/b
    d=a%b
    print(f"Division result: {c}")
    print(f"Modulo result: {int(d)}")
except ZeroDivisionError:
    print("Error: Cannot divide or modulo by zero.")
except ValueError:
    print("Error: Non-numeric input provided.")
Input	Expected	Got	
10
2
Division result: 5.0
Modulo result: 0
Division result: 5.0
Modulo result: 0
7
3
Division result: 2.3333333333333335
Modulo result: 1
Division result: 2.3333333333333335
Modulo result: 1
8
0
Error: Cannot divide or modulo by zero.
Error: Cannot divide or modulo by zero.
abc
5
Error: Non-numeric input provided.
Error: Non-numeric input provided.
