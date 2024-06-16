An automorphic number is a number whose square ends with the number itself.

For example, 5 is an automorphic number because 5*5 =25. The last digit is 5 which same

as the given number.

If the number is not valid, it should display “Invalid input”.

If it is an automorphic number display “Automorphic” else display “Not Automorphic”.

Input Format:

Take a Integer from Stdin Output Format: Print Automorphic if given number is Automorphic number,otherwise Not Automorphic Example input: 5 Output: Automorphic Example input: 25 Output: Automorphic Example input: 7 Output: Not Automorphic

For example:

Test	Result
print(automorphic(5))
Automorphic
def automorphic(n):
    square = n * n
    if str(square).endswith(str(n)):
        return "Automorphic"
    else:
        return "Not Automorphic"
 

Test	Expected	Got	
print(automorphic(5))
Automorphic
Automorphic
print(automorphic(7))
Not Automorphic
Not Automorphic
