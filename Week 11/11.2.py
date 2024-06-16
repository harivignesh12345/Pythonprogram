Write a Python program that asks the user for their age and prints a message based on the age. Ensure that the program handles cases where the input is not a valid integer.

Input Format: A single line input representing the user's age.

Output Format: Print a message based on the age or an error if the input is invalid.


For example:

Input	Result
twenty
Error: Please enter a valid age.
25
You are 25 years old.
-1
Error: Please enter a valid age.

try:
    a=int(input())
    if a>-1:
        print(f"You are {a} years old.")
    else:
        raise Exception
except:
    print("Error: Please enter a valid age.")
  Input	Expected	Got	
twenty
Error: Please enter a valid age.
Error: Please enter a valid age.
25
You are 25 years old.
You are 25 years old.
-1
Error: Please enter a valid age.
Error: Please enter a valid age.
150
You are 150 years old.
You are 150 years old.
Error: Please enter a valid age.
Error: Please enter a valid age.