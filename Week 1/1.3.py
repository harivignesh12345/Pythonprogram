Write a simple python program to find the square root of a given floating point number. The output should be displayed with 3 decimal places.

Sample Input:

8.00

Sample Output:

2.828





For example:

Input	Result
14.00
3.742
import math
a=float(input())
b=math.sqrt(a)
print("%.3f"%b)
Input	Expected	Got	
Input	Expected	Got	
8.00
2.828
2.828
14.00
3.742
3.742
4.00
2.000
2.000
487
22.068
22.068
